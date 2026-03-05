# bigip_pool_member


## Description

The `bigip_pool_member` module manages individual members within an LTM pool on F5 BIG-IP devices. A pool member is a combination of a node (IP or FQDN) and a service port. This module allows you to add, update, enable, disable, or remove pool members, as well as configure per-member monitors, ratios, and connection limits. It is typically used together with `bigip_pool` and `bigip_node` to build robust, flexible load-balancing configurations tailored to application requirements.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **pool** | **Type:** string<br>**Required:** yes | Name of the pool that the member belongs to. |
| **partition** | **Default:** Common | Partition of the pool and member. |
| **name** | **Type:** string<br>**Required:** yes | Name of the member, usually in the form `ip:port` or `node_name:port`. |
| **address** | **Type:** string | IP address of the member; required when creating if not using existing node name. |
| **port** | **Type:** int | Service port of the member if not specified in `name`. |
| **description** | **Type:** string | Description of the pool member. |
| **connection_limit** | **Type:** int | Maximum concurrent connections allowed to this member. |
| **rate_limit** | **Type:** int | Maximum connections per second for this member. |
| **ratio** | **Type:** int | Ratio used for ratio-based load balancing. |
| **monitors** | **Type:** list | List of monitors applied specifically to this member. |
| **monitor_type** | **Choices:** and_list, m_of_n | How multiple monitors are combined for the member. |
| **state** | **Choices:** present, absent, enabled, disabled, forced_offline | Desired state of the pool member. |
| **session_state** | **Choices:** enabled, disabled, user-disabled | Session availability state for the member. |
| **availability_state** | **Choices:** enabled, disabled | Operational availability state. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **pool** | Pool to which the member belongs. |
| **name** | Name of the pool member. |
| **partition** | Partition where the member resides. |
| **address** | IP address associated with the member. |
| **port** | Service port of the member. |
| **description** | Description currently set on the member. |
| **connection_limit** | Effective connection limit for the member. |
| **rate_limit** | Effective rate limit for the member. |
| **ratio** | Ratio used for load balancing. |
| **monitors** | Monitors applied directly to the member. |
| **state** | Final state of the member (present, enabled, disabled, etc.). |


## Examples


```yaml
- name: Add a pool member by IP and port
  bigip_pool_member:
    pool: web_pool
    name: 192.0.2.10:80
    address: 192.0.2.10
    port: 80
    description: "Web server 1"
    ratio: 1
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Add a member with custom monitors and limits
  bigip_pool_member:
    pool: api_pool
    name: api01:8080
    address: 198.51.100.20
    port: 8080
    monitors:
      - /Common/http
    monitor_type: and_list
    connection_limit: 1000
    rate_limit: 200
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Disable a pool member for maintenance
  bigip_pool_member:
    pool: web_pool
    name: 192.0.2.10:80
    state: disabled
    session_state: user-disabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove a pool member
  bigip_pool_member:
    pool: web_pool
    name: 192.0.2.10:80
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
