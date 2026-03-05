# bigip_asm_dos_application


## Description

The `bigip_asm_dos_application` module configures application-level DoS protection for BIG-IP ASM. It manages DoS application profiles that apply behavioral and rate-based protections to specific virtual servers or ASM policies. You can enable or disable protections, tune thresholds, configure auto-thresholding, and control mitigation actions such as blocking, challenging, or logging. This module helps automate consistent L7 DoS defenses across your application landscape.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the DoS application profile. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the DoS application profile resides. |
| **application** | **Type:** string | Name of the associated ASM policy or application context (depending on BIG-IP version). |
| **auto_thresholds** | **Choices:** enabled, disabled | Enables automatic threshold calculation based on observed traffic. |
| **bad_actor_detection** | **Choices:** enabled, disabled | Enables per-source bad actor detection and mitigation. |
| **challenge_mode** | **Choices:** none, captcha, javascript | Type of challenge presented to suspected attacking clients. |
| **dos_protection** | **Choices:** enabled, disabled | Enables or disables application DoS protection. |
| **latency_threshold** | **Type:** integer | Latency threshold in milliseconds that triggers DoS mitigation. |
| **rate_threshold** | **Type:** integer | Request rate threshold per second that triggers mitigation. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the DoS application profile; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the DoS application profile. |
| **partition** | Partition where the profile resides. |
| **dos_protection** | Indicates if DoS protection is enabled. |
| **auto_thresholds** | Indicates if automatic thresholding is enabled. |
| **latency_threshold** | Effective latency threshold in milliseconds. |
| **rate_threshold** | Effective request rate threshold per second. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Create DoS application profile with auto thresholds
  bigip_asm_dos_application:
    name: webapp_dos
    application: webapp_policy
    dos_protection: enabled
    auto_thresholds: enabled
    bad_actor_detection: enabled
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure fixed thresholds for DoS application profile
  bigip_asm_dos_application:
    name: webapp_dos
    dos_protection: enabled
    auto_thresholds: disabled
    latency_threshold: 500
    rate_threshold: 1000
    challenge_mode: javascript
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove DoS application profile
  bigip_asm_dos_application:
    name: webapp_dos
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

