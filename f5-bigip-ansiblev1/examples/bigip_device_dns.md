# bigip_device_dns


## Description

The `bigip_device_dns` module manages system-wide DNS configuration on F5 BIG-IP devices. It lets you define name servers, search domains, and DNS options that the BIG-IP uses for name resolution (for example, resolving pool member hostnames, license activation, and external service lookups). With this module you can declaratively configure or update DNS settings, ensuring consistent resolver behavior across devices in automated deployments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **cache** | **Type:** bool | Enables or disables DNS caching on the BIG-IP system resolver. |
| **name_servers** | **Type:** list | List of DNS name server IP addresses to configure on the device. |
| **search** | **Type:** list | List of DNS search domains used when resolving short hostnames. |
| **options** | **Type:** list | Additional resolver options (for example, `ndots:2`). |
| **state** | **Choices:** present | When `present`, ensures the DNS configuration matches the provided parameters. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name_servers** | The configured list of DNS name servers. |
| **search** | The configured DNS search domains. |
| **options** | Any DNS resolver options applied. |
| **cache** | Indicates whether DNS caching is enabled. |


## Examples


```yaml
- name: Configure DNS settings
  bigip_device_dns:
    name_servers:
      - 8.8.8.8
      - 8.8.4.4
    search:
      - example.com
      - corp.example.com
    options:
      - "ndots:2"
    cache: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



