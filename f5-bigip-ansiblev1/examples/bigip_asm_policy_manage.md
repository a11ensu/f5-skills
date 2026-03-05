# bigip_asm_policy_manage


## Description

The `bigip_asm_policy_manage` module manages the lifecycle and properties of ASM security policies on BIG-IP. It allows creating, renaming, exporting, applying, or deleting policies and controlling their enforcement mode (transparent or blocking). The module also handles cloning from templates or existing policies and associating policies with virtual servers, enabling consistent, automated management of web application firewall configurations.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the ASM policy to manage. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the ASM policy resides. |
| **description** | **Type:** string | Free-form description of the policy. |
| **enforcement_mode** | **Choices:** transparent, blocking | Sets the enforcement mode of the policy. |
| **template** | **Type:** string | Name of a built-in or user-defined template to base a new policy on. |
| **parent_policy** | **Type:** string | Name of an existing policy to clone when creating a new one. |
| **virtual_server** | **Type:** string | Name of the virtual server to associate with the policy. |
| **apply_policy** | **Type:** bool<br>**Default:** yes | If yes, applies the policy so that changes take effect. |
| **state** | **Choices:** present, absent, draft | `present` ensures the policy exists and is active; `draft` creates or keeps it in draft; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the ASM policy. |
| **partition** | Partition where the policy resides. |
| **enforcement_mode** | Effective enforcement mode (transparent or blocking). |
| **virtual_server** | Virtual server associated with the policy, if any. |
| **state** | Final state of the policy (`present`, `draft`, or `absent`). |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Create new ASM policy from template in transparent mode
  bigip_asm_policy_manage:
    name: webapp_policy
    partition: Common
    template: Fundamental
    enforcement_mode: transparent
    apply_policy: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Associate existing ASM policy with virtual server
  bigip_asm_policy_manage:
    name: webapp_policy
    virtual_server: vs_webapp_https
    apply_policy: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Switch ASM policy to blocking mode
  bigip_asm_policy_manage:
    name: webapp_policy
    enforcement_mode: blocking
    apply_policy: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove ASM policy
  bigip_asm_policy_manage:
    name: old_policy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

