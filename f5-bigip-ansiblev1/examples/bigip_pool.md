# bigip_pool


## Description

The `bigip_pool` module manages Local Traffic Manager (LTM) pools on F5 BIG-IP devices. Pools group backend nodes or pool members and define how traffic is load-balanced among them. With this module, you can create, modify, or delete pools; configure health monitors, load-balancing methods, and service ports; and control pool availability. It is a core building block for application delivery configurations, typically used alongside `bigip_node`, `bigip_pool_member`, and virtual server modules.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the pool. |
| **partition** | **Default:** Common | Partition where the pool resides. |
| **description** | **Type:** string | Description of the pool. |
| **lb_method** | **Choices:** round-robin, ratio-member, least-connections-member, least-sessions, observed-member, predictive-member, fastest-node, least-connections-node, ratio-node, observed-node, predictive-node, dynamic-ratio-member, dynamic-ratio-node, fallback-ip | Load-balancing method used for distributing traffic across members. |
| **monitor_type** | **Choices:** and_list, m_of_n | How multiple monitors are evaluated for pool health. |
| **monitors** | **Type:** list | List of health monitors to associate with the pool. |
| **service_down_action** | **Choices:** none, reset, drop, reselect | Action taken when all pool members are down. |
| **allow_nat** | **Type:** bool | Allows or disallows NAT for connections to the pool. |
| **allow_snat** | **Type:** bool | Allows or disallows SNAT for connections to the pool. |
| **minimum_active_members** | **Type:** int | Minimum number of active members required for the pool to be considered up. |
| **reselect_tries** | **Type:** int | Number of attempts to reselect a new member on failure. |
| **slow_ramp_time** | **Type:** int | Time for new members to ramp up to full traffic load. |
| **state** | **Choices:** present, absent | Desired state of the pool. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the pool managed by the module. |
| **partition** | Partition where the pool is configured. |
| **description** | Current description of the pool. |
| **lb_method** | Effective load-balancing method. |
| **monitors** | List of monitors applied to the pool. |
| **monitor_type** | How multiple monitors are combined. |
| **service_down_action** | Action taken when all members are down. |
| **minimum_active_members** | Minimum number of active members required. |
| **reselect_tries** | Configured reselection attempts count. |
| **slow_ramp_time** | Configured slow ramp time in seconds. |
| **state** | Final state of the pool (`present` or `absent`). |


## Examples


```yaml
- name: Create an HTTP pool with round-robin load balancing
  bigip_pool:
    name: web_pool
    partition: Common
    description: "Pool for web servers"
    lb_method: round-robin
    monitors:
      - /Common/http
    monitor_type: and_list
    slow_ramp_time: 30
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Configure service down action and minimum active members
  bigip_pool:
    name: api_pool
    service_down_action: reset
    minimum_active_members: 2
    reselect_tries: 3
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove an unused pool
  bigip_pool:
    name: old_pool
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



