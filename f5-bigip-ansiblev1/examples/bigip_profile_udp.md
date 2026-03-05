# bigip_profile_udp


## Description

The `bigip_profile_udp` module manages UDP profiles on F5 BIG-IP devices. UDP profiles define how BIG-IP handles UDP traffic, including idle timeouts, datagram processing, and optional features like Datagram TLS (DTLS) or NAT-related behaviors. By configuring UDP profiles, administrators can tune performance and resource usage for latency-sensitive or high-throughput UDP applications such as DNS, VoIP, or streaming services across BIG-IP virtual servers.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **datagram_load_balancing** | **Choices:** yes, no | Enables load balancing on a per-datagram basis. |
| **description** | **Type:** string | User-defined description of the UDP profile. |
| **idle_timeout** | **Type:** integer | Idle timeout in seconds for UDP flows. |
| **name** | **Type:** string<br>**Required:** yes | Name of the UDP profile. |
| **parent** | **Type:** string | Parent UDP profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **proxy_mss** | **Type:** integer | Proxy Maximum Segment Size for UDP encapsulations (if applicable). |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **datagram_load_balancing** | Indicates if per-datagram load balancing is enabled. |
| **description** | Description set on the profile. |
| **idle_timeout** | Idle timeout for UDP flows. |
| **name** | Name of the UDP profile managed. |
| **partition** | Partition where the profile is configured. |
| **proxy_mss** | Proxy MSS value configured. |


## Examples


```yaml
- name: Create UDP profile for DNS traffic
  bigip_profile_udp:
    name: udp_dns_profile
    description: UDP profile optimized for DNS
    parent: udp
    idle_timeout: 60
    datagram_load_balancing: yes
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Extend UDP idle timeout
  bigip_profile_udp:
    name: udp_dns_profile
    idle_timeout: 120
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove UDP profile
  bigip_profile_udp:
    name: old_udp_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
