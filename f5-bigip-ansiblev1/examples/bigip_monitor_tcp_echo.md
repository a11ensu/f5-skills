# bigip_monitor_tcp_echo


## Description

The `bigip_monitor_tcp_echo` module manages TCP Echo health monitors on F5 BIG-IP LTM systems. TCP Echo monitors open a TCP connection to a server and expect the server to echo back data, verifying that both connectivity and basic application behavior are functioning. This module allows you to create, modify, and remove TCP Echo monitors, configure intervals, timeouts, and destination settings, offering a simple yet effective way to test TCP echo services or custom echo-based health endpoints.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the TCP Echo monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing TCP Echo monitor to inherit settings from. |
| **description** | **Type:** string | Description of the TCP Echo monitor. |
| **destination** | **Type:** string | IP address and port for TCP Echo connections, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between TCP Echo health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the TCP Echo monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the TCP Echo connection times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for TCP Echo health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between TCP Echo health checks. |
| **timeout** | Timeout configured for TCP Echo connections. |
| **destination** | Destination IP and port used by the monitor. |
| **manual\_resume** | Indicates whether manual resume is enabled. |


## Examples


```yaml
- name: Create a TCP Echo monitor
  bigip_monitor_tcp_echo:
    name: tcp_echo_monitor_1
    destination: "*:7"
    interval: 5
    timeout: 16
    description: "TCP echo port 7 health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update TCP Echo monitor interval
  bigip_monitor_tcp_echo:
    name: tcp_echo_monitor_1
    interval: 10
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove TCP Echo monitor
  bigip_monitor_tcp_echo:
    name: tcp_echo_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



