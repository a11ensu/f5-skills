# bigip_message_routing_transport_config


## Description

The `bigip_message_routing_transport_config` module manages transport configuration objects for outgoing connections in the message-routing framework on F5 BIG-IP systems. Transport configurations define how TCP or other transports are established to peers, including timeouts, TLS settings, and connection limits. This module lets you create, update, or delete transport configurations to ensure reliable and secure message delivery.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the transport configuration object. |
| **defaults_from** | **Type:** string | Parent transport configuration to inherit from. |
| **idle_timeout** | **Type:** integer | Idle timeout in seconds for transport connections. |
| **max_connections** | **Type:** integer | Maximum concurrent connections allowed per transport. |
| **tls_profile** | **Type:** string | Client SSL/TLS profile applied to secure outgoing connections. |
| **source_address** | **Type:** string | Source address used for establishing connections. |
| **description** | **Type:** string | User-defined description for the transport configuration. |
| **partition** | **Default:** Common | Partition in which to manage the transport configuration. |
| **state** | **Choices:** present, absent | Whether the transport configuration should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the transport configuration. |
| **defaults_from** | Parent transport configuration used. |
| **idle_timeout** | Idle timeout configured. |
| **max_connections** | Connection limit configured. |
| **tls_profile** | TLS profile applied, if any. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a transport configuration for TLS connections
  bigip_message_routing_transport_config:
    name: app_transport
    defaults_from: /Common/genericmsg-tcp
    idle_timeout: 300
    max_connections: 5000
    tls_profile: /Common/clientssl
    source_address: 198.51.100.10
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Increase max connections for transport config
  bigip_message_routing_transport_config:
    name: app_transport
    max_connections: 10000
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a transport configuration
  bigip_message_routing_transport_config:
    name: app_transport
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
