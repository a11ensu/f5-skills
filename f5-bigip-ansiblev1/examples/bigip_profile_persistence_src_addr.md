# bigip_profile_persistence_src_addr


## Description

The `bigip_profile_persistence_src_addr` module manages source address persistence profiles on F5 BIG-IP systems. Source address persistence tracks client sessions using their source IP address, ensuring subsequent connections are sent to the same pool member. This module enables configuration of timeout values, masks, and other options that determine how long and how specifically client IPs are persisted, which is useful for applications that do not use cookies or require IP-based affinity.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | User-defined description of the source address persistence profile. |
| **mask** | **Type:** string | Network mask applied to the source IP address. |
| **match_across_pools** | **Choices:** yes, no | Maintains persistence across all pools on a virtual server. |
| **match_across_services** | **Choices:** yes, no | Maintains persistence across ports or services. |
| **match_across_virtuals** | **Choices:** yes, no | Maintains persistence across multiple virtual servers. |
| **name** | **Type:** string<br>**Required:** yes | Name of the source address persistence profile. |
| **parent** | **Type:** string | Parent source address persistence profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **timeout** | **Type:** integer | Persistence timeout in seconds. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **description** | Description set on the profile. |
| **mask** | Network mask used for persistence. |
| **match_across_pools** | Indicates if matching across pools is enabled. |
| **match_across_services** | Indicates if matching across services is enabled. |
| **match_across_virtuals** | Indicates if matching across virtuals is enabled. |
| **name** | Name of the source address persistence profile managed. |
| **partition** | Partition where the profile is configured. |
| **timeout** | Persistence timeout value. |


## Examples


```yaml
- name: Create source address persistence profile
  bigip_profile_persistence_src_addr:
    name: srcaddr_persist_webapp
    description: Source address persistence for web app
    parent: source_addr
    timeout: 3600
    mask: 255.255.255.255
    match_across_pools: no
    match_across_services: yes
    match_across_virtuals: no
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Extend persistence timeout
  bigip_profile_persistence_src_addr:
    name: srcaddr_persist_webapp
    timeout: 7200
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove source address persistence profile
  bigip_profile_persistence_src_addr:
    name: old_srcaddr_persist
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



