---
name: f5-cis-k8s
description: >
  Installs and operates F5 BIG-IP Container Ingress Services (CIS) on Kubernetes
  clusters. Use when the user asks to deploy CIS, create VirtualServer /
  TransportServer / ExternalDNS custom resources, expose Kubernetes services
  through BIG-IP, troubleshoot CIS, or manage CIS-related Kubernetes objects.
  Trigger phrases: "install CIS", "deploy CIS on Kubernetes", "expose service
  via BIG-IP", "create VirtualServer CR", "F5 CIS CRD", "BIG-IP container
  ingress", "troubleshoot CIS".
license: Apache-2.0
metadata:
  author: Allen Su
  version: 3.0.0
  category: F5
  tags: [F5, BIG-IP, CIS, Kubernetes, k8s-bigip-ctlr, CRD]
---

# F5 BIG-IP CIS on Kubernetes Skill

## Role

You are an expert F5 & Kubernetes Network Engineer. Your goal is to help the
user install, operate, and troubleshoot **F5 BIG-IP Container Ingress Services
(CIS)** on a Kubernetes cluster.

- This skill targets **Kubernetes only** (not OpenShift).
- Always use `kubectl` or `kubectl --namespace=kube-system` (never shell aliases like `k` or `ks`).
- CIS communicates with BIG-IP via its REST API (AS3). No SSH to BIG-IP.
- Official docs: https://clouddocs.f5.com/containers/latest/

---

## Scope

| Dimension | Supported |
|-----------|-----------|
| Platform | Kubernetes (not OpenShift) |
| Install method | Manual step-by-step |
| CIS mode | CRD (`--custom-resource-mode=true`) |
| Pool member type | Cluster and NodePort |
| Overlay | VXLAN |
| CNI | Cilium, Flannel, Calico |
| CIS image | `f5networks/k8s-bigip-ctlr:2.20.3` |

---

## Key Paths

> All paths are relative to the skill root: `f5-cis-k8s/`

| Name | Path | Purpose |
|------|------|---------|
| CIS install steps | `references/cis-install-steps.md` | Step-by-step manual CIS installation |
| CIS config parameters | `references/cis-config-parameters.md` | All CIS deployment arg/flag reference |
| CRD types overview | `references/cis-crd-overview.md` | CRD kinds, fields, common patterns |
| CRD examples guide | `references/crd-examples.md` | Creating, modifying, deleting CRD objects |
| CNI install guide | `references/cni-install-guide.md` | CNI installation (Cilium, Flannel, Calico) |
| Helm guide | `references/helm-guide.md` | Helm setup, repos, F5 chart reference |
| Testing services | `references/testing-services.md` | Creating/managing test pods and services |
| Troubleshooting | `references/troubleshooting.md` | Common issues and diagnostic commands |
| CIS templates | `templates/00-cis/` | CIS installation YAML templates |
| Sample app templates | `templates/10-svc/` | Test application Deployment + Service |
| CRD example templates | `templates/20-crd/` | F5 CRD YAML examples |

---

## Architecture

```
                        +----------------------------+
                        |        F5 BIG-IP           |
                        |  +----------------------+  |
  Client Request ------>|  |  Virtual Server      |  |
                        |  |  (auto-created by CIS)|  |
                        |  +----------+-----------+  |
                        |             | VXLAN tunnel  |
                        +-------------+--------------+
                                      |
                        +-------------+--------------+
                        | K8s Cluster                |
                        |             v              |
                        |  +------------------+      |
                        |  | CIS Pod          |      |
                        |  | (kube-system)    |      |
                        |  +--------+---------+      |
                        |           | watches CRDs   |
                        |           v                |
                        |  +------------------+      |
                        |  | App Pods (any NS)|      |
                        |  +------------------+      |
                        +----------------------------+
```

CIS watches the Kubernetes API for CRD objects (VirtualServer, TransportServer,
ExternalDNS, etc.) and programs the corresponding configuration on BIG-IP
via its REST API (AS3).

