# bigip_profile_http


## Description

The `bigip_profile_http` module manages HTTP profiles on F5 BIG-IP devices. HTTP profiles define how BIG-IP processes HTTP traffic, including header handling, compression, connection reuse, request/response adaptations, and support for features like X-Forwarded-For or HTTP/1.1 pipelining. Using this module, administrators can create or modify HTTP profiles tailored to specific applications, optimize performance, enforce security and compliance requirements, and standardize behavior across virtual servers in automated deployments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **compress** | **Choices:** yes, no | Enables or disables HTTP compression within the profile. |
| **description** | **Type:** string | User-defined description of the HTTP profile. |
| **fallback_host** | **Type:** string | Hostname used when the pool is unavailable. |
| **insert_xforwarded_for** | **Choices:** yes, no | Inserts X-Forwarded-For header with client IP. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTP profile. |
| **oneconnect_transformations** | **Choices:** enabled, disabled | Controls whether OneConnect transformations are applied. |
| **parent** | **Type:** string | Parent HTTP profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **response_chunking** | **Choices:** selective, rechunk, preserve | How to handle HTTP response chunking. |
| **server_agent_name** | **Type:** string | Value for the Server header in responses. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **compress** | Indicates if HTTP compression is enabled. |
| **description** | Description set on the profile. |
| **fallback_host** | Configured fallback host. |
| **insert_xforwarded_for** | Indicates if X-Forwarded-For is inserted. |
| **name** | Name of the HTTP profile managed. |
| **partition** | Partition where the profile is configured. |
| **response_chunking** | Response chunking behavior. |
| **server_agent_name** | Server header value used. |


## Examples


```yaml
- name: Create HTTP profile with XFF and compression
  bigip_profile_http:
    name: http_webapp
    description: HTTP profile for main web application
    parent: http
    insert_xforwarded_for: yes
    compress: yes
    response_chunking: selective
    server_agent_name: "BIG-IP"
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Set fallback host on HTTP profile
  bigip_profile_http:
    name: http_webapp
    fallback_host: maintenance.example.com
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove HTTP profile
  bigip_profile_http:
    name: old_http_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



