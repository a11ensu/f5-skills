# bigip_gtm_monitor_tcp


## Description

The `bigip_gtm_monitor_tcp` module manages TCP GTM monitors on F5 BIG-IP devices. TCP monitors validate the availability of services by establishing TCP connections and optionally exchanging data, without requiring application-level understanding. Use this module to create, update, or delete TCP monitors, configure send/receive strings, intervals, and timeouts, and ensure GTM accurately reflects the health of TCP-based services such as custom applications, databases, or message queues for DNS load-balancing decisions.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **defaults_from** | **Type:** string | Name of an existing TCP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the TCP monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between TCP health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor marks the resource down if no response is received. |
| **send** | **Type:** string | Optional string sent after the TCP connection is established. |
| **receive** | **Type:** string | String that must be present in the response for the resource to be considered up. |
| **transparent** | **Choices:** yes, no | When `yes`, passes traffic through to the resource without modification. |
| **reverse** | **Choices:** yes, no | When `yes`, reverses the expected monitor result (up when receive string is not found). |
| **name** | **Type:** string<br>**Required:** yes | Name of the TCP GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **interval** | Interval configured on the TCP monitor. |
| **timeout** | Timeout configured on the TCP monitor. |
| **send** | Data string sent after TCP connection establishment, if any. |
| **receive** | Expected response content for the monitor to consider the resource up. |
| **reverse** | Indicates if reverse monitoring is enabled. |
| **name** | Name of the TCP monitor. |


## Examples

```yaml
- name: Create a simple TCP GTM monitor
  bigip_gtm_monitor_tcp:
    name: tcp-monitor-basic
    defaults_from: /Common/tcp
    interval: 30
    timeout: 91
    description: "Basic TCP connectivity check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a TCP monitor with send and receive strings
  bigip_gtm_monitor_tcp:
    name: tcp-monitor-custom
    send: "PING\r\n"
    receive: "PONG"
    interval: 20
    timeout: 60
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a TCP GTM monitor
  bigip_gtm_monitor_tcp:
    name: tcp-monitor-old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



