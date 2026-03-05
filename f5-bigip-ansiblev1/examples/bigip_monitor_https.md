# bigip_monitor_https


## Description

The `bigip_monitor_https` module manages HTTPS health monitors on F5 BIG-IP LTM systems. HTTPS monitors perform SSL/TLS-encrypted HTTP health checks, validating both the HTTP response and, optionally, SSL parameters such as certificates. This module allows you to create, modify, and remove HTTPS monitors, configure send and receive strings, set SSL profiles, define intervals and timeouts, and control options such as manual resume, transparent mode, and specific destinations for secure application health monitoring.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **cipherlist** | **Type:** string | Specifies the list of ciphers to use for SSL connections. |
| **debug** | **Type:** string | Debug options for the HTTPS monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing HTTPS monitor to inherit settings from. |
| **description** | **Type:** string | Description of the HTTPS monitor. |
| **destination** | **Type:** string | IP address and port for HTTPS requests, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between HTTPS health checks. |
| **key** | **Type:** string | Name of the client SSL key used by the monitor, if required. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTPS monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String or pattern expected in the HTTPS response. |
| **recv\_disable** | **Type:** string | Receive string that, when matched, marks the resource down. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | HTTPS request string to send, including method, URI, and headers. |
| **server\_name** | **Type:** string | SNI server name to present during TLS handshake. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the HTTPS request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for HTTPS health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between HTTPS health checks. |
| **timeout** | Timeout configured for HTTPS requests. |
| **send** | HTTPS request string used by the monitor. |
| **recv** | Receive string used to determine health. |
| **server\_name** | SNI server name configured for the monitor. |


## Examples


```yaml
- name: Create an HTTPS monitor
  bigip_monitor_https:
    name: https_monitor_1
    send: "GET /health HTTP/1.1\r\nHost: secure.example.com\r\nConnection: close\r\n\r\n"
    recv: "200 OK"
    interval: 5
    timeout: 16
    server_name: "secure.example.com"
    description: "HTTPS /health check with SNI"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update HTTPS monitor cipher list
  bigip_monitor_https:
    name: https_monitor_1
    cipherlist: "DEFAULT"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove HTTPS monitor
  bigip_monitor_https:
    name: https_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



