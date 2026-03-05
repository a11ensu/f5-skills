# bigip_device_httpd


## Description

The `bigip_device_httpd` module manages HTTPD (web configuration utility) settings on F5 BIG-IP systems. It controls how the management GUI is accessed, including listen addresses, allowed IP ranges, SSL/TLS options, and idle timeout. This module lets you enforce security policies for the management interface, such as restricting access to specific networks or disabling HTTP in favor of HTTPS-only access.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **allow** | **Type:** list | List of IP addresses or networks allowed to access the management GUI. |
| **auth_pam_dashboard_timeout** | **Type:** integer | Timeout in seconds for dashboard sessions authenticated via PAM. |
| **description** | **Type:** string | Optional description or comment for HTTPD configuration. |
| **log_level** | **Choices:** debug, info, notice, warn, error, crit, alert, emerg | Logging level for the HTTPD service. |
| **max_clients** | **Type:** integer | Maximum number of concurrent HTTPD clients. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **redirect_http_to_https** | **Type:** bool | When `yes`, redirects HTTP requests to HTTPS. |
| **ssl_port** | **Type:** integer | TCP port for HTTPS access to the management GUI. |
| **state** | **Choices:** present | `present` ensures HTTPD settings match the provided parameters. |


## Return Values


| Key | Description |
| --- | --- |
| **allow** | Networks or hosts allowed to access the GUI. |
| **ssl_port** | Configured HTTPS port for the GUI. |
| **redirect_http_to_https** | Indicates if HTTP-to-HTTPS redirection is enabled. |
| **log_level** | Effective HTTPD log level. |


## Examples


```yaml
- name: Secure the HTTPD management interface
  bigip_device_httpd:
    allow:
      - 10.0.0.0/24
      - 192.168.1.0/24
    redirect_http_to_https: true
    ssl_port: 443
    log_level: notice
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



