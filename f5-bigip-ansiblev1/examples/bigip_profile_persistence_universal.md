# bigip_profile_persistence_universal


## Description

The `bigip_profile_persistence_universal` module manages universal persistence profiles on F5 BIG-IP devices. Universal persistence uses iRules expressions to extract custom persistence keys from application traffic, allowing highly flexible persistence based on headers, URIs, parameters, or other data. This module lets administrators create or modify universal persistence profiles that reference iRules, enabling advanced affinity logic for complex or proprietary applications that cannot rely on standard cookie or IP-based persistence.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | User-defined description of the universal persistence profile. |
| **match_across_pools** | **Choices:** yes, no | Maintains persistence across all pools on a virtual server. |
| **match_across_services** | **Choices:** yes, no | Maintains persistence across ports or services. |
| **match_across_virtuals** | **Choices:** yes, no | Maintains persistence across multiple virtual servers. |
| **name** | **Type:** string<br>**Required:** yes | Name of the universal persistence profile. |
| **parent** | **Type:** string | Parent universal persistence profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **rule** | **Type:** string | Name of the iRule used to generate persistence keys. |
| **timeout** | **Type:** integer | Persistence timeout in seconds. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **description** | Description set on the profile. |
| **match_across_pools** | Indicates if matching across pools is enabled. |
| **match_across_services** | Indicates if matching across services is enabled. |
| **match_across_virtuals** | Indicates if matching across virtuals is enabled. |
| **name** | Name of the universal persistence profile managed. |
| **partition** | Partition where the profile is configured. |
| **rule** | iRule used for persistence keys. |
| **timeout** | Persistence timeout value. |


## Examples


```yaml
- name: Create universal persistence profile using iRule
  bigip_profile_persistence_universal:
    name: universal_persist_header
    description: Persistence based on custom HTTP header
    parent: universal
    rule: persist_by_header
    timeout: 3600
    match_across_pools: no
    match_across_services: no
    match_across_virtuals: no
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Change timeout for universal persistence
  bigip_profile_persistence_universal:
    name: universal_persist_header
    timeout: 7200
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove universal persistence profile
  bigip_profile_persistence_universal:
    name: old_universal_persist
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



