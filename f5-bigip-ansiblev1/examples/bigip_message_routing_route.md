# bigip_message_routing_route


## Description

The `bigip_message_routing_route` module manages static routes for generic message protocol traffic on F5 BIG-IP systems. These routes determine how messages are forwarded to peers or pools based on routing keys such as destination addresses, application identifiers, or other attributes. With this module, you can define routing paths, priorities, and failover behavior for complex message-routing topologies.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the message routing route. |
| **router** | **Type:** string | Name of the associated message routing router profile. |
| **peer** | **Type:** string | Target peer or peer selection for this route. |
| **pool** | **Type:** string | Pool used as the next hop for messages. |
| **priority** | **Type:** integer | Route priority; lower values have higher preference. |
| **description** | **Type:** string | User-defined description of the route. |
| **partition** | **Default:** Common | Partition in which to manage the route. |
| **state** | **Choices:** present, absent | Whether the route should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the route. |
| **router** | Router profile associated with the route. |
| **peer** | Peer used as next hop, if configured. |
| **pool** | Pool used as next hop, if configured. |
| **priority** | Priority of the route. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a message routing route to a peer
  bigip_message_routing_route:
    name: route_to_app1
    router: /Common/app_router
    peer: /Common/app_peer_1
    priority: 10
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a backup route using a pool
  bigip_message_routing_route:
    name: route_to_app1_backup
    router: /Common/app_router
    pool: /Common/app_pool_backup
    priority: 20
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a message routing route
  bigip_message_routing_route:
    name: route_to_app1_backup
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



