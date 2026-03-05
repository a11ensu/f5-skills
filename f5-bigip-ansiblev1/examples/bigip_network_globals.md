# bigip_network_globals


## Description

The `bigip_network_globals` module manages device-wide network settings on F5 BIG-IP systems. It allows you to configure global options such as route advertisement, packet throughput optimizations, connection limits, and other global networking behaviors that affect all traffic on the device. Use this module to standardize network behavior across multiple BIG-IP devices or to enforce specific global policies required by your environment, without needing to modify individual virtual servers, pools, or profiles.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **accept_ip_options** | **Type:** bool | Enables or disables acceptance of packets with IP options. |
| **allow_dynamic_route_advertisement** | **Type:** bool | Allows dynamic routing protocols to advertise routes. |
| **arp_icmp_limit** | **Type:** int | Limits the number of ARP and ICMP unreachable responses per second. |
| **arp_icmp_limit_timeout** | **Type:** int | Time window in seconds for ARP/ICMP limit calculations. |
| **default_gateway** | **Type:** string | Specifies the default route gateway address. |
| **description** | **Type:** string | User-defined description for the global network configuration. |
| **ecmp_hash** | **Choices:** dst-ip, dst-port, ip-protocol, none, src-dst-ip, src-dst-ip-port, src-ip, src-port | Specifies the ECMP load balancing hash algorithm. |
| **icmp_unreachable** | **Type:** bool | Enables or disables sending ICMP unreachable messages. |
| **ip_forward** | **Type:** bool | Enables or disables IP forwarding globally. |
| **ip6_forward** | **Type:** bool | Enables or disables IPv6 forwarding globally. |
| **log_icmp_errors** | **Type:** bool | Enables or disables logging of ICMP errors. |
| **max_syn_retrans** | **Type:** int | Maximum number of SYN retransmissions allowed. |
| **max_concurrent_connections** | **Type:** int | Limits the maximum number of concurrent connections. |
| **path_mtu_discovery** | **Type:** bool | Enables or disables Path MTU Discovery. |
| **route_advertisement** | **Choices:** enabled, disabled, selective | Controls advertisement of routes to dynamic routing protocols. |
| **syn_cookie_protection** | **Type:** bool | Enables or disables SYN cookie protection globally. |
| **tcp_timestamps** | **Type:** bool | Enables or disables TCP timestamps. |
| **tcp_window_scaling** | **Type:** bool | Enables or disables TCP window scaling. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). Modifies module behavior to connect to the device. |
| **state** | **Choices:** present | Ensures the global network settings are configured as specified. |


## Return Values


| Key | Description |
| --- | --- |
| **accept_ip_options** | Indicates whether IP options are accepted on the device. |
| **allow_dynamic_route_advertisement** | Shows if dynamic route advertisement is enabled. |
| **arp_icmp_limit** | The configured ARP/ICMP response rate limit. |
| **default_gateway** | The currently configured default gateway. |
| **ecmp_hash** | The active ECMP hash algorithm. |
| **icmp_unreachable** | Whether ICMP unreachable messages are enabled. |
| **ip_forward** | Indicates if IP forwarding is globally enabled. |
| **ip6_forward** | Indicates if IPv6 forwarding is globally enabled. |
| **max_concurrent_connections** | The effective global connection limit. |
| **path_mtu_discovery** | Whether Path MTU Discovery is enabled. |
| **route_advertisement** | Current route advertisement mode. |
| **syn_cookie_protection** | Whether SYN cookie protection is active globally. |
| **tcp_timestamps** | Whether TCP timestamps are enabled. |
| **tcp_window_scaling** | Whether TCP window scaling is enabled. |


## Examples


```yaml
- name: Configure global network options for forwarding and ICMP
  bigip_network_globals:
    ip_forward: true
    ip6_forward: true
    icmp_unreachable: true
    log_icmp_errors: true
    arp_icmp_limit: 1000
    arp_icmp_limit_timeout: 1
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Harden global TCP behavior
  bigip_network_globals:
    syn_cookie_protection: true
    max_syn_retrans: 3
    tcp_timestamps: true
    tcp_window_scaling: true
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Configure ECMP and route advertisement
  bigip_network_globals:
    ecmp_hash: src-dst-ip-port
    route_advertisement: selective
    allow_dynamic_route_advertisement: true
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



