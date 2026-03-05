# bigip_firewall_dos_profile


## Description

The `bigip_firewall_dos_profile` module manages AFM DoS (Denial of Service) profiles on BIG-IP systems. DoS profiles define protection settings against volumetric, protocol, and application-layer attacks, including rate limits, detection thresholds, and mitigation actions. This module lets you create, update, or delete DoS profiles and tune their global settings, which can then be applied to virtual servers or contexts for automated attack mitigation.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **application** | **Type:** dict | Application-level DoS settings, including HTTP-based protections. |
| **description** | **Type:** string | Description of the DoS profile. |
| **dns** | **Type:** dict | DNS DoS protection settings. |
| **ip_intelligence** | **Type:** dict | IP Intelligence configuration for reputation-based blocking. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DoS profile. |
| **network** | **Type:** dict | Network DoS settings for L3/L4 protections. |
| **partition** | **Default:** Common | Administrative partition where the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` creates or updates the profile; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the DoS profile. |
| **application** | Effective application DoS settings. |
| **network** | Effective network DoS settings. |
| **dns** | Effective DNS DoS settings. |


## Examples


```yaml
- name: Create a basic DoS profile
  bigip_firewall_dos_profile:
    name: dos_profile_web
    description: "DoS protection for web applications"
    network:
      enabled: true
    application:
      enabled: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a DoS profile
  bigip_firewall_dos_profile:
    name: dos_profile_web
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



