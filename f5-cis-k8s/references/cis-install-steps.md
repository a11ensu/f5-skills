# CIS Manual Installation Steps

This document contains the detailed step-by-step procedure for installing
F5 BIG-IP Container Ingress Services (CIS) on Kubernetes using the manual method.

The Agent should follow these steps in order when performing a CIS installation.

---

## Step 0 — Install F5 CRDs

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

## Step 1 — Create ServiceAccount

```bash
kubectl apply -f templates/00-cis/01-cis-sa.yaml
```

Creates `bigip-ctlr` ServiceAccount in `kube-system`.

---

## Step 2 — Create BIG-IP Login Secret

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

---

## Step 3 — Create RBAC (ClusterRole + ClusterRoleBinding)

```bash
kubectl apply -f templates/00-cis/03-cis-rbac.yaml
```

Grants CIS permissions to watch nodes, services, endpoints, ingresses, CRDs, secrets, etc.

---

## Step 4 — Create IngressClass (optional but recommended)

```bash
kubectl apply -f templates/00-cis/04-cis-ingressclass.yaml
```

---

## Step 5 — Deploy CIS Controller

Choose the appropriate deployment template:

| Template | Mode | Pool Member Type |
|----------|------|------------------|
| `templates/00-cis/06-cis-crd-cluster.yaml` | CRD | Cluster |

```bash
kubectl apply -f templates/00-cis/06-cis-crd-cluster.yaml
```

> The Agent **MUST** customise the deployment YAML before applying. Key args to set:
>
> | Arg | Description | Example |
> |-----|-------------|---------|
> | `--bigip-url` | BIG-IP management IP | `10.82.255.202` |
> | `--bigip-partition` | BIG-IP partition for CIS objects | `kubeCrd-wClstr12` |
> | `--pool-member-type` | `cluster` or `nodeport` | `cluster` |
> | `--flannel-name` | BIG-IP VXLAN tunnel name (Cluster mode) | `/Common/vxlan_wClstr12` |
> | `--custom-resource-mode` | Must be `true` for CRD mode | `true` |
> | `--log-level` | Logging verbosity | `INFO` or `DEBUG` |
> | `--insecure` | Skip TLS verification to BIG-IP | (flag, no value) |
> | `image` | CIS controller image + tag | `f5networks/k8s-bigip-ctlr:2.20.3` |

---

## Step 6 — Verify CIS is Running

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
2. **Copy** it to a working location — never modify the original template files.
3. **Replace all placeholder values** (marked with comments or example data):
   - BIG-IP IP, partition, VXLAN tunnel name
   - Credentials (base64-encoded)
   - VirtualServer VIP address, hostname, pool/service names
   - CIS image tag (match the CRD version)
4. **Validate** the YAML with `kubectl apply --dry-run=client -f <file>` before applying.
5. **Apply** and verify.

---

## Uninstalling CIS

To remove CIS and all its resources:

```bash
# Delete CRD objects first (this removes BIG-IP config)
kubectl delete vs,ts,externaldns --all -A

# Delete CIS deployment and supporting resources
kubectl --namespace=kube-system delete -f templates/00-cis/06-cis-crd-cluster.yaml
kubectl --namespace=kube-system delete -f templates/00-cis/04-cis-ingressclass.yaml
kubectl --namespace=kube-system delete -f templates/00-cis/03-cis-rbac.yaml
kubectl --namespace=kube-system delete -f templates/00-cis/02-cis-secret.yaml
kubectl --namespace=kube-system delete -f templates/00-cis/01-cis-sa.yaml

# Optionally remove CRDs
kubectl delete -f https://raw.githubusercontent.com/F5Networks/k8s-bigip-ctlr/v2.20.3/docs/config_examples/customResourceDefinitions/customresourcedefinitions.yml
```
