# bigip_apm_policy_fetch

## Description

The `bigip_apm_policy_fetch` module enables the export and download of Access Policy Manager (APM) policies or access profiles from F5 BIG-IP devices. Administrators can retrieve these configurations and save them to a specified local directory. The module supports exporting either full access policies or specific access profiles by name and partition. It is particularly useful for backing up policy configurations or migrating APM settings between different BIG-IP units. The module communicates via the REST API to perform these operations.

## Parameters

| Parameter | Choices/Defaults | Comments |
| :--- | :--- | :--- |
| **dest** | **Type:** path<br>**Required:** yes | A directory to save the file into. |
| **file** | **Type:** string | The name of the file to be created on the remote device for downloading. If not specified, a random filename is generated. |
| **force** | **Choices:** no, yes<br>**Default:** yes | If `no`, the file will only be transferred if it does not exist in the destination. |
| **name** | **Type:** string<br>**Required:** yes | The name of the APM policy or APM access profile to export. |
| **partition** | **Default:** Common | Device partition which contains the APM policy or APM access profile to export. |
| **provider** | **Type:** dictionary | A dict object containing connection details. |
| **type** | **Choices:** profile\_access, access\_policy<br>**Default:** profile\_access | Specifies the type of item to export from the device. |

## Return Values

| Key | Description |
| :--- | :--- |
| **dest** | Local path to download the exported APM policy. |
| **file** | Name of the exported file on the remote BIG-IP to download. |
| **name** | Name of the APM policy or APM access profile to be exported. |
| **type** | Set to specify the type of item to export. |

## Examples

```yaml
- name: Export APM access profile
  bigip_apm_policy_fetch:
    name: foobar
    file: export_foo
    dest: /root/download
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Export APM access policy
  bigip_apm_policy_fetch:
    name: foobar
    file: export_foo
    dest: /root/download
    type: access_policy
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Export APM access profile, autogenerate name
  bigip_apm_policy_fetch:
    name: foobar
    dest: /root/download
    provider: "{{ bip }}"
  delegate_to: localhost
```

## Tested Playbooks