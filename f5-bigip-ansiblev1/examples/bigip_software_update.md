# bigip_software_update


## Description

The `bigip_software_update` module manages software update settings and operations on F5 BIG-IP devices. It can configure automatic update preferences, check for available updates, and control how and when updates are retrieved from F5. This module is useful for maintaining consistent patch management policies across multiple BIG-IP systems and integrating them into broader compliance workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **auto\_check** | **Choices:** enabled, disabled | Enables or disables automatic checking for software updates. |
| **auto\_install** | **Choices:** enabled, disabled | Controls whether updates are automatically installed when available. |
| **schedule** | **Type:** string | Optional schedule definition for when to perform updates or checks. |
| **proxy** | **Type:** string | Proxy server to use when connecting to F5 update servers. |
| **state** | **Choices:** present | Ensures the specified update configuration is applied. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **auto\_check** | Final state of automatic update checking. |
| **auto\_install** | Final state of automatic installation behavior. |
| **schedule** | Effective schedule for update checks or installations. |
| **proxy** | Proxy settings used for contacting update servers. |


## Examples


```yaml
- name: Configure automatic software update checks
  bigip_software_update:
    auto_check: enabled
    auto_install: disabled
    schedule: "daily@02:00"
    proxy: "http://proxy.example.com:3128"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


