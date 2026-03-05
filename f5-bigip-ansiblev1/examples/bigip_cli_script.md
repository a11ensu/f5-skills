# bigip_cli_script


## Description

The `bigip_cli_script` module manages tmsh CLI scripts on F5 BIG-IP systems. It allows you to create, update, or delete scripts stored in the BIG-IP configuration, using content from local files or inline definitions. These scripts can automate complex operational tasks, configuration changes, or troubleshooting workflows, and can be invoked manually or via iCall, making them an integral part of advanced automation strategies.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the CLI script on the BIG-IP. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the script is stored. |
| **content** | **Type:** string | Script body to define inline. Mutually exclusive with `src`. |
| **src** | **Type:** path | Local path to a file containing the script body. Mutually exclusive with `content`. |
| **description** | **Type:** string | Descriptive text for the script. |
| **app_service** | **Type:** string | Application service to associate with this script, if using iApps. |
| **args** | **Type:** list | List of argument definitions for the script. |
| **timeout** | **Type:** integer | Timeout in seconds for script execution when invoked. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the script; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the CLI script. |
| **partition** | Partition where the script resides. |
| **description** | Description of the script. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Create CLI script from file
  bigip_cli_script:
    name: cleanup_old_sessions
    partition: Common
    src: files/cleanup_old_sessions.tcl
    description: "Cleanup script for expired sessions"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create CLI script from inline content
  bigip_cli_script:
    name: show_vs_stats
    content: |
      cli script show_vs_stats {
        proc script::run {} {
          tmsh::show ltm virtual
        }
      }
    description: "Show virtual server statistics"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove CLI script
  bigip_cli_script:
    name: cleanup_old_sessions
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

