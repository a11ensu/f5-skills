# bigip_monitor_tcp


## Description

The `bigip_monitor_tcp` module manages TCP health monitors on F5 BIG-IP LTM systems. TCP monitors establish TCP connections to servers to verify that the service port is open and responsive, optionally sending and receiving data for more advanced checks. This module allows you to create, modify, and remove TCP monitors, configure send/receive strings, intervals, timeouts, and destination settings, providing flexible and lightweight health checks for TCP-based applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the TCP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing TCP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the TCP monitor. |
| **destination** | **Type:** string | IP address and port for TCP connections, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between TCP health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the TCP monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String expected from the server to consider it up. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | Data sent to the server after establishing the TCP connection. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the TCP connection times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for TCP health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between TCP health checks. |
| **timeout** | Timeout configured for TCP connections. |
| **send** | Data sent to the server during health checks. |
| **recv** | Receive string used to determine health. |


## Examples


```yaml
- name: Create a basic TCP monitor
  bigip_monitor_tcp:
    name: tcp_monitor_1
    destination: "*:8080"
    interval: 5
    timeout: 16
    description: "TCP port 8080 check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a TCP monitor with send/recv
  bigip_monitor_tcp:
    name: tcp_monitor_2
    destination: "*:9000"
    send: "PING\r\n"
    recv: "PONG"
    interval: 10
    timeout: 31
    description: "TCP ping-pong health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove TCP monitor
  bigip_monitor_tcp:
    name: tcp_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



