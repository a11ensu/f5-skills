# bigip_message_routing_protocol


## Description

The `bigip_message_routing_protocol` module manages generic message parser profiles on F5 BIG-IP devices. These profiles define how the system interprets, delimits, and processes application-layer messages carried over TCP or other transports. By using this module, you can configure parsing rules, message boundaries, and framing behaviors for custom or proprietary protocols within the message-routing framework.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the message routing protocol profile. |
| **defaults_from** | **Type:** string | Parent profile to inherit default settings from. |
| **delimiter** | **Type:** string | Delimiter used to separate messages in the stream. |
| **max_message_size** | **Type:** integer | Maximum allowed size of a single message in bytes. |
| **idle_timeout** | **Type:** integer | Idle timeout in seconds for connections using this profile. |
| **description** | **Type:** string | User-defined description for the protocol profile. |
| **partition** | **Default:** Common | Partition in which to manage the protocol profile. |
| **state** | **Choices:** present, absent | Whether the profile should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the protocol profile. |
| **defaults_from** | Parent profile used for defaults. |
| **delimiter** | Configured message delimiter. |
| **max_message_size** | Maximum message size configured. |
| **idle_timeout** | Idle timeout value. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a message routing protocol profile
  bigip_message_routing_protocol:
    name: custom_msg_proto
    defaults_from: /Common/genericmsg
    delimiter: "\n"
    max_message_size: 65535
    idle_timeout: 300
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update maximum message size
  bigip_message_routing_protocol:
    name: custom_msg_proto
    max_message_size: 131070
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a message routing protocol profile
  bigip_message_routing_protocol:
    name: custom_msg_proto
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



