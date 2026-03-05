# bigip_firewall_log_profile


## Description

The `bigip_firewall_log_profile` module manages AFM firewall logging profiles on BIG-IP systems. Logging profiles define what events are logged (for example, accepts, drops, DoS events) and where logs are sent, such as local syslog or remote servers. This module lets you create, update, or delete log profiles and configure their categories and destinations, enabling detailed visibility into firewall activity.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **dos_protection** | **Type:** dict | Logging settings for DoS protection events. |
| **ip_intelligence** | **Type:** dict | Logging settings for IP Intelligence events. |
| **name** | **Type:** string<br>**Required:** yes | Name of the firewall log profile. |
| **network_firewall** | **Type:** dict | Logging settings for network firewall events. |
| **partition** | **Default:** Common | Administrative partition where the log profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **protocol_inspection** | **Type:** dict | Logging settings for protocol inspection events. |
| **state** | **Choices:** present, absent | `present` creates or updates the log profile; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the log profile. |
| **network_firewall** | Effective settings for firewall event logging. |
| **dos_protection** | Effective settings for DoS logging. |
| **ip_intelligence** | Effective settings for IP Intelligence logging. |


## Examples


```yaml
- name: Create a firewall log profile
  bigip_firewall_log_profile:
    name: fw_log_profile_1
    network_firewall:
      log_drops: true
      log_accepts: false
    dos_protection:
      log_drops: true
      log_summaries: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a firewall log profile
  bigip_firewall_log_profile:
    name: fw_log_profile_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



