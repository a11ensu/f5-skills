# bigip_gtm_monitor_https


## Description

The `bigip_gtm_monitor_https` module manages HTTPS GTM monitors on F5 BIG-IP systems. HTTPS monitors extend HTTP health checks with SSL/TLS support, allowing you to validate both application availability and secure transport. Use this module to configure HTTPS monitors with custom send/receive strings, SSL options, certificates, and ciphers, as well as intervals and timeouts, ensuring GTM only sends DNS traffic to HTTPS endpoints that are reachable and correctly serving secure content.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **defaults_from** | **Type:** string | Name of an existing HTTPS monitor to inherit settings from. |
| **description** | **Type:** string | Description of the HTTPS monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between HTTPS health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor marks the resource down if no response is received. |
| **send** | **Type:** string | HTTPS request string that the monitor sends (HTTP over SSL/TLS). |
| **receive** | **Type:** string | String that must be present in the HTTPS response for the resource to be considered up. |
| **cipherlist** | **Type:** string | OpenSSL-style cipher list specifying allowed ciphers for the monitor. |
| **ssl_profile** | **Type:** string | Name of the client SSL profile the monitor should use, if applicable. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTPS GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **interval** | Interval configured on the HTTPS monitor. |
| **timeout** | Timeout configured on the HTTPS monitor. |
| **send** | HTTPS request string used by the monitor. |
| **receive** | Expected response content for the monitor to consider the resource up. |
| **cipherlist** | Cipher list configured on the monitor. |
| **ssl_profile** | SSL profile used by the monitor, if set. |
| **name** | Name of the HTTPS monitor. |


## Examples

```yaml
- name: Create an HTTPS GTM monitor for a secure API
  bigip_gtm_monitor_https:
    name: https-monitor-api
    defaults_from: /Common/https
    interval: 30
    timeout: 91
    send: "GET /healthz HTTP/1.1\r\nHost: secure-api.example.com\r\nConnection: close\r\n\r\n"
    receive: "healthy"
    cipherlist: "DEFAULT:!LOW:!EXPORT"
    description: "HTTPS health check for secure API"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Use a specific SSL profile in an HTTPS monitor
  bigip_gtm_monitor_https:
    name: https-monitor-custom-ssl
    ssl_profile: /Common/clientssl-secure
    send: "GET /status HTTP/1.1\r\nHost: app.example.com\r\n\r\n"
    receive: "UP"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an HTTPS GTM monitor
  bigip_gtm_monitor_https:
    name: https-monitor-old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



