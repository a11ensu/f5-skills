# bigip_dns_nameserver


## Description

The `bigip_dns_nameserver` module manages LTM DNS nameserver objects on F5 BIG-IP devices. These objects represent upstream DNS servers to which the BIG-IP forwards queries when acting as a resolver or cache. With this module, you can create, modify, or remove nameservers, configure their addresses, ports, and timeouts, and tune retry behavior to ensure reliable communication with external DNS infrastructure.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **address** | **Type:** string<br>**Required:** yes | IP address of the upstream DNS nameserver. |
| **description** | **Type:** string | Description of the nameserver. |
| **max_concurrent** | **Type:** integer | Maximum concurrent queries allowed to this nameserver. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DNS nameserver object. |
| **partition** | **Default:** Common | Administrative partition where the nameserver resides. |
| **port** | **Type:** integer<br>**Default:** 53 | UDP/TCP port used to query the DNS nameserver. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **route_domain** | **Type:** integer | Route domain ID associated with the nameserver address, if applicable. |
| **state** | **Choices:** present, absent | `present` ensures the nameserver exists; `absent` removes it. |
| **timeout** | **Type:** integer | Timeout in milliseconds or seconds for DNS queries to this nameserver. |
| **use_tcp** | **Type:** bool | When `yes`, uses TCP for queries in addition to or instead of UDP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | The name of the DNS nameserver object. |
| **address** | IP address of the configured nameserver. |
| **port** | Port used to send DNS queries. |
| **timeout** | Effective timeout used for queries to this nameserver. |


## Examples


```yaml
- name: Create a DNS nameserver
  bigip_dns_nameserver:
    name: ns1_google
    address: 8.8.8.8
    port: 53
    timeout: 2
    description: "Google Public DNS"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Change nameserver timeout
  bigip_dns_nameserver:
    name: ns1_google
    timeout: 5
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a DNS nameserver
  bigip_dns_nameserver:
    name: ns1_google
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



