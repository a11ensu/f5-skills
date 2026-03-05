# bigip_profile_fastl4


## Description

The `bigip_profile_fastl4` module manages Fast L4 profiles on F5 BIG-IP devices. Fast L4 profiles provide high-performance, full-proxy Layer 4 load balancing with minimal overhead, controlling TCP/UDP connection behavior, idle timeouts, and packet handling. This module enables administrators to create or adjust Fast L4 profiles for low-latency applications, tune performance and connection limits, and apply security options such as loose initiation or close, while maintaining consistent configuration across environments via automation.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **client_timeout** | **Type:** integer | Idle timeout in seconds for client-side connections. |
| **description** | **Type:** string | User-defined description of the Fast L4 profile. |
| **idle_timeout** | **Type:** integer | General idle timeout for connections if specific side not set. |
| **loose_close** | **Choices:** yes, no | Allows closing connections without full TCP handshake completion. |
| **loose_initialization** | **Choices:** yes, no | Allows connections to be created before full TCP handshake. |
| **name** | **Type:** string<br>**Required:** yes | Name of the Fast L4 profile. |
| **parent** | **Type:** string | Parent Fast L4 profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **reset_on_timeout** | **Choices:** yes, no | Sends a reset when a connection times out. |
| **server_timeout** | **Type:** integer | Idle timeout in seconds for server-side connections. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **client_timeout** | Effective client-side idle timeout. |
| **description** | Description set on the profile. |
| **idle_timeout** | General idle timeout for connections. |
| **loose_close** | Indicates if loose close is enabled. |
| **loose_initialization** | Indicates if loose initialization is enabled. |
| **name** | Name of the Fast L4 profile managed. |
| **partition** | Partition where the profile is configured. |
| **reset_on_timeout** | Whether reset is sent on timeout. |
| **server_timeout** | Effective server-side idle timeout. |


## Examples


```yaml
- name: Create Fast L4 profile for low-latency TCP
  bigip_profile_fastl4:
    name: fastl4_low_latency
    description: Fast L4 profile for trading app
    parent: fastL4
    idle_timeout: 30
    loose_initialization: yes
    loose_close: yes
    reset_on_timeout: yes
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Tune Fast L4 timeouts
  bigip_profile_fastl4:
    name: fastl4_low_latency
    client_timeout: 20
    server_timeout: 20
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove Fast L4 profile
  bigip_profile_fastl4:
    name: old_fastl4
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



