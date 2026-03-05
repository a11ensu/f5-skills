# bigip_firewall_policy


## Description

The `bigip_firewall_policy` module manages AFM firewall policies on BIG-IP devices. Firewall policies are collections of ordered rules applied to contexts such as global, route domain, or virtual servers. This module allows you to create, update, or delete policies, attach log profiles, and control policy options, forming the core of AFM’s access control configuration.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the firewall policy. |
| **log_profile** | **Type:** string | Name of the log profile associated with this policy. |
| **name** | **Type:** string<br>**Required:** yes | Name of the firewall policy. |
| **partition** | **Default:** Common | Administrative partition where the policy resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` creates or updates the policy; `absent` removes it. |
| **strategy** | **Choices:** first-match, best-match | Rule evaluation strategy for the policy. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the firewall policy. |
| **log_profile** | Log profile associated with the policy. |
| **strategy** | Rule evaluation strategy in effect. |


## Examples


```yaml
- name: Create a firewall policy with a log profile
  bigip_firewall_policy:
    name: policy_web
    description: "Web application firewall policy"
    log_profile: fw_log_profile_1
    strategy: first-match
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a firewall policy
  bigip_firewall_policy:
    name: policy_web
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



