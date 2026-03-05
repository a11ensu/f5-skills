# bigip_apm_network_access

## Description

The `bigip_apm_network_access` module allows for the configuration and management of Network Access resources within the F5 BIG-IP Access Policy Manager (APM). It supports defining split tunneling policies, assigning IPv4 and IPv6 lease pools, and configuring DNS address spaces. Administrators can also manage DTLS settings for optimized performance and define exclusion lists for specific IP subnets or DNS domains. This module ensures precise control over VPN traffic handling, enabling secure and efficient remote access setups directly through Ansible automation.

## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **allow\_local\_dns** | **Choices:** no, yes | Enables local access to DNS servers configured on the client prior to establishing a network access connection. |
| **allow\_local\_subnet** | **Choices:** no, yes | Enables local subnet access and local access to any host or subnet in routes specified in the client routing table. When `true` the system does not support integrated IP filtering. |
| **description** | **Type:** string | User created network access description. |
| **dns\_address\_space** | **Type:** list | Specifies a list of domain names describing the target LAN DNS addresses. |
| **dtls** | **Choices:** no, yes | When `true` the network access connection uses Datagram Transport Level Security instead of TCP, to provide better throughput for high demand applications like VoIP or streaming video. |
| **dtls\_port** | **Type:** integer | Specifies the port number the network access resource uses for secure UDP traffic with DTLS. |
| **excluded\_dns\_addresses** | **Type:** list | Specifies the DNS address spaces for which traffic is not forced through the tunnel. |
| **excluded\_ipv4\_adresses** | **Type:** list | Specifies IPV4 address spaces for which traffic is not forced through the tunnel. Elements are dictionaries containing `subnet`. |
| **excluded\_ipv4\_adresses/subnet** | **Type:** string | The address of subnet in CIDR format, e.g. `192.168.1.0/24`. Host addresses can be specified without the CIDR mask notation. |
| **excluded\_ipv6\_adresses** | **Type:** list | Specifies IPV6 address spaces for which traffic is not forced through the tunnel. Elements are dictionaries containing `subnet`. |
| **excluded\_ipv6\_adresses/subnet** | **Type:** string | The address of a subnet in CIDR format, e.g. `2001:db8:abcd:8000::/52`. Host addresses can be specified without the CIDR mask notation. |
| **ip\_version** | **Choices:** ipv4, ipv4-ipv6 | Supported IP version on the network access resource. |
| **ipv4\_address\_space** | **Type:** list | Specifies a list of IPv4 hosts or networks describing the target LAN. Mandatory when creating a new resource and `split_tunnel` is `true`. Elements are dictionaries containing `subnet`. |
| **ipv4\_address\_space/subnet** | **Type:** string | The address of subnet in CIDR format, e.g. `192.168.1.0/24`. Host addresses can be specified without the CIDR mask notation. |
| **ipv4\_lease\_pool** | **Type:** string | Specifies the IPV4 lease pool resource to use with network access. Can be full path (e.g. `/Common/pool_name`). |
| **ipv6\_address\_space** | **Type:** list | Specifies a list of IPv6 hosts or networks describing the target LAN. Mandatory when creating a new resource and `split_tunnel` is `true`. Elements are dictionaries containing `subnet`. |
| **ipv6\_address\_space/subnet** | **Type:** string | The address of subnet in CIDR format, e.g. `2001:db8:abcd:8000::/52`. Host addresses can be specified without the CIDR mask notation. |
| **ipv6\_lease\_pool** | **Type:** string | Specifies the IPV6 lease pool resource to use with network access. Can be full path (e.g. `/Common/pool_name`). |
| **name** | **Type:** string<br>**Required:** yes | Specifies the name of the APM network access to manage/create. |
| **partition** | **Default:** Common | Device partition to manage resources on. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **snat\_pool** | **Type:** string | Specifies the name of a SNAT pool used for implementing selective and intelligent SNATs. Use `none` for no SNAT pool, or `automap` to use self IPs. |
| **split\_tunnel** | **Choices:** no, yes | Specifies that only the traffic targeted to a specified address space is sent over the network access tunnel. |
| **state** | **Choices:** present, absent | `present` ensures the resource exists; `absent` removes it. |

## Return Values

| Key | Description |
| --- | --- |
| **allow\_local\_dns** | Enables local access to DNS servers configured on the client. |
| **allow\_local\_subnet** | Enables local subnet access. |
| **description** | The new description of Network Access. |
| **dns\_address\_space** | Specifies a list of domain names describing the target LAN DNS addresses. |
| **dtls** | Enables use of DTLS by network access. |
| **dtls\_port** | Specifies the port number the network access resource uses for DTLS. |
| **excluded\_dns\_addresses** | Specifies the DNS address spaces for which traffic is not forced through the tunnel. |
| **excluded\_ipv4\_adresses** | Specifies IPV4 address spaces for which traffic is not forced through the tunnel. |
| **excluded\_ipv6\_adresses** | Specifies IPV6 address spaces for which traffic is not forced through the tunnel. |
| **ip\_version** | Supported IP version on the network access resource. |
| **ipv4\_address\_space** | Specifies a list of IPv4 hosts or networks describing the target LAN. |
| **ipv4\_lease\_pool** | Specifies a IPV4 lease pool resource to use with network access. |
| **ipv6\_address\_space** | Specifies a list of IPv6 hosts or networks describing the target LAN. |
| **ipv6\_lease\_pool** | Specifies a IPV6 lease pool resource to use with network access. |
| **snat\_pool** | The name of a SNAT pool used by the network access resource. |
| **split\_tunnel** | Enables split tunnel on the network access resource. |

## Examples

```yaml
- name: Create a split tunnel IPV4 Network Access
  bigip_apm_network_access:
    name: foobar
    ip_version: ipv4
    split_tunnel: true
    snat_pool: "none"
    ipv4_lease_pool: leasefoo
    ipv4_address_space:
      - subnet: 10.10.1.1
      - subnet: 10.10.2.0/24
    excluded_ipv4_adresses:
      - subnet: 192.168.1.0/24
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Modify a split tunnel IPV4 Network Access
  bigip_apm_network_access:
    name: foobar
    snat_pool: /Common/poolsnat
    ipv4_address_space:
      - subnet: 172.16.23.0/24
    excluded_ipv4_adresses:
      - subnet: 10.10.2.0/24
    allow_local_subnet: true
    allow_local_dns: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove Network Access
  bigip_apm_network_access:
    name: foobar
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```

## Tested Playbooks