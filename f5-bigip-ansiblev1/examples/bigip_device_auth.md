# bigip_device_auth


## Description

The `bigip_device_auth` module manages system-wide device authentication configuration on F5 BIG-IP. It allows you to define how users authenticate to the device (local, LDAP, RADIUS, TACACS, etc.), specify primary and fallback authentication sources, and configure remote role-based access control. By automating these settings, you can standardize administrative access, integrate with centralized identity services, and enforce consistent security policies across BIG-IP appliances.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **auth_source** | **Choices:** local, radius, radius\_fallback, ldap, ldap\_fallback, tacacs, tacacs\_fallback | Primary authentication source for BIG-IP device logins. |
| **fallback** | **Choices:** local, radius, ldap, tacacs | Fallback authentication source if the primary fails or is unavailable. |
| **remote_role** | **Type:** bool<br>**Default:** no | Enables remote role-based access control for authenticated users. |
| **remote_role_default_role** | **Choices:** admin, auditor, guest, operator, resource-admin, manager | Default role assigned when remote role is enabled and no specific mapping is matched. |
| **remote_role_default_partition** | **Type:** string | Default partition for users when remote role is enabled. |
| **remote_role_default_terminal** | **Choices:** none, tmsh, bash | Default terminal type for remote users. |
| **remote_role_info** | **Type:** list | List of remote role mappings used when `remote_role` is enabled. |
| **remote_role_info/role** | **Choices:** admin, auditor, guest, operator, resource-admin, manager | Role to assign when the mapping rule matches. |
| **remote_role_info/partition** | **Type:** string | Partition associated with the role mapping. |
| **remote_role_info/terminal** | **Choices:** none, tmsh, bash | Terminal type associated with the role mapping. |
| **remote_role_info/attribute** | **Type:** string | Attribute name used for matching (for example, `memberOf`). |
| **remote_role_info/value** | **Type:** string | Attribute value to match for this mapping. |
| **state** | **Choices:** present<br>**Default:** present | `present` ensures the device authentication settings match the provided options. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server\_port, validate\_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **auth_source** | Effective primary authentication source. |
| **fallback** | Effective fallback authentication source. |
| **remote_role** | Indicates whether remote role-based access is enabled. |
| **remote_role_info** | List of configured remote role mappings. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Use LDAP as primary auth with local fallback
  bigip_device_auth:
    auth_source: ldap
    fallback: local
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Enable remote roles with default admin access
  bigip_device_auth:
    auth_source: radius
    fallback: local
    remote_role: yes
    remote_role_default_role: admin
    remote_role_default_partition: Common
    remote_role_default_terminal: tmsh
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure remote role mappings based on group membership
  bigip_device_auth:
    auth_source: ldap
    remote_role: yes
    remote_role_info:
      - role: admin
        partition: Common
        terminal: tmsh
        attribute: memberOf
        value: "CN=F5-Admins,OU=Groups,DC=example,DC=com"
      - role: auditor
        partition: Common
        terminal: none
        attribute: memberOf
        value: "CN=F5-Auditors,OU=Groups,DC=example,DC=com"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



