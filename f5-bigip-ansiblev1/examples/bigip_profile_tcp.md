# bigip_profile_tcp


## Description

The `bigip_profile_tcp` module manages TCP profiles on F5 BIG-IP systems. TCP profiles control how BIG-IP handles TCP connections, including congestion control, buffering, window scaling, Nagle’s algorithm, and timeouts. By tuning TCP profiles, administrators can optimize performance for different application types (such as high-latency WAN, low-latency LAN, or bulk transfers), improve throughput, and mitigate issues like slow-start or connection resets in automated and repeatable ways.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **congestion_control** | **Type:** string | TCP congestion control algorithm (for example, newreno, cubic). |
| **description** | **Type:** string | User-defined description of the TCP profile. |
| **idle_timeout** | **Type:** integer | Idle timeout in seconds for TCP connections. |
| **keepalive_interval** | **Type:** integer | Interval in seconds between TCP keepalive probes. |
| **max_syn_retrans** | **Type:** integer | Maximum number of SYN retransmissions. |
| **name** | **Type:** string<br>**Required:** yes | Name of the TCP profile. |
| **nagle** | **Choices:** enabled, disabled | Enables or disables Nagle’s algorithm. |
| **parent** | **Type:** string | Parent TCP profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **proxy_buffer_high** | **Type:** integer | High watermark for proxy buffer size. |
| **proxy_buffer_low** | **Type:** integer | Low watermark for proxy buffer size. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **congestion_control** | Congestion control algorithm used. |
| **description** | Description set on the profile. |
| **idle_timeout** | Idle timeout for TCP connections. |
| **keepalive_interval** | Keepalive interval configured. |
| **max_syn_retrans** | Maximum SYN retransmissions. |
| **name** | Name of the TCP profile managed. |
| **nagle** | Indicates if Nagle’s algorithm is enabled. |
| **partition** | Partition where the profile is configured. |
| **proxy_buffer_high** | High watermark for proxy buffer. |
| **proxy_buffer_low** | Low watermark for proxy buffer. |


## Examples


```yaml
- name: Create TCP profile optimized for WAN
  bigip_profile_tcp:
    name: tcp_wan_optimized
    description: TCP profile for high-latency WAN
    parent: tcp
    congestion_control: cubic
    idle_timeout: 300
    keepalive_interval: 60
    max_syn_retrans: 5
    nagle: disabled
    proxy_buffer_high: 131072
    proxy_buffer_low: 98304
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Adjust idle timeout for TCP profile
  bigip_profile_tcp:
    name: tcp_wan_optimized
    idle_timeout: 600
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove TCP profile
  bigip_profile_tcp:
    name: old_tcp_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



