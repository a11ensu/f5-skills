# bigip_message_routing_peer


## Description

The `bigip_message_routing_peer` module manages peers used for routing generic message protocol traffic on F5 BIG-IP systems. Peers represent remote endpoints or clusters that send or receive messages through the message-routing framework. With this module, you can define peer addresses, connection limits, load-balancing behavior, and health monitoring to build scalable, application-layer message routing topologies.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the message routing peer. |
| **transport_config** | **Type:** string | Name of the associated message routing transport configuration. |
| **address** | **Type:** string | IP address or hostname of the peer. |
| **port** | **Type:** integer | Port used to communicate with the peer. |
| **ratio** | **Type:** integer | Load-balancing ratio when multiple peers are used. |
| **max_connections** | **Type:** integer | Maximum concurrent connections allowed to this peer. |
| **monitor** | **Type:** string | Health monitor applied to the peer. |
| **description** | **Type:** string | User-defined description for the peer. |
| **partition** | **Default:** Common | Partition in which to manage the peer. |
| **state** | **Choices:** present, absent | Whether the peer should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the peer. |
| **address** | Configured address of the peer. |
| **port** | Configured port of the peer. |
| **transport_config** | Transport configuration associated with the peer. |
| **max_connections** | Connection limit applied to the peer. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a message routing peer
  bigip_message_routing_peer:
    name: app_peer_1
    address: 203.0.113.10
    port: 9000
    transport_config: /Common/app_transport
    max_connections: 1000
    ratio: 1
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update peer connection limit
  bigip_message_routing_peer:
    name: app_peer_1
    max_connections: 2000
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a message routing peer
  bigip_message_routing_peer:
    name: app_peer_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



