# bigip_remote_role


## Description

The `bigip_remote_role` module manages remote user roles on BIG-IP systems. It allows administrators to define how users authenticated via remote services (such as LDAP, RADIUS, or TACACS+) are mapped to BIG-IP roles and partitions. Using this module, you can create, modify, or delete remote role entries that determine user permissions, including terminal access, partition access, and role-based privileges for managing BIG-IP resources.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the remote role configuration entry. |
| **attribute** | **Type:** string | Remote attribute used to match the user (for example, group or class attribute from the AAA server). |
| **attribute_value** | **Type:** string | Value of the remote attribute that triggers this role mapping. |
| **role** | **Type:** string | BIG-IP user role to assign (for example, `admin`, `resource-admin`, `operator`, `guest`). |
| **partition** | **Type:** string | Administrative partition to which the role applies. Use `all` for access to all partitions. |
| **terminal_access** | **Choices:** tmsh, none | Specifies whether the user has terminal (TMSH) access. |
| **state** | **Choices:** present, absent | `present` creates or updates the remote role; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the remote role object managed. |
| **role** | BIG-IP role assigned to matched remote users. |
| **partition** | Partition or scope of access for the role. |
| **terminal_access** | Indicates whether terminal access is granted. |
| **changed** | Shows whether the remote role configuration was modified. |


## Examples


```yaml
- name: Create remote role for LDAP admins
  bigip_remote_role:
    name: ldap_admins
    attribute: memberOf
    attribute_value: CN=BIGIP-Admins,OU=Groups,DC=example,DC=com
    role: admin
    partition: all
    terminal_access: tmsh
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create remote role for read-only operators
  bigip_remote_role:
    name: ldap_ops
    attribute: memberOf
    attribute_value: CN=BIGIP-Ops,OU=Groups,DC=example,DC=com
    role: operator
    partition: Common
    terminal_access: none
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove unused remote role mapping
  bigip_remote_role:
    name: old_group_mapping
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



