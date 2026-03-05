# bigip_device_syslog


## Description

The `bigip_device_syslog` module manages system-level syslog settings on F5 BIG-IP devices. It allows you to configure remote syslog servers, log destinations, and facility/level mappings for different subsystems. By using this module, you can centralize BIG-IP logs for security, compliance, and troubleshooting, and enforce consistent logging policies across multiple devices.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **remote_servers** | **Type:** list | List of remote syslog servers with protocol and port configuration. |
| **local_ip** | **Type:** string | Source IP address used for sending syslog messages. |
| **log_level** | **Choices:** debug, info, notice, warn, error, crit, alert, emerg | Default log level for system messages. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present | `present` ensures syslog configuration matches the provided parameters. |


## Return Values


| Key | Description |
| --- | --- |
| **remote_servers** | Remote syslog servers configured on the device. |
| **local_ip** | Source IP used for outgoing syslog messages. |
| **log_level** | Default logging level for system logs. |


## Examples


```yaml
- name: Configure remote syslog servers
  bigip_device_syslog:
    remote_servers:
      - host: 192.0.2.10
        port: 514
        protocol: udp
      - host: 192.0.2.11
        port: 6514
        protocol: tcp
    local_ip: 10.10.10.10
    log_level: info
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



