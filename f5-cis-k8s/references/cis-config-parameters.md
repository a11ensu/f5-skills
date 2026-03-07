# CIS Configuration Parameters Reference

Source: https://clouddocs.f5.com/containers/latest/userguide/config-parameters.html

All parameters are passed as command-line arguments in the CIS Deployment spec `args` array.

---

## BIG-IP System (Required)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--bigip-url` | String | — | BIG-IP admin IP or URL. Examples: `10.82.255.202`, `https://bigip.example.com:8443` |
| `--bigip-username` | String | — | BIG-IP iControl REST username (Administrator role required) |
| `--bigip-password` | String | — | BIG-IP iControl REST password |
| `--bigip-partition` | String | — | BIG-IP partition for CIS-managed objects. AS3 agent cannot write to `Common` |

## General

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--custom-resource-mode` | Boolean | false | Process CRD resources. When `true`, ConfigMaps/Routes/Ingress are NOT processed |
| `--agent` | String | AS3 | Agent for BIG-IP communication: `AS3` or `CCCL` |
| `--insecure` | Boolean | false | Skip TLS certificate verification to BIG-IP |
| `--ipam` | Boolean | false | Enable interface with F5 IPAM Controller (FIC) |
| `--ipam-namespace` | String | kube-system | Namespace of IPAM custom resource |
| `--verify-interval` | Integer | 30 | Interval (sec) at which NET config is synced to BIG-IP |
| `--node-poll-interval` | Integer | 30 | Interval (sec) at which CIS monitors node membership |
| `--static-routing-mode` | Boolean | false | Add static routes on BIG-IP for direct pod routing (no tunnels) |
| `--orchestration-cni` | String | flannel | CNI name: `cilium-k8s`, `flannel`, `ovn-k8s`, `antrea` |
| `--default-route-domain` | Integer | 0 | Default Route Domain for custom resources |
| `--custom-resource-label` | String | f5cr=true | Label CIS watches on custom resources |

## Logging

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--log-level` | String | INFO | Log level: `INFO`, `DEBUG`, `AS3DEBUG`, `WARNING`, `ERROR`, `CRITICAL` |
| `--log-as3-response` | Boolean | false | Log the body of AS3 API responses |
| `--log-file` | String | — | File path to store CIS logs |

## VXLAN

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--flannel-name` | String | — | BIG-IP VXLAN tunnel name for Flannel/Cilium subnet |
| `--openshift-sdn-name` | String | — | BIG-IP VXLAN tunnel for OpenShift SDN HostSubnet *(not used in K8s)* |
| `--cilium-name` | String | — | BIG-IP VXLAN tunnel for Cilium subnet |

> Only ONE VXLAN parameter is allowed per CIS deployment.

## Kubernetes

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--pool-member-type` | String | nodeport | `cluster` (pod IPs), `nodeport` (node IPs + NodePort), `auto` (CRD/NextGen only) |
| `--namespace` | String | all | Namespace(s) to watch. Use multiple `--namespace` flags for multiple namespaces |
| `--namespace-label` | String | — | Watch namespaces matching this label |
| `--node-label-selector` | String | — | Only manage nodes with this label |
| `--default-ingress-ip` | String | — | VIP for Ingresses with `virtual-server.f5.com/ip: 'controller-default'` |
| `--kubeconfig` | String | ./config | Path to kubeconfig file |
| `--running-in-cluster` | Boolean | true | Whether CIS runs inside the cluster |
| `--use-node-internal` | Boolean | true | Use InternalIP for pool members |
| `--ingress-class` | String | F5 | Ingress class CIS responds to |

## GTM BIG-IP (for ExternalDNS CRDs)

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--gtm-bigip-url` | String | — | GTM BIG-IP URL |
| `--gtm-bigip-username` | String | — | GTM BIG-IP username |
| `--gtm-bigip-password` | String | — | GTM BIG-IP password |

## Multi-Cluster

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `--multi-cluster-mode` | String | — | `standalone` or `primary` or `secondary` |

---

## Notes

- `AS3DEBUG` log level logs both AS3 requests and responses — use only for debugging.
- `--custom-resource-mode=true` and `--controller-mode=openshift` are mutually exclusive.
- For Cluster mode pool members, BIG-IP user must have **Administrator** role.
- The `--bigip-partition` value becomes the AS3 tenant name on BIG-IP.
