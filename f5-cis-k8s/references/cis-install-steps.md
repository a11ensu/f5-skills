# CIS Manual Installation Steps

This document contains the detailed step-by-step procedure for installing
F5 BIG-IP Container Ingress Services (CIS) on Kubernetes using the manual method.

The Agent should follow these steps in order when performing a CIS installation.

Official reference: https://clouddocs.f5.com/containers/latest/userguide/cis-installation.html

---

## Prerequisites

Before installing CIS, verify the following:

1. **Kubernetes cluster is UP** and all nodes are Ready.
2. **kubectl** works and can reach the cluster.
3. **CNI plugin** is installed (Cilium, Flannel, or Calico) -- all nodes Ready.
4. **BIG-IP prerequisites:**
   - AS3 3.18+ installed on BIG-IP.
   - A dedicated partition created on BIG-IP for CIS-managed objects:
     ```
     tmsh create auth partition <cis_managed_partition>
     ```
   - A user with Administrator role access to that partition.
5. **For Cluster mode with VXLAN:**
   - BIG-IP must have a VXLAN tunnel configured.
   - BIG-IP must have a self-IP on the VXLAN tunnel in the pod CIDR range.
   - BIG-IP must have a route to the Kubernetes pod CIDR via the VXLAN tunnel.
   - Note the VXLAN tunnel MAC address (needed for the BIG-IP Node object):
     ```
     tmsh show net tunnels tunnel <tunnel_name> all-properties
     ```

---

## Step 0 -- Install F5 CRDs

Install the F5 Custom Resource Definitions into the cluster. The CRD manifest
version **must match** the CIS controller image version.

```bash
kubectl create -f https://raw.githubusercontent.com/F5Networks/k8s-bigip-ctlr/v2.20.3/docs/config_examples/customResourceDefinitions/customresourcedefinitions.yml
```

Verify:

```bash
kubectl get crd | grep f5
```

Expected CRDs:
- `virtualservers.cis.f5.com`
- `tlsprofiles.cis.f5.com`
- `transportservers.cis.f5.com`
- `externaldnses.cis.f5.com`
- `ingresslinks.cis.f5.com`
- `policies.cis.f5.com`

---

## Step 1 -- Create ServiceAccount

```bash
kubectl apply -f templates/00-cis/01-cis-sa.yaml
```

Creates `bigip-ctlr` ServiceAccount in `kube-system`.

---

## Step 2 -- Create BIG-IP Login Secret

```bash
kubectl apply -f templates/00-cis/02-cis-secret.yaml
```

> **IMPORTANT:** The template contains base64-encoded placeholder credentials
> (`admin` / `admin`). The Agent **MUST** ask the user for actual BIG-IP
> credentials and generate the secret with proper base64 values:
> ```bash
> echo -n '<username>' | base64
> echo -n '<password>' | base64
> ```
>
> Alternatively, create the secret imperatively:
> ```bash
> kubectl create secret generic bigip-login -n kube-system \
>   --from-literal=username=<USERNAME> \
>   --from-literal=password=<PASSWORD>
> ```

---

## Step 3 -- Create RBAC (ClusterRole + ClusterRoleBinding)

```bash
kubectl apply -f templates/00-cis/03-cis-rbac.yaml
```

Grants CIS permissions to watch nodes, services, endpoints, ingresses,
CIS CRDs, IPAM resources, secrets, etc.

---

## Step 4 -- Create IngressClass (optional but recommended)

```bash
kubectl apply -f templates/00-cis/04-cis-ingressclass.yaml
```

Creates three IngressClass resources: `ingclass-cluster`, `ingclass-nodeport`, `ingclass-crd`.

---

## Step 5 -- Create BIG-IP Node (Cluster mode with VXLAN only)

**Required for Cluster mode** when using Flannel or Calico CNI with VXLAN.
Not needed for NodePort mode or when Cilium VTEP is configured.

```bash
kubectl apply -f templates/00-cis/05-cis-node.yaml
```

> The Agent **MUST** customise the Node YAML before applying:
>
> | Field | Description | Example |
> |-------|-------------|---------|
> | `metadata.name` | Unique node name for BIG-IP | `bip202` |
> | `flannel.alpha.coreos.com/public-ip` | BIG-IP VXLAN self-IP facing K8s | `10.82.255.202` |
> | `flannel.alpha.coreos.com/backend-data` | VXLAN tunnel MAC address | `{"VtepMAC":"00:50:56:bd:22:12"}` |
> | `spec.podCIDR` | Pod CIDR routed through BIG-IP's VXLAN | `172.20.202.0/24` |

Verify:

```bash
kubectl get nodes -o wide
```

The BIG-IP should appear as a node (it will show `NotReady` -- this is expected).

---

## Step 6 -- Deploy CIS Controller

Choose the appropriate deployment template:

| Template | Mode | Pool Member Type |
|----------|------|------------------|
| `templates/00-cis/06-cis-crd-cluster.yaml` | CRD | Cluster |
| `templates/00-cis/06-cis-crd-nodeport.yaml` | CRD | NodePort |

```bash
kubectl apply -f templates/00-cis/06-cis-crd-cluster.yaml
```

