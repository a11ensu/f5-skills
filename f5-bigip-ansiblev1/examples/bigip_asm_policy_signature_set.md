# bigip_asm_policy_signature_set


## Description

The `bigip_asm_policy_signature_set` module manages attack signature sets assigned to ASM policies on BIG-IP. It allows you to enable or disable built-in or custom signature sets, adjust staging behavior, and control how signatures are enforced. By automating signature set configuration, you can align WAF protections with application risk profiles, streamline tuning, and maintain consistent security across multiple policies and environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **policy_name** | **Type:** string<br>**Required:** yes | Name of the ASM policy whose signature sets will be managed. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the ASM policy resides. |
| **signature_sets** | **Type:** list of dictionaries | List of signature set definitions to apply. Each item can define `name`, `enabled`, and `staging`. |
| **signature_sets/name** | **Type:** string<br>**Required:** yes | Name of the signature set (for example, `Generic Detection Signatures`). |
| **signature_sets/enabled** | **Type:** bool<br>**Default:** true | Whether the signature set is enabled on the policy. |
| **signature_sets/staging** | **Type:** bool<br>**Default:** false | Whether signatures in the set should be in staging mode. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the specified signature sets are configured; `absent` removes them from the policy. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **policy_name** | Name of the ASM policy whose signature sets were managed. |
| **partition** | Partition where the policy resides. |
| **signature_sets** | Effective list of signature set configurations applied to the policy. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Enable generic and SQL injection signature sets
  bigip_asm_policy_signature_set:
    policy_name: webapp_policy
    signature_sets:
      - name: Generic Detection Signatures
        enabled: true
        staging: false
      - name: SQL Injection Signatures
        enabled: true
        staging: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable high-risk signatures set on policy
  bigip_asm_policy_signature_set:
    policy_name: webapp_policy
    signature_sets:
      - name: High Risk Signatures
        enabled: false
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove custom signature set from policy
  bigip_asm_policy_signature_set:
    policy_name: webapp_policy
    signature_sets:
      - name: Custom App Signatures
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
