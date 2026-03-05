# bigip_dns_resolver


## Description

The `bigip_dns_resolver` module manages DNS resolver objects on F5 BIG-IP systems. DNS resolvers define how the BIG-IP performs recursive DNS lookups, including which nameservers to query, retry and timeout behavior, and whether to use IPv4 or IPv6. This module allows you to create, update, or delete resolvers, associate them with nameservers, and tune resolution parameters to match your network design and performance needs.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **cache** | **Type:** string | Name of the associated DNS cache resolver, if any. |
| **description** | **Type:** string | Description of the DNS resolver. |
| **ignore_tc** | **Type:** bool | When `yes`, ignores truncated (TC) bit and does not retry over TCP. |
| **max_concurrent** | **Type:** integer | Maximum concurrent queries handled by this resolver. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DNS resolver object. |
| **nameservers** | **Type:** list | List of DNS nameserver objects associated with this resolver. |
| **partition** | **Default:** Common | Administrative partition where the resolver resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **retries** | **Type:** integer | Number of retry attempts per query before failing. |
| **state** | **Choices:** present, absent | `present` ensures the resolver exists; `absent` removes it. |
| **timeout** | **Type:** integer | Timeout in seconds for each query attempt. |
| **use_ipv4** | **Type:** bool | Enables IPv4 resolution. |
| **use_ipv6** | **Type:** bool | Enables IPv6 resolution. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the DNS resolver configured. |
| **nameservers** | List of associated nameserver objects. |
| **timeout** | Timeout applied to DNS queries. |
| **retries** | Number of retries configured per query. |


## Examples


```yaml
- name: Create a DNS resolver using two nameservers
  bigip_dns_resolver:
    name: dns_resolver_1
    nameservers:
      - ns1_google
      - ns1_corp
    timeout: 5
    retries: 2
    use_ipv4: true
    use_ipv6: false
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update resolver to enable IPv6
  bigip_dns_resolver:
    name: dns_resolver_1
    use_ipv6: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a DNS resolver
  bigip_dns_resolver:
    name: dns_resolver_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



