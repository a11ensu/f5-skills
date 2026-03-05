# bigip_firewall_log_profile_network


## Description

The `bigip_firewall_log_profile_network` module configures the network firewall–specific settings of an AFM log profile. It controls which network firewall events are logged (accepts, drops, rejects), sampling rates, and log destinations. This module is used to fine-tune logging behavior for firewall traffic without affecting other categories such as DoS or IP Intelligence in the same profile.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **log_profile** | **Type:** string<br>**Required:** yes | Name of the AFM log profile to modify. |
| **log_drops** | **Type:** bool | Enables logging of dropped packets. |
| **log_accepts** | **Type:** bool | Enables logging of accepted packets. |
| **log_rejects** | **Type:** bool | Enables logging of rejected packets. |
| **log_translation_fields** | **Type:** bool | Logs NAT/translation-related fields. |
| **partition** | **Default:** Common | Administrative partition of the log profile. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present | `present` ensures network firewall logging settings match the provided parameters. |


## Return Values


| Key | Description |
| --- | --- |
| **log_profile** | Name of the log profile modified. |
| **log_drops** | Indicates whether drop logging is enabled. |
| **log_accepts** | Indicates whether accept logging is enabled. |
| **log_rejects** | Indicates whether reject logging is enabled. |


## Examples


```yaml
- name: Enable drop and reject logging for a log profile
  bigip_firewall_log_profile_network:
    log_profile: fw_log_profile_1
    log_drops: true
    log_rejects: true
    log_accepts: false
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



