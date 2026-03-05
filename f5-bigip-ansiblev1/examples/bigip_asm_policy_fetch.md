# bigip_asm_policy_fetch


## Description

The `bigip_asm_policy_fetch` module retrieves ASM security policies from a BIG-IP device and saves them as XML or JSON files on the Ansible controller. This enables you to export policies for backup, version control, or offline editing. The module supports fetching policies by name and partition, and can overwrite existing exported files, making it suitable for integration into CI/CD pipelines and configuration audit workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the ASM policy to fetch. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the ASM policy resides. |
| **dest** | **Type:** path<br>**Required:** yes | Local path on the Ansible controller where the exported policy file will be saved. |
| **file_format** | **Choices:** xml, json<br>**Default:** xml | Format of the exported policy file. |
| **force** | **Type:** bool<br>**Default:** no | If yes, overwrites an existing file at `dest`. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the fetched ASM policy. |
| **partition** | Partition where the policy resides. |
| **dest** | Local path where the policy file was stored. |
| **file_format** | Format of the exported policy file. |
| **changed** | Indicates if the destination file was created or overwritten. |


## Examples


```yaml
- name: Fetch ASM policy in XML format
  bigip_asm_policy_fetch:
    name: webapp_policy
    partition: Common
    dest: /backups/asm/webapp_policy.xml
    file_format: xml
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Fetch ASM policy in JSON format and overwrite existing file
  bigip_asm_policy_fetch:
    name: api_policy
    partition: Common
    dest: /backups/asm/api_policy.json
    file_format: json
    force: yes
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

