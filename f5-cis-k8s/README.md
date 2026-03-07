# f5-cis-k8s Skill — Developer Guide

This document explains the structure of the `f5-cis-k8s` skill folder,
how each component works, and how to expand the skill with new content.

---

## Folder Structure

```
f5-cis-k8s/
├── SKILL.md                          # Main skill file — Agent reads this first
├── README.md                         # This file — developer/maintainer guide
├── references/                       # Detailed reference documents
│   ├── cis-config-parameters.md      # CIS deployment arg/flag reference
│   ├── cis-crd-overview.md           # CRD types, fields, and patterns
│   ├── cis-install-steps.md          # Step-by-step manual CIS installation
│   ├── cni-install-guide.md          # CNI installation (Cilium, Flannel, Calico)
│   ├── crd-examples.md              # Guide for creating/modifying/deleting CRDs
│   ├── helm-guide.md                # Helm setup, repos, and common operations
│   ├── testing-services.md          # Creating/managing test pods and services
│   └── troubleshooting.md           # Common issues and diagnostic commands
└── templates/                        # YAML templates (do NOT edit originals)
    ├── 00-cis/                       # CIS installation resources
    │   ├── 01-cis-sa.yaml            # ServiceAccount
    │   ├── 02-cis-secret.yaml        # BIG-IP login secret
    │   ├── 03-cis-rbac.yaml          # ClusterRole + ClusterRoleBinding
    │   ├── 04-cis-ingressclass.yaml  # IngressClass definitions
    │   └── 06-cis-crd-cluster.yaml   # CIS Deployment (CRD mode, Cluster)
    ├── 10-svc/                       # Sample application templates
    │   ├── ns-example.yaml           # Example namespace
    │   ├── cafe-svc-cluster.yaml     # Cafe demo (coffee + tea)
    │   └── httpbin-svc.yaml          # httpbin demo
    └── 20-crd/                       # CRD example templates
        ├── README.md                 # CRD examples index and numbering guide
        ├── 21-crd-vs-cafe.yaml       # VirtualServer — cafe (path-based routing)
        ├── 21-crd-vs-httpbin.yaml    # VirtualServer — httpbin
        ├── 22-crd-ts-example.yaml    # TransportServer — L4 TCP example
        └── 29-crd-externaldns.yaml   # ExternalDNS — GTM/GSLB example
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
   - `100+`  = Advanced or combined examples

2. Include clear comments at the top with `CUSTOMISE` markers for placeholder values.

3. Add the label `f5cr: "true"` in metadata.labels.

4. Update `templates/20-crd/README.md` with the new file entry.

5. If the new example introduces a new pattern, add a section to
   `references/crd-examples.md`.

### Adding New Test Applications

1. Create a new YAML file in `templates/10-svc/` with Deployment + Service.

2. Follow the existing naming pattern (e.g. `<appname>-svc.yaml`).

3. Update `references/testing-services.md` with the new template entry.

### Adding New CIS Deployment Variants

1. Create a new YAML file in `templates/00-cis/` with a descriptive name.
   Follow the numbering: `06-cis-<mode>-<pool-type>.yaml`
   (e.g. `07-cis-crd-nodeport.yaml`).

2. Update `references/cis-install-steps.md` Step 5 table with the new template.

3. If the variant has different prerequisites or flags, document them.

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

### Adding OpenShift Support

1. This would likely be a separate skill (`f5-cis-openshift`) or a major
   version update.

2. If extending this skill, add OpenShift-specific references and templates
   in clearly separated directories (e.g. `templates/00-cis-ocp/`).

3. Update the Scope table in `SKILL.md`.

---

## Design Principles

- **SKILL.md is the entry point** — keep it concise. Move detailed steps,
  procedures, and examples into `references/` files.
- **Templates are read-only** — the Agent copies and customises them, never
  edits the originals in `templates/`.
- **References are self-contained** — each reference file should be usable
  on its own without requiring the reader to jump to other files (though
  cross-references are fine for optional deeper context).
- **Numbering conventions** in `templates/` keep things organised as the
  skill grows. Follow the established ranges.
