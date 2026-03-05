# bigip_profile_http2


## Description

The `bigip_profile_http2` module manages HTTP/2 profiles on F5 BIG-IP systems. HTTP/2 profiles control how BIG-IP negotiates and handles HTTP/2 connections, including settings for concurrency, header compression, and protocol negotiation (ALPN). By configuring HTTP/2 profiles, administrators can enable modern web performance features such as multiplexing and header compression on virtual servers, while tuning resource usage and compatibility with clients and back-end applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **concurrent_streams_per_connection** | **Type:** integer | Maximum number of concurrent streams per connection. |
| **description** | **Type:** string | User-defined description of the HTTP/2 profile. |
| **header_table_size** | **Type:** integer | Size of the HPACK header table in bytes. |
| **initial_window_size** | **Type:** integer | Initial flow-control window size in bytes. |
| **max_frame_size** | **Type:** integer | Maximum size of HTTP/2 frames in bytes. |
| **max_header_list_size** | **Type:** integer | Maximum size of header list in bytes. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTP/2 profile. |
| **parent** | **Type:** string | Parent HTTP/2 profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **concurrent_streams_per_connection** | Effective limit of concurrent streams. |
| **description** | Description set on the profile. |
| **header_table_size** | Configured HPACK header table size. |
| **initial_window_size** | Configured initial window size. |
| **max_frame_size** | Maximum HTTP/2 frame size. |
| **max_header_list_size** | Maximum allowed header list size. |
| **name** | Name of the HTTP/2 profile managed. |
| **partition** | Partition where the profile is configured. |


## Examples


```yaml
- name: Create HTTP/2 profile for web app
  bigip_profile_http2:
    name: http2_webapp
    description: HTTP/2 profile for main web application
    parent: http2
    concurrent_streams_per_connection: 100
    header_table_size: 4096
    initial_window_size: 65535
    max_frame_size: 16384
    max_header_list_size: 32768
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Tune HTTP/2 concurrency
  bigip_profile_http2:
    name: http2_webapp
    concurrent_streams_per_connection: 50
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove HTTP/2 profile
  bigip_profile_http2:
    name: old_http2_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



