# bigip_gtm_monitor_http


## Description

The `bigip_gtm_monitor_http` module manages HTTP GTM monitors on F5 BIG-IP devices. HTTP monitors actively query HTTP services to verify their availability and content, using configurable send and receive strings, status code expectations, and SSL options. Use this module to create, modify, or delete HTTP monitors, control intervals and timeouts, customize HTTP requests, and ensure that GTM only directs DNS traffic to HTTP endpoints that are healthy and responding as expected.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **defaults_from** | **Type:** string | Name of an existing HTTP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the HTTP monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between HTTP health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor marks the resource down if no response is received. |
| **send** | **Type:** string | HTTP request string that the monitor sends (for example, `GET /health HTTP/1.1\r\nHost: example.com\r\n\r\n`). |
| **receive** | **Type:** string | String that must be present in the response for the monitor to mark the resource up. |
| **transparent** | **Choices:** yes, no | When `yes`, the monitor passes traffic through to the resource without modifying the request. |
| **reverse** | **Choices:** yes, no | When `yes`, reverses the monitor logic, marking the resource down when the receive string is found. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTP GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **interval** | Interval configured on the HTTP monitor. |
| **timeout** | Timeout configured on the HTTP monitor. |
| **send** | HTTP request string used by the monitor. |
| **receive** | Expected response content for the monitor to consider the resource up. |
| **reverse** | Indicates if reverse monitoring is enabled. |
| **name** | Name of the HTTP monitor. |


## Examples

```yaml
- name: Create an HTTP GTM monitor for a health endpoint
  bigip_gtm_monitor_http:
    name: http-monitor-api
    defaults_from: /Common/http
    interval: 30
    timeout: 91
    send: "GET /health HTTP/1.1\r\nHost: api.example.com\r\nConnection: close\r\n\r\n"
    receive: "OK"
    description: "HTTP health check for public API"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a reverse HTTP monitor
  bigip_gtm_monitor_http:
    name: http-monitor-reverse
    defaults_from: /Common/http
    send: "GET /status HTTP/1.1\r\nHost: app.example.com\r\n\r\n"
    receive: "ERROR"
    reverse: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an HTTP GTM monitor
  bigip_gtm_monitor_http:
    name: http-monitor-legacy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



