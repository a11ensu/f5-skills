# bigip_device_trust


## Description

The `bigip_device_trust` module manages trust relationships between BIG-IP devices. Trust is required for forming device clusters and enabling configuration and traffic synchronization. This module automates adding devices into a trust domain, establishing certificates and credentials, and optionally resetting or removing trust, making it essential for building repeatable HA and cluster deployment workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **ca_device** | **Type:** string | Hostname or address of the certificate authority device in the trust domain. |
| **ca_username** | **Type:** string | Username used to authenticate to the CA device. |
| **ca_password** | **Type:** string | Password used to authenticate to the CA device. |
| **device** | **Type:** string | Local device name to add to or manage within the trust domain. |
| **reset_trust** | **Type:** bool | When `yes`, resets existing trust relationships before re-establishing them. |
| **state** | **Choices:** present, absent | `present` ensures the device is part of the trust domain; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **device** | Device that was added to or removed from trust. |
| **trust_domain** | Name or identifier of the trust domain, if available. |
| **state** | Final trust state of the device. |


## Examples


```yaml
- name: Add device to BIG-IP trust domain
  bigip_device_trust:
    ca_device: bigip-a.example.com
    ca_username: admin
    ca_password: secret
    device: bigip-b.example.com
    reset_trust: false
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
