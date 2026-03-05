# bigip_gtm_monitor_bigip


## Description

The `bigip_gtm_monitor_bigip` module manages BIG-IP type GTM monitors, which are used to monitor the health and availability of other BIG-IP systems in a GTM configuration. These monitors query remote BIG-IP devices using iQuery or related mechanisms to determine status and metrics. Use this module to create, modify, or delete BIG-IP monitors, adjust intervals and timeouts, and control how GTM interprets the health of monitored BIG-IP servers for DNS load-balancing decisions.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **defaults_from** | **Type:** string | Name of an existing BIG-IP monitor to inherit default settings from. |
| **description** | **Type:** string | Description of the monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor declares the target down if no response is received. |
| **name** | **Type:** string<br>**Required:** yes | Name of the BIG-IP GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **probe_timeout** | **Type:** integer | Time, in seconds, that the monitor waits for a probe response before considering it failed. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **interval** | Interval configured on the BIG-IP GTM monitor. |
| **timeout** | Timeout configured on the monitor. |
| **probe_timeout** | Probe timeout configured on the monitor. |
| **name** | Name of the monitor. |
| **partition** | Partition where the monitor resides. |


## Examples

```yaml
- name: Create a BIG-IP GTM monitor with custom interval and timeout
  bigip_gtm_monitor_bigip:
    name: bigip-monitor-1
    defaults_from: /Common/bigip
    interval: 30
    timeout: 90
    description: "Monitor for remote BIG-IP pair"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update BIG-IP GTM monitor timeouts
  bigip_gtm_monitor_bigip:
    name: bigip-monitor-1
    interval: 20
    timeout: 60
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove BIG-IP GTM monitor
  bigip_gtm_monitor_bigip:
    name: bigip-monitor-legacy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



