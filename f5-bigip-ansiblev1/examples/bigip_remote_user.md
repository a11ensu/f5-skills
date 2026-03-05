# bigip_remote_user


## Description

The `bigip_remote_user` module manages default settings for remote user accounts on BIG-IP systems. It controls how accounts authenticated via remote AAA methods (such as LDAP, RADIUS, or TACACS+) are treated when no explicit remote role mapping exists. Using this module, you can define default roles, partitions, and terminal access for such users, ensuring appropriate baseline permissions and consistent behavior across devices.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **default_role** | **Type:** string | Default BIG-IP role assigned to remote users without explicit mappings (for example, `no-access`, `guest`, `operator`, `admin`). |
| **default_partition** | **Type:** string | Default partition for remote users; typically `Common` or `all`. |
| **terminal_access** | **Choices:** tmsh, none | Whether remote users receive terminal (TMSH) access by default. |
| **state** | **Choices:** present, absent | `present` ensures default remote user settings are configured; `absent` resets or removes them. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **default_role** | The default role applied to remote users. |
| **default_partition** | The default partition assigned to remote users. |
| **terminal_access** | Indicates whether remote users get terminal access by default. |
| **changed** | Shows whether the default remote user configuration was modified. |


## Examples


```yaml
- name: Set default remote user role to no-access
  bigip_remote_user:
    default_role: no-access
    default_partition: Common
    terminal_access: none
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Allow remote users operator access to all partitions
  bigip_remote_user:
    default_role: operator
    default_partition: all
    terminal_access: tmsh
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Reset default remote user configuration
  bigip_remote_user:
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



