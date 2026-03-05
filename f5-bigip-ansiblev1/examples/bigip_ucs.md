# bigip_ucs


## Description

The `bigip_ucs` module manages User Configuration Set (UCS) files on F5 BIG-IP devices. UCS files contain comprehensive backups of BIG-IP configuration, including system, network, and application objects. This module allows you to create UCS archives, upload UCS files to the device, install them to restore configuration, and delete old archives. Automating UCS handling supports regular backups, rapid disaster recovery, and configuration migration between devices.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the UCS file (without path). |
| **state** | **Choices:** present, absent, installed<br>**Default:** present | `present` creates or uploads a UCS; `installed` installs the UCS; `absent` removes it. |
| **src** | **Type:** string | Local path to a UCS file to upload to the BIG-IP. |
| **no_license** | **Choices:** yes, no | When installing, skip license information from the UCS. |
| **no_platform_check** | **Choices:** yes, no | Skip platform compatibility checks when installing. |
| **passphrase** | **Type:** string | Passphrase used to encrypt or decrypt the UCS file. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the UCS file managed. |
| **state** | Final state (`present`, `installed`, or `absent`). |
| **created** | Boolean indicating if a UCS was created on the device. |
| **uploaded** | Boolean indicating if a UCS file was uploaded. |
| **installed** | Boolean indicating if a UCS file was installed. |


## Examples


```yaml
- name: Create a UCS backup on the BIG-IP
  bigip_ucs:
    name: daily_backup.ucs
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Upload and install a UCS from local file
  bigip_ucs:
    name: migration_config.ucs
    src: /backups/migration_config.ucs
    state: installed
    no_platform_check: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an old UCS file from the BIG-IP
  bigip_ucs:
    name: old_backup.ucs
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



