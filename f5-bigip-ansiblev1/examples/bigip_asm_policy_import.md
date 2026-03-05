# bigip_asm_policy_import


## Description

The `bigip_asm_policy_import` module imports ASM security policies from XML or JSON files into a BIG-IP device. It can create new policies or overwrite existing ones, optionally applying them immediately. The module supports specifying policy names, partitions, and whether to retain existing configuration references. This enables repeatable deployment of standardized security policies from version-controlled artifacts across multiple BIG-IP instances.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the ASM policy to create or update on the BIG-IP. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the ASM policy will reside. |
| **src** | **Type:** path<br>**Required:** yes | Local path on the Ansible controller to the policy file (XML or JSON) to import. |
| **file_format** | **Choices:** xml, json | Format of the imported policy file. If omitted, inferred from file extension. |
| **force** | **Type:** bool<br>**Default:** no | If yes, overwrites an existing policy with the same name. |
| **apply_policy** | **Type:** bool<br>**Default:** yes | If yes, applies the policy after import so it becomes active. |
| **retain_signature_sets** | **Type:** bool<br>**Default:** yes | Retains existing signature set references when updating a policy, when supported. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` imports or updates the policy; `absent` removes it from the BIG-IP. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the ASM policy managed on the BIG-IP. |
| **partition** | Partition where the policy resides. |
| **src** | Source file path used for import. |
| **applied** | Indicates whether the policy is applied after import. |
| **state** | Final state of the policy (`present` or `absent`). |
| **changed** | Indicates whether any change was made. |


## Examples


```yaml
- name: Import ASM policy from XML and apply it
  bigip_asm_policy_import:
    name: webapp_policy
    partition: Common
    src: files/webapp_policy.xml
    file_format: xml
    apply_policy: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Import ASM policy from JSON without applying
  bigip_asm_policy_import:
    name: api_policy
    src: files/api_policy.json
    file_format: json
    apply_policy: no
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Replace existing ASM policy from version-controlled XML
  bigip_asm_policy_import:
    name: webapp_policy
    src: files/webapp_policy_new.xml
    file_format: xml
    force: yes
    retain_signature_sets: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove ASM policy from BIG-IP
  bigip_asm_policy_import:
    name: deprecated_policy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