---

## Agent Workflow

The Agent MUST follow these steps in order:

### Step 1 -- Understand the User Request

Identify what the user needs:
- Install or troubleshoot CIS
- Change CIS deployment configuration
- Create, delete, or modify test pods/services
- Create, delete, or modify CIS objects (F5 CRDs, ConfigMap, Ingress)

### Step 2 -- Verify Prerequisites and Current Status

**MUST-HAVE (always check first):**

a. **Remote Kubernetes is UP:**
```bash
kubectl get nodes -o wide
```
If nodes are not Ready, stop and inform the user.

b. **kubectl works and can reach the cluster:**
```bash
kubectl cluster-info
```

**OPTIONAL (check when relevant):**

a. **CNI status:**
```bash
kubectl get pods -A | grep -iE 'cilium|flannel|calico'
```
If CNI is **not installed**, the user must specify which CNI to use.
CNI installation requires Helm and the CNI repo to be added.
See `references/cni-install-guide.md` and `references/helm-guide.md`.

b. **BIG-IP status:** (TO-DO later)

c. **Existing CIS installation:**
```bash
kubectl --namespace=kube-system get pods -l app=cis-ctlr-deployment
kubectl get crd | grep f5
```

### Step 3 -- Decide Next Step Based on the Request

The scope of actions is limited to:

| Action | Reference |
|--------|-----------|
| **a. Troubleshoot / complete CIS installation** | `references/cis-install-steps.md`, `references/troubleshooting.md` |
| **b. Change CIS deployment configuration** | `references/cis-config-parameters.md`, `templates/00-cis/` |
| **c. Create, delete, or modify test pods/services** | `references/testing-services.md`, `templates/10-svc/` |
| **d. Create, delete, or modify CIS objects** (F5 CRDs) | `references/crd-examples.md`, `references/cis-crd-overview.md`, `templates/20-crd/` |

Read the relevant reference file(s) before proceeding.

### Step 4 -- Test the Result

After making changes, verify with `curl`:

```bash
# L7 HTTP
curl http://<VIP>/<path> -H "Host: <hostname>"

# L4 TCP
curl -v telnet://<VIP>:<port>
```

**If the Agent has no connectivity to the virtual server**, show the user the
curl command to run from a machine that does have access.

---

## Quick Reference

### CIS Modes (mutually exclusive)

| Mode | Flag | What CIS Watches |
|------|------|------------------|
| CRD | `--custom-resource-mode=true` | VirtualServer, TransportServer, ExternalDNS, TLSProfile, Policy |
| Ingress / ConfigMap | (default, no flag) | Kubernetes Ingress, ConfigMap with AS3 |

### Pool Member Types

| Type | Flag | How Pool Members are Built |
|------|------|----------------------------|
| Cluster | `--pool-member-type=cluster` | Pod IPs (requires VXLAN or BGP overlay) |
| NodePort | `--pool-member-type=nodeport` | Node IPs + NodePort (no overlay needed) |

### Essential CIS Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--bigip-url` | Yes | BIG-IP management IP or URL |
| `--bigip-partition` | Yes | BIG-IP partition for CIS objects |
| `--custom-resource-mode` | No | Set `true` for CRD mode |
| `--pool-member-type` | No | `cluster` or `nodeport` (default: nodeport) |
| `--flannel-name` | No | BIG-IP VXLAN tunnel name (Cluster mode with Flannel/Cilium/Calico) |
| `--log-level` | No | `INFO`, `DEBUG`, `AS3DEBUG` |
| `--insecure` | No | Skip TLS cert verification to BIG-IP |

Full parameter list: `references/cis-config-parameters.md`

## Important

- CIS deployment MUST have `replicas: 1` -- do NOT increase.
- The `--bigip-partition` value becomes the AS3 tenant name on BIG-IP.
- CRD version must match the CIS controller image version.
- Always use label `f5cr: "true"` on CRD objects for CIS to watch them.
- Templates are read-only: copy, customise, then apply.
