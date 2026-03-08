# Helm Guide for F5 CIS

This document covers Helm-based operations relevant to the CIS skill,
including CNI installation via Helm and the F5 CIS Helm chart reference.

---

## Prerequisites

Helm 3.x must be installed and available on the system.

```bash
# Verify Helm is installed
helm version
```

If Helm is not installed:

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

---

## Adding Helm Repositories

### Cilium

```bash
helm repo add cilium https://helm.cilium.io/
helm repo update
```

### Flannel

```bash
helm repo add flannel https://flannel-io.github.io/flannel/
helm repo update
```

### Calico (Tigera)

```bash
helm repo add projectcalico https://docs.tigera.io/calico/charts
helm repo update
```

### F5 CIS

```bash
helm repo add f5-stable https://f5networks.github.io/charts/stable
helm repo update
```

---

## Verifying Repo is Added

```bash
helm repo list
helm search repo <repo-name>
```

---

## Common Helm Operations

```bash
# List installed releases
helm list -A

# Install a chart
helm install <release-name> <chart> -n <namespace> --create-namespace -f values.yaml

# Upgrade a release
helm upgrade <release-name> <chart> -n <namespace> -f values.yaml

# Uninstall a release
helm uninstall <release-name> -n <namespace>

# Show chart default values
helm show values <chart>

# Pull a chart locally for inspection
helm pull <chart>
# or with untar
helm pull <chart> --untar
```

---

## F5 CIS Helm Chart Reference

The official F5 CIS Helm chart is available at:

```bash
helm repo add f5-stable https://f5networks.github.io/charts/stable
helm pull f5-stable/f5-bigip-ctlr
```

A local copy of the chart (v0.0.36) is available in `local/f5-cis-k8s-docs/f5-chart/`
for reference. Key files:

| File | Description |
|------|-------------|
| `Chart.yaml` | Chart metadata (name: `f5-bigip-ctlr`, version: `0.0.36`) |
| `values.yaml` | Default values and all configurable parameters |
| `templates/f5-bigip-ctlr-deploy.yaml` | CIS Deployment template |
| `templates/f5-bigip-ctlr-clusterrole.yaml` | ClusterRole template |
| `templates/f5-bigip-ctlr-serviceaccount.yaml` | ServiceAccount template |
| `templates/f5-bigip-ctlr-secrets.yaml` | BIG-IP credentials Secret template |
| `templates/f5-bigip-ctlr-ingress-class.yaml` | IngressClass template |
| `crds/f5-bigip-ctlr-customresourcedefinitions.yml` | CRD definitions |

### Key Helm Values

| Value | Default | Description |
|-------|---------|-------------|
| `args.bigip_url` | (required) | BIG-IP management IP |
| `args.bigip_partition` | `f5-bigip-ctlr` | BIG-IP partition |
| `bigip_login_secret` | `f5-bigip-ctlr-login` | Name of existing credentials Secret |
| `bigip_secret.create` | `false` | Create Secret via Helm |
| `namespace` | `kube-system` | Deployment namespace |
| `image.user` | `f5networks` | Container image registry user |
| `image.repo` | `k8s-bigip-ctlr` | Container image name |
| `version` | `latest` | Container image tag |
| `rbac.create` | `true` | Create RBAC resources |
| `rbac.namespaced` | `false` | Use per-namespace Roles instead of ClusterRole |
| `serviceAccount.create` | `true` | Create ServiceAccount |
| `ingressClass.create` | `true` | Create IngressClass |
| `ingressClass.ingressClassName` | `f5` | IngressClass name |

> **Note:** Helm values use `_` instead of `-` (e.g. `bigip_url` maps to `--bigip-url`).
> This skill focuses on **manual installation**. The Helm chart is documented here
> as a reference for understanding parameters and defaults.

---

## Notes

- The Agent should verify `helm version` works before attempting any Helm operations.
- If the user specifies a CNI that requires Helm and the repo is not added, the
  Agent should add the repo first.
- Helm-based CIS installation is not the primary method in this skill version but
  the F5 Helm chart is documented above for reference.
