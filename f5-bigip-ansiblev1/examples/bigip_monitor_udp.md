# bigip_monitor_udp


## Description

The `bigip_monitor_udp` module manages UDP health monitors on F5 BIG-IP LTM systems. UDP monitors send UDP packets to servers and optionally evaluate responses to determine service availability on connectionless protocols. This module allows you to create, modify, and remove UDP monitors, configure send/receive strings, intervals, timeouts, and destination settings, providing flexible health checks for DNS, RADIUS, and other UDP-based applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the UDP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing UDP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the UDP monitor. |
| **destination** | **Type:** string | IP address and port for UDP checks, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between UDP health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the UDP monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String expected from the server in response to the UDP payload. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | Data sent to the server as a UDP payload. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the UDP request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for UDP health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between UDP health checks. |
| **timeout** | Timeout configured for UDP responses. |
| **send** | UDP payload sent during health checks. |
| **recv** | Receive string used to determine health. |


## Examples


```yaml
- name: Create a UDP monitor
  bigip_monitor_udp:
    name: udp_monitor_1
    destination: "*:53"
    send: "\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"
    recv: "\x00\x00\x81\x80"
    interval: 5
    timeout: 16
    description: "UDP DNS-like health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update UDP monitor interval
  bigip_monitor_udp:
    name: udp_monitor_1
    interval: 10
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove UDP monitor
  bigip_monitor_udp:
    name: udp_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
