# CRD Examples Reference

This document covers creating, modifying, and deleting F5 CIS Custom Resource
objects (VirtualServer, TransportServer, ExternalDNS, etc.).

For CRD field definitions and types, see `references/cis-crd-overview.md`.

---

## Available Templates

| Template | Type | Description |
|----------|------|-------------|
| `templates/20-crd/21-crd-vs-cafe.yaml` | VirtualServer | L7 HTTP with path-based routing (/coffee, /tea), hostGroup |
| `templates/20-crd/21-crd-vs-httpbin.yaml` | VirtualServer | L7 HTTP for httpbin, shared VIP via hostGroup |
| `templates/20-crd/21-crd-vs-nodeport-cafe.yaml` | VirtualServer | L7 HTTP cafe for NodePort mode |
| `templates/20-crd/22-crd-ts-example.yaml` | TransportServer | L4 TCP generic example |
| `templates/20-crd/22-crd-ts-argocd.yaml` | TransportServer | L4 TCP for ArgoCD (port 443) |
| `templates/20-crd/29-crd-externaldns.yaml` | ExternalDNS | GTM/GSLB wide-IP |

See `templates/20-crd/README.md` for the full index and numbering convention.

---

## Creating CRD Objects

### Workflow

1. Identify the CRD type needed (VirtualServer, TransportServer, ExternalDNS).
2. Read the appropriate template from `templates/20-crd/`.
3. Customise: host, virtualServerAddress (VIP), pools, paths, service names/ports.
4. Ensure the label `f5cr: "true"` is present (required for CIS to watch it).
5. Apply to the correct namespace.
6. Verify via CIS logs or `curl`.

### VirtualServer (L7 HTTP)

```bash
# Apply
kubectl -n <namespace> apply -f templates/20-crd/21-crd-vs-cafe.yaml

# Verify
kubectl -n <namespace> get vs
kubectl --namespace=kube-system logs deployment/<cis-deployment> | tail -20
```

Key fields to customise:

| Field | Description | Example |
|-------|-------------|---------|
| `spec.host` | Hostname for routing | `cafe.example.com` |
| `spec.virtualServerAddress` | BIG-IP VIP | `10.171.184.221` |
| `spec.hostGroup` | Share VIP across multiple VS CRs | `cafe` |
| `spec.pools[].path` | URL path to match | `/coffee` |
| `spec.pools[].service` | K8s Service name | `coffee-svc` |
| `spec.pools[].servicePort` | Service port | `80` |

### TransportServer (L4 TCP/UDP)

```bash
kubectl -n <namespace> apply -f templates/20-crd/22-crd-ts-example.yaml

kubectl -n <namespace> get ts
```

Key fields to customise:

| Field | Description | Example |
|-------|-------------|---------|
| `spec.virtualServerAddress` | BIG-IP VIP | `10.171.184.221` |
| `spec.virtualServerPort` | Listening port | `443` |
| `spec.virtualServerName` | VS name on BIG-IP | `vs-argocd` |
| `spec.pool.service` | K8s Service name | `argo-cd-argocd-server` |
| `spec.pool.servicePort` | Service port | `443` |
| `spec.type` | Protocol: `tcp` or `udp` | `tcp` |

### ExternalDNS (GTM/GSLB)

```bash
kubectl -n <namespace> apply -f templates/20-crd/29-crd-externaldns.yaml

kubectl -n <namespace> get externaldns
```

> Requires GTM parameters in CIS deployment: `--gtm-bigip-url`, `--gtm-bigip-username`, `--gtm-bigip-password`.

---

## Modifying CRD Objects

Edit the YAML and re-apply, or use `kubectl edit`:

```bash
# Edit in-place
kubectl -n <namespace> edit vs <name>

# Or modify the file and re-apply
kubectl -n <namespace> apply -f <modified-file>.yaml
```

Common modifications:
- Change VIP address (`spec.virtualServerAddress`)
- Add/remove pools or paths
- Change host-based routing (`spec.host`)
- Add health monitors to pools (`spec.pools[].monitor`)
- Add TLS termination (`spec.tlsProfileName`)
- Attach a Policy CR (`spec.policyName`)

---

## Deleting CRD Objects

```bash
# Delete specific CR
kubectl -n <namespace> delete vs <name>
kubectl -n <namespace> delete ts <name>
kubectl -n <namespace> delete externaldns <name>

# Delete by file
kubectl -n <namespace> delete -f templates/20-crd/21-crd-vs-cafe.yaml

# Delete all CRDs in all namespaces
kubectl delete vs,ts,externaldns --all -A
```

> Deleting a CRD object causes CIS to **remove** the corresponding configuration
> from BIG-IP (Virtual Server, pools, etc.).

---

## Verifying on BIG-IP

After applying a CRD object, CIS creates:
- A Virtual Server in the configured partition on BIG-IP
- Pool(s) with pod IPs (Cluster mode) or node IPs (NodePort mode)
- ARP and route entries (if `serviceAddress` with `arpEnabled: true` is set)

Check CIS logs for confirmation:

```bash
kubectl --namespace=kube-system logs deployment/<cis-deployment> --tail=50
```

Look for:
- `"msg":"Posting declaration"` -- CIS is sending config to BIG-IP
- `"msg":"AS3 response status code: 200"` -- BIG-IP accepted the config
- No `422` or `500` errors

---

## Common Patterns

### Shared VIP (hostGroup)

Multiple VirtualServer CRs can share the same VIP:

```yaml
# VS 1
spec:
  host: app1.example.com
  hostGroup: "shared-vip"
  virtualServerAddress: "10.171.184.221"

# VS 2
spec:
  host: app2.example.com
  hostGroup: "shared-vip"
  virtualServerAddress: "10.171.184.221"
```

### serviceAddress (ARP + Route Advertisement)

Enable BIG-IP to respond to ARP for the VIP:

```yaml
serviceAddress:
  - icmpEcho: "enable"
    arpEnabled: true
    routeAdvertisement: "all"
```

### Health Monitor

Add a health monitor to a pool:

```yaml
pools:
  - path: /coffee
    service: coffee-svc
    servicePort: 80
    monitor:
      type: http
      send: "GET /health HTTP/1.1\r\nHost: \r\n\r\n"
      recv: ""
      interval: 10
      timeout: 31
```
