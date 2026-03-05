# bigip_monitor_mysql


## Description

The `bigip_monitor_mysql` module manages MySQL health monitors on F5 BIG-IP LTM systems. MySQL monitors connect to MySQL database servers, optionally authenticate, and issue simple queries to verify that the service is available and responsive. This module allows you to create, modify, and remove MySQL monitors, configure usernames, passwords, send/receive strings, intervals, timeouts, and destination settings, ensuring accurate health checks for MySQL-backed applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **database** | **Type:** string | Name of the MySQL database to connect to, if required. |
| **debug** | **Type:** string | Debug options for the MySQL monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing MySQL monitor to inherit settings from. |
| **description** | **Type:** string | Description of the MySQL monitor. |
| **destination** | **Type:** string | IP address and port for MySQL connections, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between MySQL health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the MySQL monitor. |
| **password** | **Type:** string | Password used for MySQL authentication. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String expected in the MySQL response to consider it up. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | SQL query or command to send to the MySQL server. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the MySQL request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for MySQL health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |
| **username** | **Type:** string | Username used for MySQL authentication. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between MySQL health checks. |
| **timeout** | Timeout configured for MySQL requests. |
| **database** | Database name used in the health check. |
| **send** | SQL query used for monitoring. |
| **recv** | Receive string used to determine health. |


## Examples


```yaml
- name: Create a MySQL monitor
  bigip_monitor_mysql:
    name: mysql_monitor_1
    destination: "203.0.113.10:3306"
    username: "monitor"
    password: "secret"
    database: "test"
    send: "SELECT 1"
    recv: "1"
    interval: 10
    timeout: 31
    description: "MySQL simple query health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update MySQL monitor query
  bigip_monitor_mysql:
    name: mysql_monitor_1
    send: "SELECT NOW()"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove MySQL monitor
  bigip_monitor_mysql:
    name: mysql_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



