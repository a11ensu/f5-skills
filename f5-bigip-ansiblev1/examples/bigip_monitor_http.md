# bigip_monitor_http


## Description

The `bigip_monitor_http` module manages HTTP health monitors on F5 BIG-IP LTM systems. HTTP monitors actively send HTTP requests to servers and evaluate responses based on status codes and content, allowing detailed application-level health checks. This module allows you to create, modify, and remove HTTP monitors, configure send and receive strings, specify HTTP versions and methods, set intervals and timeouts, and customize destination, manual resume, and transparent behavior to match application requirements.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Specifies debug options for the HTTP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing HTTP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the HTTP monitor. |
| **destination** | **Type:** string | IP address and port for HTTP requests, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between HTTP health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTP monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String or pattern expected in the HTTP response body or headers. |
| **recv\_disable** | **Type:** string | Receive string that, when matched, marks the resource down. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | HTTP request string to send, including method, URI, and headers. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the HTTP request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for HTTP health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between HTTP health checks. |
| **timeout** | Timeout configured for HTTP requests. |
| **send** | HTTP request string used by the monitor. |
| **recv** | Receive string used to determine health. |
| **recv\_disable** | Receive string used to mark the resource down. |


## Examples


```yaml
- name: Create an HTTP monitor
  bigip_monitor_http:
    name: http_monitor_1
    send: "GET /health HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
    recv: "200 OK"
    interval: 5
    timeout: 16
    description: "HTTP /health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update HTTP monitor receive disable string
  bigip_monitor_http:
    name: http_monitor_1
    recv_disable: "500"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove HTTP monitor
  bigip_monitor_http:
    name: http_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



