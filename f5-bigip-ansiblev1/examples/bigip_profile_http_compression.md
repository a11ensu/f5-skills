# bigip_profile_http_compression


## Description

The `bigip_profile_http_compression` module manages HTTP compression profiles on F5 BIG-IP devices. These profiles define how and when BIG-IP compresses HTTP responses, including supported compression algorithms, content types, and size thresholds. By using this module, administrators can optimize bandwidth usage and improve page load times for clients, while maintaining control over CPU utilization and avoiding compression for already-compressed or sensitive content.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **buffer_size** | **Type:** integer | Size of the compression buffer in bytes. |
| **compression_level** | **Type:** integer | Compression level (typically 1–9, higher is more CPU-intensive). |
| **content_types** | **Type:** list | List of MIME types to compress (for example, text/html). |
| **description** | **Type:** string | User-defined description of the compression profile. |
| **min_size** | **Type:** integer | Minimum response size in bytes to trigger compression. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTP compression profile. |
| **parent** | **Type:** string | Parent compression profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **buffer_size** | Compression buffer size. |
| **compression_level** | Compression level configured. |
| **content_types** | MIME types subject to compression. |
| **description** | Description set on the profile. |
| **min_size** | Minimum size to trigger compression. |
| **name** | Name of the compression profile managed. |
| **partition** | Partition where the profile is configured. |


## Examples


```yaml
- name: Create HTTP compression profile for text content
  bigip_profile_http_compression:
    name: http_compress_text
    description: Compress text and JSON responses
    parent: httpcompression
    compression_level: 6
    buffer_size: 8192
    min_size: 1024
    content_types:
      - text/html
      - text/css
      - application/javascript
      - application/json
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Adjust compression level
  bigip_profile_http_compression:
    name: http_compress_text
    compression_level: 4
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove HTTP compression profile
  bigip_profile_http_compression:
    name: old_http_compression
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



