# bigip_message_routing_router


## Description

The `bigip_message_routing_router` module manages router profiles used in the message-routing framework on F5 BIG-IP devices. Router profiles define how routing decisions are made for generic message protocols, including selection of routes, peers, and failover strategies. Using this module, you can create, modify, or remove router profiles to implement custom message distribution logic and high availability.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the message routing router profile. |
| **defaults_from** | **Type:** string | Parent router profile to inherit settings from. |
| **protocol** | **Type:** string | Message routing protocol profile associated with this router. |
| **load_balancing_mode** | **Choices:** ratio, round-robin, least-connections | Algorithm for selecting peers or routes. |
| **description** | **Type:** string | User-defined description for the router profile. |
| **partition** | **Default:** Common | Partition in which to manage the router profile. |
| **state** | **Choices:** present, absent | Whether the router profile should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the router profile. |
| **defaults_from** | Parent router profile used. |
| **protocol** | Protocol profile associated with this router. |
| **load_balancing_mode** | Load-balancing algorithm configured. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a message routing router profile
  bigip_message_routing_router:
    name: app_router
    defaults_from: /Common/genericmsg-router
    protocol: /Common/custom_msg_proto
    load_balancing_mode: ratio
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Change router load balancing mode
  bigip_message_routing_router:
    name: app_router
    load_balancing_mode: least-connections
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a router profile
  bigip_message_routing_router:
    name: app_router
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



