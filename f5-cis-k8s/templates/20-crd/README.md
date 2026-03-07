# F5 CIS CRD Examples Index

This directory contains example Custom Resource definitions for F5 CIS.
Apply these in the application namespace after CIS is running.

## Numbering Convention

| Range | Category | Description |
|-------|----------|-------------|
| 21-xx | VirtualServer | L7 HTTP/HTTPS virtual servers with host/path routing |
| 22-xx | TransportServer | L4 TCP/UDP transport servers |
| 29-xx | ExternalDNS | GSLB / GTM wide-IP records |
| 100+ | *(reserved)* | Additional advanced examples |

## Current Examples

### VirtualServer (21-xx)

| File | Description |
|------|-------------|
| `21-crd-vs-cafe.yaml` | HTTP VirtualServer with path-based routing (/coffee, /tea) using hostGroup for shared VIP |
| `21-crd-vs-httpbin.yaml` | HTTP VirtualServer for httpbin service using hostGroup for shared VIP |

### TransportServer (22-xx)

| File | Description |
|------|-------------|
| `22-crd-ts-example.yaml` | L4 TCP TransportServer example (e.g. for ArgoCD or similar TCP service) |

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