> The Agent **MUST** customise the deployment YAML before applying. Key args to set:
>
> | Arg | Description | Example |
> |-----|-------------|---------|
> | `--bigip-url` | BIG-IP management IP | `10.82.255.201` |
> | `--bigip-partition` | BIG-IP partition for CIS objects | `wClstr11-kubeCrd` |
> | `--pool-member-type` | `cluster` or `nodeport` | `cluster` |
> | `--flannel-name` | BIG-IP VXLAN tunnel name (Cluster mode) | `/Common/vxlan_wClstr12` |
> | `--custom-resource-mode` | Must be `true` for CRD mode | `true` |
> | `--log-level` | Logging verbosity | `INFO` or `DEBUG` |
> | `--insecure` | Skip TLS verification to BIG-IP | (flag, no value) |
> | `image` | CIS controller image + tag | `f5networks/k8s-bigip-ctlr:2.20.3` |

---

## Step 7 -- Verify CIS is Running

```bash
kubectl --namespace=kube-system get pods -l app=cis-ctlr-deployment
kubectl --namespace=kube-system logs -f deployment/<cis-deployment-name>
```

Look for:
- Pod status: `Running`
- Log line: `"level":"info","msg":"CIS Successfully Initialized"`
- No repeated auth errors or connection refused messages

---

## Template Customisation Rules

When the Agent uses a template, it **MUST**:

1. **Read the template** from `templates/` first.
2. **Copy** it to a working location -- never modify the original template files.
3. **Replace all placeholder values** (marked with comments or angle brackets):
   - BIG-IP IP, partition, VXLAN tunnel name
   - Credentials (base64-encoded)
   - VirtualServer VIP address, hostname, pool/service names
   - BIG-IP Node annotations (IP, MAC, podCIDR)
   - CIS image tag (match the CRD version)
4. **Validate** the YAML with `kubectl apply --dry-run=client -f <file>` before applying.
5. **Apply** and verify.

---

## Worked Example: Calico + VXLAN + Cluster + CRD Mode

This is a tested, working example. The environment:

- **Cluster:** 5 nodes (wawnode111-115), Kubernetes v1.31.6, cri-o
- **CNI:** Calico v3.31.2 via Tigera operator
- **BIG-IP:** `10.82.255.201`, VLAN `VlanKube` (IP `10.82.255.202`), VXLAN tunnel `vxlan_wClstr12` (IP `172.20.202.3/24`, MAC `00:50:56:bd:22:12`)
- **Partition:** `wClstr11-kubeCrd`
- **BGP:** BIG-IP AS 65500, Calico nodes AS 65511
- **Pod CIDR route:** `172.20.32.0/20` via tunnel `vxlan_wClstr12`

Installation order:

```bash
# Step 0: Install CRDs
kubectl create -f https://raw.githubusercontent.com/F5Networks/k8s-bigip-ctlr/v2.20.3/docs/config_examples/customResourceDefinitions/customresourcedefinitions.yml

# Step 1-4: CIS prerequisites
kubectl apply -f templates/00-cis/01-cis-sa.yaml
kubectl apply -f templates/00-cis/02-cis-secret.yaml     # CUSTOMISE credentials
kubectl apply -f templates/00-cis/03-cis-rbac.yaml
kubectl apply -f templates/00-cis/04-cis-ingressclass.yaml

# Step 5: BIG-IP Node (for Cluster mode VXLAN)
kubectl apply -f templates/00-cis/05-cis-node.yaml        # CUSTOMISE node details

# Step 6: Deploy CIS
kubectl apply -f templates/00-cis/06-cis-crd-cluster.yaml # CUSTOMISE args

# Step 7: Verify
kubectl --namespace=kube-system get pods -l app=cis-ctlr-deployment
```

After deploying test services and CRD objects:

```bash
# Test results
curl http://10.171.184.221/coffee -H "Host: cafe.example.com"
# Server address: 172.20.24.66:8080 Server name: coffee-6db967495b-8v9zm ...

curl http://10.171.184.221/tea -H "Host: cafe.example.com"
# Server address: 172.20.24.67:8080 Server name: tea-7b7d6c947d-j6mxr ...

curl -I http://10.171.184.221/ -H "Host: httpbin.example.com"
# HTTP/1.1 200 OK ...
```

---

## Uninstalling CIS

To remove CIS and all its resources:

```bash
# Delete CRD objects first (this removes BIG-IP config)
kubectl delete vs,ts,externaldns --all -A

# Delete CIS deployment and supporting resources (reverse order)
kubectl --namespace=kube-system delete -f templates/00-cis/06-cis-crd-cluster.yaml
kubectl delete -f templates/00-cis/05-cis-node.yaml
kubectl delete -f templates/00-cis/04-cis-ingressclass.yaml
kubectl delete -f templates/00-cis/03-cis-rbac.yaml
kubectl --namespace=kube-system delete -f templates/00-cis/02-cis-secret.yaml
kubectl --namespace=kube-system delete -f templates/00-cis/01-cis-sa.yaml

# Optionally remove CRDs
kubectl delete -f https://raw.githubusercontent.com/F5Networks/k8s-bigip-ctlr/v2.20.3/docs/config_examples/customResourceDefinitions/customresourcedefinitions.yml
```
