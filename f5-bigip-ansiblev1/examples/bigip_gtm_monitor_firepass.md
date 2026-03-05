# bigip_gtm_monitor_firepass


## Description

The `bigip_gtm_monitor_firepass` module manages FirePass GTM monitors on F5 BIG-IP systems. FirePass monitors are specialized health checks for F5 FirePass SSL VPN devices, allowing GTM to verify their availability and performance before directing DNS traffic to them. Use this module to create, adjust, or remove FirePass monitors, configure authentication and URIs, and fine-tune intervals and timeouts so that FirePass resources are accurately reflected in GTM load-balancing decisions.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **defaults_from** | **Type:** string | Name of an existing FirePass monitor to inherit settings from. |
| **description** | **Type:** string | Description of the FirePass monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor marks the FirePass device down if no response is received. |
| **username** | **Type:** string | Username used to authenticate to the FirePass device, if required. |
| **password** | **Type:** string | Password used for FirePass authentication. |
| **url** | **Type:** string | URL or path that the monitor requests on the FirePass device. |
| **name** | **Type:** string<br>**Required:** yes | Name of the FirePass GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **interval** | Interval configured on the FirePass monitor. |
| **timeout** | Timeout configured on the FirePass monitor. |
| **url** | URL or path that the monitor checks. |
| **username** | Username used for authentication, if configured. |
| **name** | Name of the FirePass monitor. |


## Examples

```yaml
- name: Create a FirePass GTM monitor with authentication
  bigip_gtm_monitor_firepass:
    name: firepass-monitor-1
    defaults_from: /Common/firepass
    interval: 30
    timeout: 91
    url: "/myvpn/healthcheck"
    username: monitoruser
    password: secretpass
    description: "Monitor for FirePass VPN cluster"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Adjust FirePass monitor timing
  bigip_gtm_monitor_firepass:
    name: firepass-monitor-1
    interval: 20
    timeout: 60
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a FirePass GTM monitor
  bigip_gtm_monitor_firepass:
    name: firepass-monitor-old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



