# bigip_profile_ftp


## Description

The `bigip_profile_ftp` module manages FTP profiles on F5 BIG-IP systems. FTP profiles control how BIG-IP handles FTP control and data channels, including support for active and passive modes, security options, and inspection of FTP commands. By configuring FTP profiles, administrators can offload FTP connection management, enforce security policies, and ensure compatibility with firewalls and NAT, while simplifying deployment of FTP-based services behind BIG-IP virtual servers.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **data_port** | **Type:** integer | Default data port used for active FTP connections (usually 20). |
| **description** | **Type:** string | User-defined description of the FTP profile. |
| **inherit_parent_profile** | **Choices:** yes, no | Whether to inherit settings from the parent profile. |
| **name** | **Type:** string<br>**Required:** yes | Name of the FTP profile. |
| **parent** | **Type:** string | Parent FTP profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **security** | **Choices:** enabled, disabled | Enables or disables security features such as command checking. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **data_port** | Effective data port used by the profile. |
| **description** | Description set on the profile. |
| **inherit_parent_profile** | Indicates if parent settings are inherited. |
| **name** | Name of the FTP profile managed. |
| **partition** | Partition where the profile is configured. |
| **security** | Indicates if FTP security features are enabled. |


## Examples


```yaml
- name: Create FTP profile for passive FTP service
  bigip_profile_ftp:
    name: ftp_passive_profile
    description: FTP profile for passive mode service
    parent: ftp
    security: enabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Customize FTP data port
  bigip_profile_ftp:
    name: ftp_custom_data_port
    description: FTP profile with custom data port
    data_port: 2121
    security: enabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove FTP profile
  bigip_profile_ftp:
    name: old_ftp_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



