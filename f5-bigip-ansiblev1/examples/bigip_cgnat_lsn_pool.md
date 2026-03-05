# bigip_cgnat_lsn_pool


## Description

The `bigip_cgnat_lsn_pool` module manages Large Scale NAT (LSN) pools used by Carrier-Grade NAT (CGNAT) on F5 BIG-IP systems. It allows you to create, modify, or remove LSN pools, configure translation address ranges, port allocation strategies, and connection limits. By automating LSN pool configuration, the module helps service providers scale IPv4 address sharing, control subscriber behavior, and integrate CGNAT provisioning into broader orchestration workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the LSN pool. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the LSN pool resides. |
| **description** | **Type:** string | Descriptive text for the LSN pool. |
| **members** | **Type:** list | List of translation address ranges in CIDR or start-end format. |
| **members/address** | **Type:** string | IPv4 or IPv6 address or subnet for translation. |
| **members/port_range** | **Type:** string | Port range associated with this member (for example, `0-65535`). |
| **mode** | **Choices:** napt, pba | Translation mode: NAPT or Port Block Allocation (PBA). |
| **persistence_mode** | **Choices:** address, address-port | How subscriber sessions are persisted to translation addresses and ports. |
| **inbound_connections** | **Choices:** enabled, disabled | Whether inbound connections to subscribers are allowed. |
| **hairpinning** | **Choices:** enabled, disabled | Whether hairpin connections between subscribers are allowed. |
| **tcp_idle_timeout** | **Type:** integer | TCP idle timeout in seconds. |
| **udp_idle_timeout** | **Type:** integer | UDP idle timeout in seconds. |
| **icmp_idle_timeout** | **Type:** integer | ICMP idle timeout in seconds. |
| **port_alloc_mode** | **Choices:** dynamic, deterministic | Port allocation method for subscribers. |
| **protocol_profile** | **Type:** string | Name of a CGNAT protocol profile to associate with this pool. |
| **log_publisher** | **Type:** string | Name of a log publisher for CGNAT events. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the LSN pool; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the LSN pool. |
| **partition** | Partition where the LSN pool resides. |
| **members** | List of translation address members configured on the pool. |
| **mode** | Effective translation mode (NAPT or PBA). |
| **state** | Final state of the LSN pool (`present` or `absent`). |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Create NAPT LSN pool with address range
  bigip_cgnat_lsn_pool:
    name: cgnat_pool_1
    partition: Common
    description: "CGNAT pool for broadband subscribers"
    members:
      - address: 198.51.100.0/24
        port_range: 0-65535
    mode: napt
    persistence_mode: address-port
    inbound_connections: disabled
    hairpinning: enabled
    tcp_idle_timeout: 300
    udp_idle_timeout: 60
    icmp_idle_timeout: 30
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create PBA LSN pool with deterministic ports
  bigip_cgnat_lsn_pool:
    name: cgnat_pba_pool
    members:
      - address: 203.0.113.0/25
        port_range: 1024-65535
    mode: pba
    port_alloc_mode: deterministic
    log_publisher: cgnat-logger
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove LSN pool
  bigip_cgnat_lsn_pool:
    name: cgnat_pool_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

