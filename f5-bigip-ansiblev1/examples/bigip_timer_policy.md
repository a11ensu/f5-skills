# bigip_timer_policy


## Description

The `bigip_timer_policy` module manages timer policies on F5 BIG-IP systems. Timer policies define timing behavior for connections, such as idle timeouts, hard timeouts, and other timing-related attributes that affect how long connections or flows are maintained. This module allows you to create, modify, or remove timer policies, enabling fine-grained control over connection lifecycles for applications, security, and performance optimization.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the timer policy to manage. |
| **description** | **Type:** string | User-defined description for the timer policy. |
| **idle_timeout** | **Type:** integer | Idle timeout in seconds before a connection is removed. |
| **hard_timeout** | **Type:** integer | Hard timeout in seconds after which a connection is removed regardless of activity. |
| **app_service** | **Type:** string | Application service to which the timer policy belongs, if any. |
| **partition** | **Default:** Common | Administrative partition where the timer policy resides. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the timer policy exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the timer policy. |
| **description** | Description of the timer policy. |
| **idle_timeout** | Configured idle timeout in seconds. |
| **hard_timeout** | Configured hard timeout in seconds. |
| **partition** | Partition where the timer policy resides. |
| **state** | Final state of the timer policy (`present` or `absent`). |


## Examples


```yaml
- name: Create a timer policy with idle and hard timeouts
  bigip_timer_policy:
    name: web_timer
    description: Timer policy for web applications
    idle_timeout: 300
    hard_timeout: 3600
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Modify idle timeout for an existing timer policy
  bigip_timer_policy:
    name: web_timer
    idle_timeout: 600
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a timer policy
  bigip_timer_policy:
    name: web_timer
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



