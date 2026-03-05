# bigip_profile_oneconnect


## Description

The `bigip_profile_oneconnect` module manages OneConnect profiles on F5 BIG-IP systems. OneConnect profiles enable connection pooling and reuse on the server side, allowing multiple client requests to share a smaller set of back-end TCP connections. This improves performance and scalability for HTTP and other protocols that support connection reuse. The module lets administrators configure parameters such as idle timeouts and source masks to tune pooling behavior for specific applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | User-defined description of the OneConnect profile. |
| **idle_timeout_override** | **Type:** integer | Idle timeout in seconds for pooled server connections. |
| **limit_type** | **Choices:** none, connection, request | Type of limit applied to connections or requests. |
| **max_age** | **Type:** integer | Maximum age in seconds for a pooled connection. |
| **max_reuse** | **Type:** integer | Maximum number of reuses per connection. |
| **max_size** | **Type:** integer | Maximum number of connections in the pool. |
| **name** | **Type:** string<br>**Required:** yes | Name of the OneConnect profile. |
| **parent** | **Type:** string | Parent OneConnect profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **source_mask** | **Type:** string | Source IP mask used to determine connection reuse. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **description** | Description set on the profile. |
| **idle_timeout_override** | Idle timeout for pooled connections. |
| **limit_type** | Type of limit applied. |
| **max_age** | Maximum connection age. |
| **max_reuse** | Maximum reuse count. |
| **max_size** | Maximum pool size. |
| **name** | Name of the OneConnect profile managed. |
| **partition** | Partition where the profile is configured. |
| **source_mask** | Source mask used for pooling decisions. |


## Examples


```yaml
- name: Create OneConnect profile for HTTP pooling
  bigip_profile_oneconnect:
    name: oneconnect_http
    description: OneConnect for HTTP virtual servers
    parent: oneconnect
    source_mask: 0.0.0.0
    idle_timeout_override: 30
    max_reuse: 1000
    max_age: 300
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Limit OneConnect pool size
  bigip_profile_oneconnect:
    name: oneconnect_http
    max_size: 10000
    limit_type: connection
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove OneConnect profile
  bigip_profile_oneconnect:
    name: old_oneconnect
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



