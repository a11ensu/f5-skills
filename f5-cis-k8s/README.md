# f5-cis-k8s

Installs and operates F5 BIG-IP Container Ingress Services (CIS) on Kubernetes clusters. Provides templates, CRD examples, and reference documents for deploying CIS, creating VirtualServer/TransportServer/ExternalDNS custom resources, exposing Kubernetes services through BIG-IP, and troubleshooting CIS.

| Field | Value |
|-------|-------|
| **Version** | 3.0.0 |
| **Last Updated** | 2026-03-07 |

## What's Updated (v3.0.0 -- 2026-03-07)

- Added NodePort pool type templates and VirtualServer NodePort variant
- Added BIG-IP Node template for VXLAN overlay (Cluster mode)
- Added Calico (Tigera operator) CNI installation docs
- Added ArgoCD TransportServer example
- Added worked example in CIS installation steps
- Added F5 Helm chart reference documentation
- Expanded CRD field documentation in crd-overview

---

## Developer Guide

This section explains the structure of the `f5-cis-k8s` skill folder,
how each component works, and how to expand the skill with new content.

---

## Folder Structure

```
f5-cis-k8s/
├── SKILL.md                              # Main skill file -- Agent reads this first
├── README.md                             # This file -- developer/maintainer guide
├── references/                           # Detailed reference documents
│   ├── cis-config-parameters.md          # CIS deployment arg/flag reference
│   ├── cis-crd-overview.md              # CRD types, fields, and patterns
│   ├── cis-install-steps.md             # Step-by-step manual CIS installation
│   ├── cni-install-guide.md             # CNI installation (Cilium, Flannel, Calico)
│   ├── crd-examples.md                  # Guide for creating/modifying/deleting CRDs
│   ├── helm-guide.md                    # Helm setup, repos, F5 chart reference
│   ├── testing-services.md              # Creating/managing test pods and services
│   └── troubleshooting.md              # Common issues and diagnostic commands
└── templates/                            # YAML templates (do NOT edit originals)
    ├── 00-cis/                           # CIS installation resources
    │   ├── 01-cis-sa.yaml               # ServiceAccount
    │   ├── 02-cis-secret.yaml           # BIG-IP login secret
    │   ├── 03-cis-rbac.yaml             # ClusterRole + ClusterRoleBinding
    │   ├── 04-cis-ingressclass.yaml     # IngressClass definitions
    │   ├── 05-cis-node.yaml             # BIG-IP Node for VXLAN (Cluster mode)
    │   ├── 06-cis-crd-cluster.yaml      # CIS Deployment (CRD mode, Cluster)
    │   └── 06-cis-crd-nodeport.yaml     # CIS Deployment (CRD mode, NodePort)
    ├── 10-svc/                           # Sample application templates
    │   ├── ns-example.yaml              # Example namespace with crd label
    │   ├── cafe-svc-cluster.yaml        # Cafe demo (coffee + tea) ClusterIP
    │   ├── cafe-svc-nodeport.yaml       # Cafe demo (coffee + tea) NodePort
    │   └── httpbin-svc.yaml             # httpbin demo
    └── 20-crd/                           # CRD example templates
        ├── README.md                    # CRD examples index and numbering guide
        ├── 21-crd-vs-cafe.yaml          # VirtualServer -- cafe (path-based routing)
        ├── 21-crd-vs-httpbin.yaml       # VirtualServer -- httpbin
        ├── 21-crd-vs-nodeport-cafe.yaml # VirtualServer -- cafe (NodePort variant)
        ├── 22-crd-ts-example.yaml       # TransportServer -- L4 TCP generic
        ├── 22-crd-ts-argocd.yaml        # TransportServer -- ArgoCD L4 TCP
        └── 29-crd-externaldns.yaml      # ExternalDNS -- GTM/GSLB example
```

---

## How the Skill Works

The `SKILL.md` file is the entry point. When triggered, the Agent:

1. **Understands** the user's request (install, configure, create CRDs, troubleshoot).
2. **Verifies prerequisites** (Kubernetes UP, kubectl works, CNI status, existing CIS).
3. **Reads the relevant reference file(s)** from `references/` for detailed steps.
4. **Uses templates** from `templates/` as starting points (copies, customises, applies).
5. **Tests the result** via `curl` or shows the user the test command.

The design principle is: **SKILL.md stays concise** and delegates details to
reference files. This keeps the Agent's primary context small and focused.

---

## How to Expand This Skill

### Adding New CRD Examples

1. Create a new YAML file in `templates/20-crd/` following the numbering convention:
   - `21-xx` = VirtualServer examples
   - `22-xx` = TransportServer examples
   - `23-xx` = TLSProfile examples
   - `24-xx` = Policy examples
   - `29-xx` = ExternalDNS examples
   - `100+`  = Advanced, combined, or real-world examples

2. Include clear comments at the top with `CUSTOMISE` markers for placeholder values.

3. Add the label `f5cr: "true"` in metadata.labels.

4. Update `templates/20-crd/README.md` with the new file entry.

5. If the new example introduces a new pattern, add a section to
   `references/crd-examples.md`.

### Adding New Test Applications

1. Create a new YAML file in `templates/10-svc/` with Deployment + Service.

2. Follow the existing naming pattern (e.g. `<appname>-svc.yaml` for ClusterIP,
   `<appname>-svc-nodeport.yaml` for NodePort).

