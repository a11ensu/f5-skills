# bigip_device_ntp


## Description

The `bigip_device_ntp` module manages NTP (Network Time Protocol) settings on F5 BIG-IP devices. Accurate time is critical for logging, SSL validation, and synchronization across HA pairs. This module lets you define NTP servers, configure timezone, and control whether NTP is enabled, ensuring consistent and reliable timekeeping across managed BIG-IP systems.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **servers** | **Type:** list | List of NTP server hostnames or IP addresses to configure. |
| **timezone** | **Type:** string | System timezone identifier (for example, `UTC`, `America/New_York`). |
| **state** | **Choices:** present | When `present`, ensures NTP configuration matches the provided parameters. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **servers** | The configured list of NTP servers. |
| **timezone** | The effective system timezone. |


## Examples


```yaml
- name: Configure NTP servers and timezone
  bigip_device_ntp:
    servers:
      - 0.pool.ntp.org
      - 1.pool.ntp.org
    timezone: "UTC"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



