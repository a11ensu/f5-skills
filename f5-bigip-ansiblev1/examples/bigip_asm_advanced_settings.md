# bigip_asm_advanced_settings


## Description

The `bigip_asm_advanced_settings` module manages advanced configuration options for BIG-IP Application Security Manager (ASM) policies. It allows you to tune low-level security and performance parameters such as header limits, request size thresholds, attack detection toggles, and protocol-specific behaviors. By automating these options, you can align ASM enforcement with application requirements, improve detection accuracy, and standardize security posture across multiple policies and environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the ASM advanced setting to configure (for example, `maximumHttpHeaderSize`). |
| **value** | **Type:** string / integer / boolean | Desired value of the advanced setting. Accepted type and range depend on the specific setting. |
| **policy_name** | **Type:** string<br>**Required:** yes | Name of the ASM policy to which the advanced setting applies. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the ASM policy resides. |
| **state** | **Choices:** present | `present` ensures the advanced setting is configured with the specified value. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the advanced setting that was managed. |
| **value** | Effective value of the advanced setting after the task completes. |
| **policy_name** | ASM policy associated with the advanced setting. |
| **changed** | Indicates whether any change was made to the setting. |


## Examples


```yaml
- name: Set maximum HTTP header size for ASM policy
  bigip_asm_advanced_settings:
    policy_name: webapp_policy
    name: maximumHttpHeaderSize
    value: 32768
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Enable detection of evasions for ASM policy
  bigip_asm_advanced_settings:
    policy_name: webapp_policy
    name: enableEvasionSignatures
    value: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


