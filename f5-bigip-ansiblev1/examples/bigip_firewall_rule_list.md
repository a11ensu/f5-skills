# bigip_firewall_rule_list


## Description

The `bigip_firewall_rule_list` module manages AFM firewall rule lists on BIG-IP devices. Rule lists are reusable collections of rules that can be referenced by multiple policies or contexts, promoting modular and maintainable firewall configurations. This module allows you to create, update, or delete rule lists and manage their association with policies, without modifying individual rules directly.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the firewall rule list. |
| **name** | **Type:** string<br>**Required:** yes | Name of the rule list. |
| **partition** | **Default:** Common | Administrative partition where the rule list resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **rules** | **Type:** list | Optional inline definition of rules belonging to this list. |
| **state** | **Choices:** present, absent | `present` creates or updates the rule list; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the rule list. |
| **rules** | Rules associated with the rule list. |
| **description** | Description of the rule list. |


## Examples


```yaml
- name: Create an empty firewall rule list
  bigip_firewall_rule_list:
    name: rl_web_common
    description: "Common rules for web applications"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a firewall rule list
  bigip_firewall_rule_list:
    name: rl_web_common
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



