# bigip_gtm_monitor_tcp_half_open


## Description

The `bigip_gtm_monitor_tcp_half_open` module manages TCP half-open GTM monitors on F5 BIG-IP devices. TCP half-open monitors perform lightweight health checks by initiating a TCP handshake but not fully establishing the connection, reducing load on monitored services. Use this module to create, tune, or delete half-open monitors, configure intervals and timeouts, and efficiently verify reachability of large numbers of TCP endpoints for GTM DNS load balancing while minimizing impact on backend systems.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **defaults_from** | **Type:** string | Name of an existing TCP half-open monitor to inherit settings from. |
| **description** | **Type:** string | Description of the TCP half-open monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor marks the resource down if no response is detected. |
| **name** | **Type:** string<br>**Required:** yes | Name of the TCP half-open GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **interval** | Interval configured on the TCP half-open monitor. |
| **timeout** | Timeout configured on the TCP half-open monitor. |
| **name** | Name of the TCP half-open monitor. |
| **partition** | Partition where the monitor resides. |


## Examples

```yaml
- name: Create a TCP half-open GTM monitor
  bigip_gtm_monitor_tcp_half_open:
    name: tcp-half-open-monitor-1
    defaults_from: /Common/tcp_half_open
    interval: 30
    timeout: 91
    description: "Lightweight reachability check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Tune interval and timeout for a half-open monitor
  bigip_gtm_monitor_tcp_half_open:
    name: tcp-half-open-monitor-1
    interval: 15
    timeout: 45
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a TCP half-open GTM monitor
  bigip_gtm_monitor_tcp_half_open:
    name: tcp-half-open-monitor-old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
