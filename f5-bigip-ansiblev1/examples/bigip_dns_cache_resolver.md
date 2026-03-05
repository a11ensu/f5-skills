# bigip_dns_cache_resolver


## Description

The `bigip_dns_cache_resolver` module manages DNS resolver cache objects on F5 BIG-IP systems. These caches store responses from upstream DNS servers to improve resolution performance and reduce external query load. With this module, you can create, update, or remove cache resolvers, control TTL behavior, enable or disable caching of negative responses, and tune size and eviction settings to optimize DNS caching for your environment.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **answer_default_zones** | **Type:** bool | When `yes`, the cache answers queries for built-in default zones (such as localhost and reverse zones). |
| **cache_size** | **Type:** integer | Maximum number of records or entries the cache can store, depending on BIG-IP version. |
| **dnssec** | **Type:** bool | Enables or disables DNSSEC-aware caching behavior. |
| **ignore_ttl** | **Type:** bool | When `yes`, ignores TTLs in responses and uses BIG-IP-defined values. |
| **max_concurrent** | **Type:** integer | Limits the number of concurrent DNS queries handled by this cache. |
| **max_entry** | **Type:** integer | Maximum number of entries per record or per name, depending on version. |
| **max_stale_age** | **Type:** integer | Maximum age in seconds for serving stale answers when upstream is unavailable. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DNS cache resolver object. |
| **partition** | **Default:** Common | Administrative partition where the cache resides. |
| **persistent** | **Type:** bool | When `yes`, cache entries persist across TMM restarts if supported. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **query_behavior** | **Choices:** use-local-bind, use-dns-profile | Controls how queries are forwarded or processed. |
| **resolver** | **Type:** string | Name of the associated DNS resolver configuration, if required. |
| **state** | **Choices:** present, absent | `present` ensures the cache exists; `absent` removes it. |
| **use_ipv4** | **Type:** bool | Enables IPv4 query handling. |
| **use_ipv6** | **Type:** bool | Enables IPv6 query handling. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | The name of the DNS cache resolver managed by the module. |
| **cache_size** | Effective size of the cache after configuration. |
| **dnssec** | Indicates whether DNSSEC-aware caching is enabled. |
| **ignore_ttl** | Indicates whether TTLs from upstream servers are ignored. |


## Examples


```yaml
- name: Create a DNS cache resolver
  bigip_dns_cache_resolver:
    name: cache_resolver_1
    cache_size: 50000
    dnssec: true
    ignore_ttl: false
    answer_default_zones: true
    use_ipv4: true
    use_ipv6: false
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update DNS cache resolver to allow IPv6
  bigip_dns_cache_resolver:
    name: cache_resolver_1
    use_ipv6: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a DNS cache resolver
  bigip_dns_cache_resolver:
    name: cache_resolver_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



