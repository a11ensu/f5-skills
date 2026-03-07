# F5 CIS Custom Resource Definitions (CRDs) Overview

Source: https://clouddocs.f5.com/containers/latest/userguide/crd/index.html

CIS CRD mode (`--custom-resource-mode=true`) watches the following custom resource types
and programs corresponding objects on BIG-IP via AS3.

---

## CRD Types

### VirtualServer (`vs`)

- **API:** `cis.f5.com/v1`
- **Kind:** `VirtualServer`
- **Scope:** Namespaced
- **Purpose:** L7 HTTP/HTTPS load balancing with host-based and path-based routing.

Key fields:
| Field | Type | Description |
|-------|------|-------------|
| `spec.host` | String | Hostname for host-based routing (e.g. `cafe.example.com`) |
| `spec.hostGroup` | String | Group multiple VirtualServers onto the same VIP |
| `spec.virtualServerAddress` | String | BIG-IP VIP address |
| `spec.virtualServerHTTPPort` | Integer | Custom HTTP port (default 80) |
| `spec.virtualServerHTTPSPort` | Integer | Custom HTTPS port (default 443) |
| `spec.httpTraffic` | String | `allow`, `none`, or `redirect` |
| `spec.snat` | String | SNAT pool name or `auto` |
| `spec.pools` | Array | List of pool definitions |
| `spec.pools[].path` | String | URL path to match |
| `spec.pools[].service` | String | Kubernetes Service name |
| `spec.pools[].servicePort` | Integer | Service port |
| `spec.pools[].monitor` | Object | Health monitor for this pool |
| `spec.tlsProfileName` | String | Reference to a TLSProfile CR |
| `spec.policyName` | String | Reference to a Policy CR |
| `spec.serviceAddress` | Array | Service address settings (ARP, ICMP, route advertisement) |
| `spec.partition` | String | Override default partition |

Labels:
- CIS watches CRs with label `f5cr: "true"` by default (configurable via `--custom-resource-label`).

---

### TLSProfile

- **API:** `cis.f5.com/v1`
- **Kind:** `TLSProfile`
- **Scope:** Namespaced
- **Purpose:** TLS termination configuration for VirtualServer CRs.

Key fields:
| Field | Type | Description |
|-------|------|-------------|
| `spec.tls.termination` | String | `edge`, `reencrypt`, or `passthrough` |
| `spec.tls.clientSSL` | String | BIG-IP client SSL profile path |
| `spec.tls.serverSSL` | String | BIG-IP server SSL profile path |
| `spec.tls.reference` | String | `bigip` (use existing profile) or `secret` (use K8s secret) |

---

### TransportServer (`ts`)

- **API:** `cis.f5.com/v1`
- **Kind:** `TransportServer`
- **Scope:** Namespaced
- **Purpose:** L4 TCP/UDP load balancing.

Key fields:
| Field | Type | Description |
|-------|------|-------------|
| `spec.virtualServerAddress` | String | BIG-IP VIP address |
| `spec.virtualServerPort` | Integer | Listening port |
| `spec.virtualServerName` | String | Custom VS name on BIG-IP |
| `spec.mode` | String | `standard` or `performance` |
| `spec.snat` | String | SNAT pool or `auto` |
| `spec.pool.service` | String | Kubernetes Service name |
| `spec.pool.servicePort` | Integer | Service port |
| `spec.pool.monitor` | Object | Health monitor |
| `spec.type` | String | `tcp` (default) or `udp` |

---

### ExternalDNS

- **API:** `cis.f5.com/v1`
- **Kind:** `ExternalDNS`
- **Scope:** Namespaced
- **Purpose:** Configure GTM/DNS wide-IP records on BIG-IP for GSLB.

Key fields:
| Field | Type | Description |
|-------|------|-------------|
| `spec.domainName` | String | DNS domain (e.g. `example.com`) |
| `spec.dnsRecordType` | String | `A` or `AAAA` |
| `spec.loadBalanceMethod` | String | `round-robin`, `ratio`, etc. |
| `spec.pools` | Array | DNS pool definitions |
| `spec.pools[].dataServerName` | String | GTM server path |
| `spec.pools[].monitor` | Object | Health monitor for DNS pool |

> Requires GTM BIG-IP parameters in CIS deployment (`--gtm-bigip-url`, etc.)

---

### Policy

- **API:** `cis.f5.com/v1`
- **Kind:** `Policy`
- **Scope:** Namespaced
- **Purpose:** Attach WAF, iRules, TCP/HTTP profiles, persistence, etc. to VirtualServer CRs.

Key fields:
| Field | Type | Description |
|-------|------|-------------|
| `spec.l7Policies.waf` | String | BIG-IP ASM/WAF policy path |
| `spec.l3Policies.firewallPolicy` | String | BIG-IP AFM firewall policy path |
| `spec.ltmPolicies` | Array | BIG-IP LTM policy references |
| `spec.iRules` | Array | BIG-IP iRule references |
| `spec.profiles.tcp` | Object | TCP profile configuration |
| `spec.profiles.http` | String | HTTP profile path |
| `spec.profiles.persistenceProfile` | String | Persistence profile path |

---

### IngressLink

- **API:** `cis.f5.com/v1`
- **Kind:** `IngressLink`
- **Scope:** Namespaced
- **Purpose:** Integration with third-party ingress controllers (e.g. NGINX, Traefik).

---

## Common Patterns

### serviceAddress (ARP + Route Advertisement)

Add to VirtualServer or TransportServer to enable BIG-IP to respond to ARP for the VIP
and advertise the route:

```yaml
serviceAddress:
  - icmpEcho: "enable"
    arpEnabled: true
    routeAdvertisement: "all"
```

### hostGroup (Shared VIP)

Multiple VirtualServer CRs can share the same VIP by using the same `hostGroup` value
and the same `virtualServerAddress`. CIS creates a single BIG-IP VS with policies to
route based on Host header.

```yaml
# VS 1
spec:
  host: cafe.example.com
  hostGroup: "shared-vip"
  virtualServerAddress: "10.1.1.100"

# VS 2
spec:
  host: httpbin.example.com
  hostGroup: "shared-vip"
  virtualServerAddress: "10.1.1.100"
```

---

## CRD Installation Command

```bash
kubectl create -f https://raw.githubusercontent.com/F5Networks/k8s-bigip-ctlr/v2.20.3/docs/config_examples/customResourceDefinitions/customresourcedefinitions.yml
```

Verify:
```bash
kubectl get crd | grep f5
```

Expected output:
```
externaldnses.cis.f5.com       ...
ingresslinks.cis.f5.com        ...
policies.cis.f5.com            ...
tlsprofiles.cis.f5.com         ...
transportservers.cis.f5.com    ...
virtualservers.cis.f5.com      ...
```
