# bigip_monitor_oracle


## Description

The `bigip_monitor_oracle` module manages Oracle database health monitors on F5 BIG-IP LTM systems. Oracle monitors connect to Oracle database servers using SQL*Net, authenticate with provided credentials, and optionally run SQL queries to verify service availability. This module allows you to create, modify, and remove Oracle monitors, configure usernames, passwords, send/receive strings, intervals, timeouts, and destination settings, enabling robust health checks for Oracle-based applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the Oracle monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing Oracle monitor to inherit settings from. |
| **description** | **Type:** string | Description of the Oracle monitor. |
| **destination** | **Type:** string | IP address and port for Oracle connections, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between Oracle health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the Oracle monitor. |
| **password** | **Type:** string | Password used for Oracle authentication. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String expected in the Oracle response to consider it up. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | SQL query or command to send to the Oracle server. |
| **service** | **Type:** string | Oracle service name or SID to connect to. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the Oracle request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for Oracle health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |
| **username** | **Type:** string | Username used for Oracle authentication. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between Oracle health checks. |
| **timeout** | Timeout configured for Oracle requests. |
| **service** | Oracle service name or SID used in the health check. |
| **send** | SQL query used for monitoring. |
| **recv** | Receive string used to determine health. |


## Examples


```yaml
- name: Create an Oracle monitor
  bigip_monitor_oracle:
    name: oracle_monitor_1
    destination: "203.0.113.20:1521"
    username: "monitor"
    password: "secret"
    service: "ORCL"
    send: "SELECT 1 FROM DUAL"
    recv: "1"
    interval: 10
    timeout: 31
    description: "Oracle simple query health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update Oracle monitor query
  bigip_monitor_oracle:
    name: oracle_monitor_1
    send: "SELECT SYSDATE FROM DUAL"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove Oracle monitor
  bigip_monitor_oracle:
    name: oracle_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



