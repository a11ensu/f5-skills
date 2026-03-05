# bigip_hostname


## Description

The `bigip_hostname` module manages the system hostname on F5 BIG-IP devices. The hostname identifies the device in administrative interfaces, logs, and network tools. Use this module to set or change the BIG-IP hostname in a consistent, automated manner across environments, ensuring devices follow naming standards and can be easily identified in monitoring and management systems.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **hostname** | **Type:** string<br>**Required:** yes | Fully qualified hostname to assign to the BIG-IP (for example, `bigip01.example.com`). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present<br>**Default:** present | Ensures the BIG-IP hostname matches the specified value. |


## Return Values

| Key | Description |
| --- | --- |
| **hostname** | Hostname configured on the BIG-IP after the task completes. |


## Examples

```yaml
- name: Set BIG-IP hostname
  bigip_hostname:
    hostname: bigip01.dc1.example.com
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Change BIG-IP hostname for DC2 migration
  bigip_hostname:
    hostname: bigip01.dc2.example.com
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
