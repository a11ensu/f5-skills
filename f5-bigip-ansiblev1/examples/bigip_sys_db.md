# bigip_sys_db


## Description

The `bigip_sys_db` module manages BIG-IP system database (sys db) variables, which control internal system behavior and advanced settings. It allows you to query, set, or reset values for supported database keys, enabling automation of otherwise manual `tmsh`-level configuration. Typical uses include tuning system performance, enabling or disabling features, and aligning device behavior with operational standards. The module can manage single variables or multiple variables in a single play for consistent configuration.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **key** | **Type:** string | The name of the sys db variable to manage (for example, `provision.extramb`). |
| **value** | **Type:** string | The value to assign to the sys db variable. |
| **state** | **Choices:** present, reset<br>**Default:** present | `present` sets the variable to the specified value; `reset` reverts it to its default. |
| **keys** | **Type:** list | A list of key/value pairs for managing multiple sys db variables at once. |
| **partition** | **Default:** Common | Included for consistency; sys db variables are global but may appear in partitioned contexts. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **key** | The sys db key that was modified. |
| **value** | The resulting value of the sys db variable. |
| **old_value** | The previous value of the sys db variable before the change. |
| **changed** | Boolean indicating whether a change was made. |
| **keys** | For bulk operations, a mapping of keys to their resulting values. |


## Examples


```yaml
- name: Set a single sys db variable
  bigip_sys_db:
    key: ui.system.preferences.recording
    value: "true"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Reset a sys db variable to default
  bigip_sys_db:
    key: tm.maxprocesses
    state: reset
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Set multiple sys db variables
  bigip_sys_db:
    keys:
      - key: log.access.control
        value: "enabled"
      - key: ui.advisory.enabled
        value: "true"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



