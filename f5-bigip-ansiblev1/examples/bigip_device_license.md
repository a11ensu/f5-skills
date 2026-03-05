# bigip_device_license


## Description

The `bigip_device_license` module manages license installation and activation on F5 BIG-IP devices. It automates the process of applying license keys or license files, handling both online and offline activation workflows. This module can install new licenses, re-activate existing ones, and validate license status, making it suitable for zero-touch provisioning and lifecycle management of BIG-IP instances in automated environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **license_key** | **Type:** string | Base registration key used to license the BIG-IP. |
| **license_file** | **Type:** string | Path to a local license file to upload and install. |
| **state** | **Choices:** present, activated | `present` ensures a license is installed; `activated` forces activation or reactivation. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **accept_eula** | **Type:** bool | When `yes`, automatically accepts the license EULA, if required. |
| **force** | **Type:** bool | When `yes`, forces re-licensing even if a valid license exists. |


## Return Values


| Key | Description |
| --- | --- |
| **status** | Resulting license status after the operation. |
| **license_end_date** | License expiration date, if applicable. |
| **license_key** | Registration key applied to the device. |


## Examples


```yaml
- name: Install and activate BIG-IP license using a registration key
  bigip_device_license:
    license_key: "AAAAA-BBBBB-CCCCC-DDDDD-EEEEE"
    accept_eula: true
    state: activated
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



