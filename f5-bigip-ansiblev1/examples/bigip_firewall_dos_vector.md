# bigip_firewall_dos_vector


## Description

The `bigip_firewall_dos_vector` module manages individual attack vector settings within an AFM DoS profile. Attack vectors represent specific DoS signatures or behaviors (for example, SYN flood, DNS query flood) with configurable thresholds and actions. This module allows you to enable or disable vectors, adjust rate limits, detection thresholds, and mitigation policies, providing fine-grained control over DoS protection behavior.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **dos_profile** | **Type:** string<br>**Required:** yes | Name of the DoS profile containing the vector. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DoS attack vector. |
| **partition** | **Default:** Common | Administrative partition of the DoS profile. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, disabled | `present` enables/configures the vector; `disabled` turns it off. |
| **threshold_mode** | **Choices:** manual, fully-automatic | Mode for threshold calculation. |
| **rate_limit** | **Type:** integer | Maximum allowed rate before mitigation starts. |
| **threshold** | **Type:** integer | Detection threshold for the vector. |
| **mitigation_action** | **Choices:** drop, rate-limit, detect-only | Action taken when the vector is triggered. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the configured vector. |
| **state** | Whether the vector is enabled or disabled. |
| **rate_limit** | Configured rate limit. |
| **threshold** | Configured detection threshold. |


## Examples


```yaml
- name: Enable SYN flood vector with manual thresholds
  bigip_firewall_dos_vector:
    dos_profile: dos_profile_web
    name: tcp-syn-flood
    threshold_mode: manual
    threshold: 10000
    rate_limit: 15000
    mitigation_action: drop
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable a DoS vector
  bigip_firewall_dos_vector:
    dos_profile: dos_profile_web
    name: tcp-syn-flood
    state: disabled
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



