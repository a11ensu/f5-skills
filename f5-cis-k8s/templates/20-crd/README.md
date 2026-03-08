# F5 CIS CRD Examples Index

This directory contains example Custom Resource definitions for F5 CIS.
Apply these in the application namespace after CIS is running.

## Numbering Convention

| Range | Category | Description |
|-------|----------|-------------|
| 21-xx | VirtualServer | L7 HTTP/HTTPS virtual servers with host/path routing |
| 22-xx | TransportServer | L4 TCP/UDP transport servers |
| 23-xx | TLSProfile | TLS termination configurations *(reserved)* |
| 24-xx | Policy | WAF, iRules, profiles *(reserved)* |
| 29-xx | ExternalDNS | GSLB / GTM wide-IP records |
| 100+ | *(reserved)* | Advanced, combined, or real-world examples |

## Current Examples

### VirtualServer (21-xx)

| File | Description |
|------|-------------|
| `21-crd-vs-cafe.yaml` | HTTP VirtualServer with path-based routing (/coffee, /tea) using hostGroup for shared VIP |
| `21-crd-vs-httpbin.yaml` | HTTP VirtualServer for httpbin service using hostGroup for shared VIP |
| `21-crd-vs-nodeport-cafe.yaml` | HTTP VirtualServer for cafe app (NodePort mode variant) |

### TransportServer (22-xx)

| File | Description |
|------|-------------|
| `22-crd-ts-example.yaml` | L4 TCP TransportServer generic example |
| `22-crd-ts-argocd.yaml` | L4 TCP TransportServer for ArgoCD (port 443) |

### ExternalDNS (29-xx)

| File | Description |
|------|-------------|
| `29-crd-externaldns.yaml` | ExternalDNS example for GTM/GSLB wide-IP configuration |

## Usage

```bash
# Apply a VirtualServer CR to a namespace
kubectl -n <namespace> apply -f 21-crd-vs-cafe.yaml

# Check status
kubectl -n <namespace> get vs

# Delete
kubectl -n <namespace> delete -f 21-crd-vs-cafe.yaml
```

## CUSTOMISE Before Applying

All templates contain placeholder values that MUST be customised:

- `virtualServerAddress`: The BIG-IP VIP address
- `host`: The hostname for host-based routing
- `service` / `servicePort`: Must match actual Kubernetes Service names and ports
- `hostGroup`: Use the same value across VirtualServers that share a VIP

## Adding New Examples

1. Follow the numbering convention above.
2. Use numbers 100+ for advanced or combined examples.
3. Include clear comments with `CUSTOMISE` markers.
4. Add the label `f5cr: "true"` in `metadata.labels`.
5. Update this README with the new file entry.
