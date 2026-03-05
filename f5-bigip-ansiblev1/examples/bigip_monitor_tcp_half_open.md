# bigip_monitor_tcp_half_open


## Description

The `bigip_monitor_tcp_half_open` module manages TCP Half-Open health monitors on F5 BIG-IP LTM systems. TCP Half-Open monitors initiate a TCP handshake to verify that a service port is listening, but do not complete the full connection, reducing resource usage on the target. This module allows you to create, modify, and remove TCP Half-Open monitors, configure intervals, timeouts, and destination settings, providing efficient port-level health checks for high-scale environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the TCP Half-Open monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing TCP Half-Open monitor to inherit settings from. |
| **description** | **Type:** string | Description of the TCP Half-Open monitor. |
| **destination** | **Type:** string | IP address and port for TCP Half-Open checks, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between TCP Half-Open health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the TCP Half-Open monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the TCP Half-Open attempt times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for TCP Half-Open health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between TCP Half-Open health checks. |
| **timeout** | Timeout configured for TCP Half-Open attempts. |
| **destination** | Destination IP and port used by the monitor. |
| **manual\_resume** | Indicates whether manual resume is enabled. |


## Examples


```yaml
- name: Create a TCP Half-Open monitor
  bigip_monitor_tcp_half_open:
    name: tcp_half_open_monitor_1
    destination: "*:443"
    interval: 5
    timeout: 16
    description: "TCP half-open port 443 check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update TCP Half-Open monitor timeout
  bigip_monitor_tcp_half_open:
    name: tcp_half_open_monitor_1
    timeout: 30
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove TCP Half-Open monitor
  bigip_monitor_tcp_half_open:
    name: tcp_half_open_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



