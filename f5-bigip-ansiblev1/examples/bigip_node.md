# bigip_node


## Description

The `bigip_node` module manages LTM nodes on F5 BIG-IP devices. A node typically represents a physical server or endpoint identified by an IP address or FQDN. This module lets you create, update, enable, disable, or remove nodes, as well as adjust health monitoring, connection limits, and other attributes. It is commonly used with `bigip_pool_member` and `bigip_pool` to build complete load-balancing configurations, ensuring consistent definitions for backend servers across your BIG-IP environment.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **address** | **Type:** string | IP address or FQDN of the node. Required when creating a node. |
| **connection_limit** | **Type:** int | Maximum number of concurrent connections allowed to the node. |
| **description** | **Type:** string | User-defined description for the node. |
| **dynamic_ratio** | **Type:** int | Dynamic ratio value used with certain load-balancing algorithms. |
| **fqdn** | **Type:** dict | FQDN configuration if the node is defined by DNS name. |
| **fqdn/address_family** | **Choices:** ipv4, ipv6, any | Restricts address family for DNS resolution. |
| **fqdn/autopopulate** | **Type:** bool | Automatically creates pool members from DNS-resolved addresses. |
| **fqdn/down_interval** | **Type:** int | Interval in seconds to mark node down when DNS resolution fails. |
| **fqdn/interval** | **Type:** int | Frequency in seconds for DNS lookups. |
| **logging** | **Type:** bool | Enables or disables connection logging for the node. |
| **monitor_type** | **Choices:** and_list, m_of_n | How multiple monitors are combined when assigned to the node. |
| **monitors** | **Type:** list | List of health monitors to associate with the node. |
| **name** | **Type:** string<br>**Required:** yes | Name of the node. |
| **partition** | **Default:** Common | Administrative partition the node belongs to. |
| **rate_limit** | **Type:** int | Maximum number of connections per second. |
| **ratio** | **Type:** int | Static ratio value for ratio-based load balancing. |
| **state** | **Choices:** present, absent, enabled, disabled, forced_offline | Desired state of the node. `present` maintains configuration, `enabled`/`disabled` control availability. |
| **session_state** | **Choices:** enabled, disabled, user-disabled | Session availability state independent of monitor results. |
| **availability_state** | **Choices:** enabled, disabled | Operational availability state. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **address** | The IP address or FQDN resolved address of the node. |
| **connection_limit** | The effective connection limit for the node. |
| **description** | The description currently set on the node. |
| **fqdn** | FQDN configuration applied to the node, if any. |
| **logging** | Indicates whether connection logging is enabled. |
| **monitors** | List of monitors bound to the node. |
| **partition** | Partition where the node resides. |
| **rate_limit** | The effective rate limit for the node. |
| **ratio** | The ratio value used for load balancing. |
| **state** | The final state of the node (enabled, disabled, offline, etc.). |


## Examples


```yaml
- name: Create a node with an IPv4 address
  bigip_node:
    name: web01
    address: 192.0.2.10
    description: "Primary web server"
    monitors:
      - /Common/http
    connection_limit: 0
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Create an FQDN-based node with DNS autopopulate
  bigip_node:
    name: app-servers.example.com
    fqdn:
      address_family: ipv4
      autopopulate: true
      interval: 300
    monitors:
      - /Common/tcp
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Disable a node for maintenance
  bigip_node:
    name: web01
    state: disabled
    session_state: user-disabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove a node
  bigip_node:
    name: old-backend
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



