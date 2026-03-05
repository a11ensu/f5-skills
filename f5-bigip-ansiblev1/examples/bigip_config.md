# bigip_config


## Description

The `bigip_config` module manages high-level BIG-IP configuration operations such as saving, loading, or rolling back system configuration. It can save the running configuration to disk, load configuration files, and trigger UCS archive creation or restoration. This module is essential for integrating configuration backup, restore, and transactional workflows into Ansible-based automation of BIG-IP platforms.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **save** | **Type:** bool | If yes, saves the running configuration to disk (`save sys config`). |
| **load** | **Type:** bool | If yes, loads the configuration from disk (`load sys config`). |
| **merge** | **Type:** bool | If yes with `load`, merges the configuration instead of replacing it. |
| **reset** | **Type:** bool | If yes, resets the configuration to default factory state (where supported). |
| **ucs** | **Type:** string | Path or name of a UCS archive to create or load. |
| **ucs_state** | **Choices:** present, absent | `present` creates or loads a UCS; `absent` deletes a UCS file. |
| **no_license** | **Type:** bool | When resetting or loading, do not affect license configuration. |
| **no_platform_check** | **Type:** bool | Skip platform compatibility checks when loading UCS. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **save** | Indicates if a save operation was performed. |
| **load** | Indicates if a load operation was performed. |
| **ucs** | Name or path of the UCS archive created or loaded. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Save running configuration to disk
  bigip_config:
    save: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create UCS backup archive
  bigip_config:
    ucs: /var/local/ucs/bigip_backup.ucs
    ucs_state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Restore UCS archive (skip platform check)
  bigip_config:
    ucs: /var/local/ucs/bigip_backup.ucs
    ucs_state: present
    no_platform_check: yes
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

