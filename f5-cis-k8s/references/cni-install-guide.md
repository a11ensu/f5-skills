# CNI Installation Guide

This document covers installing CNI plugins that are compatible with F5 CIS.
CNI is an **optional prerequisite** — if already installed, skip this entirely.

If CNI is not installed, the **user must specify** which CNI to use.
CNI installation via Helm requires:
1. Helm is installed (`helm version`)
2. The CNI Helm repository has been added

See `references/helm-guide.md` for Helm setup and repo commands.

---

## Detecting Installed CNI

```bash
# Check for running CNI pods
kubectl --namespace=kube-system get pods | grep -iE 'cilium|flannel|calico'

# Check for CNI config files on a node
kubectl get nodes -o wide
```

If CNI pods are running and healthy, CNI is already installed.

---

## Cilium

### Install via Helm

```bash
helm repo add cilium https://helm.cilium.io/
helm repo update

helm install cilium cilium/cilium \
  --version 1.16.5 \
  --namespace kube-system \
  --set operator.replicas=1
```

### Verify

```bash
kubectl --namespace=kube-system get pods -l app.kubernetes.io/part-of=cilium
cilium status   # if cilium CLI is installed
```

### Cilium VTEP Configuration (for CIS Cluster Mode)

When using Cilium with CIS in Cluster mode (VXLAN), Cilium can be configured
with VTEP (Virtual Tunnel Endpoint) integration so that the BIG-IP VXLAN
tunnel endpoint is known to Cilium. This eliminates the need for a fake Node
object.

```bash
helm upgrade cilium cilium/cilium \
  --namespace kube-system \
  --reuse-values \
  --set vtep.enabled=true \
  --set vtep.endpoint="<BIGIP_VTEP_IP>" \
  --set vtep.cidr="<BIGIP_VXLAN_SELFIP_CIDR>" \
  --set vtep.mask="255.255.255.0" \
  --set vtep.mac="<BIGIP_VXLAN_MAC>"
```

---

## Flannel

### Install via Helm

```bash
helm repo add flannel https://flannel-io.github.io/flannel/
helm repo update

helm install flannel flannel/flannel \
  --namespace kube-flannel \
  --create-namespace
```

### Alternative: Install via kubectl

```bash
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```

### Verify

```bash
kubectl --namespace=kube-flannel get pods -l app=flannel
# or
kubectl --namespace=kube-system get pods | grep flannel
```

---

## Calico

### Install via Helm

```bash
helm repo add projectcalico https://docs.tigera.io/calico/charts
helm repo update

helm install calico projectcalico/tigera-operator \
  --version v3.28.0 \
  --namespace tigera-operator \
  --create-namespace
```

### Alternative: Install via kubectl (operator method)

```bash
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/tigera-operator.yaml
kubectl create -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/custom-resources.yaml
```

### Verify

```bash
kubectl get pods -n calico-system
# or
kubectl --namespace=kube-system get pods | grep calico
```

---

## Post-CNI Verification

After installing any CNI, verify that pods can be scheduled and are running:

```bash
kubectl get nodes            # All nodes should be Ready
kubectl get pods -A          # No pods stuck in Pending/ContainerCreating
```

---

## CIS VXLAN Flag Mapping

| CNI | CIS Flag | Notes |
|-----|----------|-------|
| Cilium | `--flannel-name` or `--cilium-name` | `--flannel-name` is the tested approach |
| Flannel | `--flannel-name` | Standard VXLAN integration |
| Calico | `--flannel-name` | When using VXLAN backend mode |

Only **one** VXLAN flag is allowed per CIS deployment.
