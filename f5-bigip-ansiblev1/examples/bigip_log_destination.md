# bigip_log_destination


## Description

The `bigip_log_destination` module manages log destinations on F5 BIG-IP devices. It allows you to create, modify, or delete destinations such as remote syslog servers, local log files, IPFIX collectors, or high-speed log (HSL) endpoints. By automating log destinations, you can standardize logging across BIG-IP instances and integrate them with SIEM or monitoring platforms.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the log destination. |
| **type** | **Choices:** syslog, ipfix, splunk, arcsight, remote-high-speed-log, management-port, local-syslog | Type of log destination. |
| **address** | **Type:** string | IP address or hostname of the remote logging endpoint (for network types). |
| **port** | **Type:** integer | Destination port (for example, 514 for syslog). |
| **protocol** | **Choices:** udp, tcp, tls | Transport protocol for network logging. |
| **pool** | **Type:** string | BIG-IP pool used as a log destination (for HSL). |
| **description** | **Type:** string | User-defined description of the log destination. |
| **partition** | **Default:** Common | Partition in which to manage the log destination. |
| **state** | **Choices:** present, absent | Whether the log destination should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the log destination. |
| **type** | Log destination type (for example, syslog). |
| **address** | Configured address of the destination, if applicable. |
| **port** | Configured port of the destination, if applicable. |
| **pool** | Pool used for high-speed logging, if configured. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a remote syslog log destination
  bigip_log_destination:
    name: remote_syslog_1
    type: syslog
    address: 192.0.2.50
    port: 514
    protocol: udp
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a high-speed log destination using a pool
  bigip_log_destination:
    name: hsl_pool_dest
    type: remote-high-speed-log
    pool: /Common/log_pool
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a log destination
  bigip_log_destination:
    name: remote_syslog_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



