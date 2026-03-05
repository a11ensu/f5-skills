# bigip_ucs_fetch


## Description

The `bigip_ucs_fetch` module retrieves UCS files from remote BIG-IP devices to the local Ansible control machine. It supports copying one or more UCS archives, enabling centralized backup storage, offline analysis, or archival. You can specify the remote UCS path, local destination directory, and optional file permissions. Automating UCS retrieval ensures consistent backup workflows and simplifies integration with external backup or compliance systems.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **src** | **Type:** string<br>**Required:** yes | Path to the UCS file on the BIG-IP device. |
| **dest** | **Type:** string<br>**Required:** yes | Local directory or file path where the UCS will be stored. |
| **flat** | **Choices:** yes, no | When copying multiple files, controls whether the destination is flattened. |
| **mode** | **Type:** string | File mode (permissions) to set on the fetched UCS. |
| **validate_checksum** | **Choices:** yes, no | Whether to validate checksums after transfer. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **dest** | Local path where the UCS file was stored. |
| **src** | Remote path of the UCS file. |
| **checksum** | Checksum of the fetched UCS file. |
| **changed** | Boolean indicating if a file was transferred. |


## Examples


```yaml
- name: Fetch a UCS file to local backup directory
  bigip_ucs_fetch:
    src: /var/local/ucs/daily_backup.ucs
    dest: /backups/bigip01/
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Fetch a UCS file with specific permissions
  bigip_ucs_fetch:
    src: /var/local/ucs/migration_config.ucs
    dest: /backups/migration_config.ucs
    mode: "0600"
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