3. Update `references/testing-services.md` with the new template entry.

### Adding New CIS Deployment Variants

CIS supports multiple deployment configurations. Currently covered:

| Template | Mode | Pool Type |
|----------|------|-----------|
| `06-cis-crd-cluster.yaml` | CRD | Cluster |
| `06-cis-crd-nodeport.yaml` | CRD | NodePort |

To add more (e.g. Ingress mode, ConfigMap mode):

1. Create a new YAML file in `templates/00-cis/` with a descriptive name.
   Follow the numbering: `06-cis-<mode>-<pool-type>.yaml`

2. Update `references/cis-install-steps.md` Step 6 table with the new template.

3. If the variant has different prerequisites or flags, document them in the
   template comments and reference files.

### Adding New Reference Documents

1. Create a new `.md` file in `references/`.

2. Add the file to the **Key Paths** table in `SKILL.md`.

3. If the reference is needed during a specific agent workflow step,
   add a link in the **Step 3** action table in `SKILL.md`.

### Adding Support for New CNIs

1. Add the installation steps to `references/cni-install-guide.md`.

2. Add the Helm repo to `references/helm-guide.md`.

3. Update the CIS VXLAN Flag Mapping table in `references/cni-install-guide.md`.

### Adding Helm-Based CIS Installation

1. Create `references/cis-install-helm.md` with the Helm-based install procedure.

2. Add it to the **Key Paths** table in `SKILL.md`.

3. Update the Scope table in `SKILL.md` to reflect Helm support.

4. The F5 Helm chart reference is already documented in `references/helm-guide.md`
   and a local copy of the chart exists in `local/f5-cis-k8s-docs/f5-chart/`.

### Adding OpenShift Support

This would be a separate skill (`f5-cis-openshift`). The directory already
exists at the repository root level.

---

## Design Principles

- **SKILL.md is the entry point** -- keep it concise (under 5000 words).
  Move detailed steps, procedures, and examples into `references/` files.
- **Templates are read-only** -- the Agent copies and customises them, never
  edits the originals in `templates/`.
- **References are self-contained** -- each reference file should be usable
  on its own without requiring the reader to jump to other files (though
  cross-references are fine for optional deeper context).
- **Numbering conventions** in `templates/` keep things organised as the
  skill grows. Follow the established ranges.
- **Progressive disclosure** -- the Agent reads SKILL.md first (level 1),
  then reads specific reference files as needed (level 2), then reads
  templates when applying changes (level 3).

---

## File Inventory

### Templates (YAML)

| Directory | File | Description |
|-----------|------|-------------|
| `00-cis/` | `01-cis-sa.yaml` | ServiceAccount for CIS controller |
| `00-cis/` | `02-cis-secret.yaml` | BIG-IP credentials Secret |
| `00-cis/` | `03-cis-rbac.yaml` | ClusterRole + ClusterRoleBinding |
| `00-cis/` | `04-cis-ingressclass.yaml` | IngressClass definitions (3 classes) |
| `00-cis/` | `05-cis-node.yaml` | BIG-IP Node for VXLAN overlay |
| `00-cis/` | `06-cis-crd-cluster.yaml` | CIS Deployment -- CRD mode, Cluster pool |
| `00-cis/` | `06-cis-crd-nodeport.yaml` | CIS Deployment -- CRD mode, NodePort pool |
| `10-svc/` | `ns-example.yaml` | Example namespace with `type: crd` label |
| `10-svc/` | `cafe-svc-cluster.yaml` | Cafe app (coffee + tea) ClusterIP |
| `10-svc/` | `cafe-svc-nodeport.yaml` | Cafe app (coffee + tea) NodePort |
| `10-svc/` | `httpbin-svc.yaml` | httpbin HTTP testing service |
| `20-crd/` | `21-crd-vs-cafe.yaml` | VirtualServer for cafe app |
| `20-crd/` | `21-crd-vs-httpbin.yaml` | VirtualServer for httpbin |
| `20-crd/` | `21-crd-vs-nodeport-cafe.yaml` | VirtualServer for cafe (NodePort) |
| `20-crd/` | `22-crd-ts-example.yaml` | TransportServer generic TCP |
| `20-crd/` | `22-crd-ts-argocd.yaml` | TransportServer for ArgoCD |
| `20-crd/` | `29-crd-externaldns.yaml` | ExternalDNS for GTM/GSLB |

### References (Markdown)

| File | Description |
|------|-------------|
| `cis-install-steps.md` | Step-by-step manual CIS installation with worked example |
| `cis-config-parameters.md` | All CIS deployment CLI flags and Helm chart defaults |
| `cis-crd-overview.md` | CRD types (VS, TS, TLS, ExternalDNS, Policy, IngressLink) |
| `crd-examples.md` | Creating, modifying, deleting CRD objects |
| `cni-install-guide.md` | CNI installation (Cilium, Flannel, Calico via Tigera) |
| `helm-guide.md` | Helm setup, repos, F5 chart reference |
| `testing-services.md` | Test apps (cafe, httpbin) and curl testing |
| `troubleshooting.md` | Common issues table and diagnostic workflow |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-03-05 | Initial release -- CRD mode, Cluster pool type |
| 3.0.0 | 2026-03-07 | Added NodePort templates, BIG-IP Node template, Calico Tigera operator docs, ArgoCD TransportServer, worked example in install-steps, F5 Helm chart reference, expanded CRD field docs |
