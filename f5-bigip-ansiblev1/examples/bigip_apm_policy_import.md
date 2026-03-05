# bigip_apm_policy_import

## Description

The `bigip_apm_policy_import` module facilitates the import of Access Policy Manager (APM) policies or access profiles into F5 BIG-IP systems from local archive files. It allows administrators to create new policies or overwrite existing ones using the `force` parameter. The module also supports the `reuse_objects` feature, which optimizes configuration by utilizing existing objects on the device instead of those defined in the import file, though care must be taken as configurations may differ. This module is essential for restoring backups, migrating configurations, or deploying standardized APM policies via the REST API.

## Parameters

| Parameter | Choices/Defaults | Comments |
| :--- | :--- | :--- |
| **force** | **Choices:** no, yes<br>**Default:** no | When set to `yes`, any existing policy with the same name will be overwritten by the new import. If a policy does not exist, this setting is ignored. |
| **name** | **Type:** string<br>**Required:** yes | The name of the APM policy or APM access profile to create or override. |
| **partition** | **Default:** Common | Device partition to manage resources on. |
| **provider** | **Type:** dictionary | A dict object containing connection details. |
| **reuse\_objects** | **Choices:** no, yes<br>**Default:** yes | When set to `yes` and objects referred within the policy exist on the BIG-IP, those will be used instead of the objects defined in the policy. Reusing existing objects reduces configuration size. |
| **source** | **Type:** path | Full path to a file to be imported into the BIG-IP APM. |
| **type** | **Choices:** profile\_access, access\_policy, profile\_api\_protection<br>**Default:** profile\_access | Specifies the type of item to import to the device. |

## Return Values

| Key | Description |
| :--- | :--- |
| **force** | Set when overwriting an existing policy or profile. |
| **name** | Name of the APM policy or APM access profile to be created/overwritten. |
| **reuse\_objects** | Set when reusing existing objects on the BIG-IP. |
| **source** | Local path to APM policy file. |
| **type** | Set to specify type of item to export. |

## Examples

```yaml
- name: Import APM profile
  bigip_apm_policy_import:
    name: new_apm_profile
    source: /root/apm_profile.tar.gz
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Import APM policy
  bigip_apm_policy_import:
    name: new_apm_policy
    source: /root/apm_policy.tar.gz
    type: access_policy
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Override existing APM policy
  bigip_apm_policy_import:
    name: new_apm_policy
    source: /root/apm_policy.tar.gz
    force: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Import APM profile without re-using existing configuration objects
  bigip_apm_policy_import:
    name: new_apm_profile
    source: /root/apm_profile.tar.gz
    reuse_objects: no
    provider: "{{ bip }}"
  delegate_to: localhost
```

## Tested Playbooks