# Helm Guide for F5 CIS

This document covers Helm-based operations relevant to the CIS skill,
including CNI installation via Helm and future Helm-based CIS installation.

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

### F5 CIS (for future Helm-based CIS install)

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
```

---

## Notes

- The Agent should verify `helm version` works before attempting any Helm operations.
- If the user specifies a CNI that requires Helm and the repo is not added, the
  Agent should add the repo first.
- Helm-based CIS installation is not yet covered in this skill version but the
  F5 Helm chart repo is listed above for future use.
