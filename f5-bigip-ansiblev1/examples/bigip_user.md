# bigip_user


## Description

The `bigip_user` module manages local user accounts and their attributes on F5 BIG-IP devices. It allows you to create, modify, or delete users, set passwords, assign roles and partitions, and control shell access. This module is essential for automating user lifecycle management, enforcing least privilege, and standardizing administrative access across multiple BIG-IP instances in line with organizational security policies.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Username of the BIG-IP account. |
| **password** | **Type:** string | Password for the user account. |
| **full_name** | **Type:** string | Full name or descriptive comment for the user. |
| **partition_access** | **Type:** list | List of partitions and roles the user can access. |
| **shell** | **Choices:** bash, tmsh, none | Shell access level for the user. |
| **state** | **Choices:** present, absent, update_password<br>**Default:** present | `present` ensures the user exists; `absent` removes it; `update_password` updates only the password. |
| **role** | **Type:** string | Global role for the user (for example, `admin`, `operator`). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Username of the account. |
| **full_name** | Full name or description of the user. |
| **role** | Global role assigned to the user. |
| **partition_access** | List of partition access entries. |
| **shell** | Shell access level. |
| **state** | Final state of the user (`present` or `absent`). |


## Examples


```yaml
- name: Create an admin user with bash shell
  bigip_user:
    name: adminuser
    password: "StrongPassw0rd!"
    full_name: "BIG-IP Administrator"
    role: admin
    shell: bash
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create an operator with limited partition access
  bigip_user:
    name: opsuser
    password: "OpsPass123!"
    full_name: "Operations User"
    partition_access:
      - name: Common
        role: operator
    shell: tmsh
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a user
  bigip_user:
    name: olduser
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



