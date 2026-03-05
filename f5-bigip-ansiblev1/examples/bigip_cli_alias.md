# bigip_cli_alias


## Description

The `bigip_cli_alias` module manages command-line interface (CLI) aliases on F5 BIG-IP systems. It allows you to create, modify, or remove both global and per-user aliases that map short commands to longer tmsh or shell commands. This simplifies repetitive operational tasks, standardizes operator shortcuts, and enables consistent CLI behavior across devices when used in automated provisioning workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the CLI alias. |
| **partition** | **Type:** string | Not typically used; aliases are generally global or per-user. |
| **scope** | **Choices:** user, system<br>**Default:** system | Scope of the alias: per-user or system-wide. |
| **user** | **Type:** string | Username for a per-user alias; required when `scope` is `user`. |
| **command** | **Type:** string | The full command that the alias expands to. |
| **description** | **Type:** string | Descriptive text for the alias. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the alias; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the CLI alias. |
| **scope** | Scope of the alias (`user` or `system`). |
| **user** | User for which the alias is configured, when scope is `user`. |
| **command** | Command string associated with the alias. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Create system-wide alias for show ltm virtual
  bigip_cli_alias:
    name: svs
    scope: system
    command: "tmsh show ltm virtual"
    description: "Shortcut to show virtual servers"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create per-user alias for configuration save
  bigip_cli_alias:
    name: cs
    scope: user
    user: admin
    command: "tmsh save sys config"
    description: "Save system configuration"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove system-wide alias
  bigip_cli_alias:
    name: svs
    scope: system
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

