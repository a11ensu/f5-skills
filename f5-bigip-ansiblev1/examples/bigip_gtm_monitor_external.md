# bigip_gtm_monitor_external


## Description

The `bigip_gtm_monitor_external` module manages external GTM monitors on F5 BIG-IP devices. External monitors use custom scripts (often shell or TCL) to perform complex health checks that are not covered by built-in monitor types. Use this module to create, modify, or delete external monitors, specify the monitoring script, arguments, intervals, and timeouts, and integrate custom application or environment checks into GTM health and load-balancing decisions.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **arguments** | **Type:** string | Arguments that are passed to the external monitor script. |
| **defaults_from** | **Type:** string | Name of an existing external monitor to inherit settings from. |
| **description** | **Type:** string | Description of the external monitor. |
| **interval** | **Type:** integer | Interval, in seconds, between health checks. |
| **timeout** | **Type:** integer | Time, in seconds, before the monitor marks the resource down if no response is received. |
| **manual_resume** | **Choices:** yes, no | When `yes`, requires manual intervention to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the external GTM monitor. |
| **partition** | **Default:** Common | Partition in which the monitor is created. |
| **run** | **Type:** string | Name of the external script file that the monitor runs. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the monitor exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **arguments** | Arguments configured for the external script. |
| **interval** | Interval configured on the external monitor. |
| **timeout** | Timeout configured on the external monitor. |
| **manual_resume** | Whether manual resume is enabled. |
| **run** | Name of the external script used by the monitor. |
| **name** | Name of the external monitor. |


## Examples

```yaml
- name: Create an external GTM monitor using a custom script
  bigip_gtm_monitor_external:
    name: ext-monitor-http-json
    run: ext_http_json_check
    arguments: "--url https://api.example.com/health --expect-code 200"
    interval: 30
    timeout: 91
    description: "External JSON API health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Enable manual resume on an external monitor
  bigip_gtm_monitor_external:
    name: ext-monitor-http-json
    manual_resume: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an external GTM monitor
  bigip_gtm_monitor_external:
    name: ext-monitor-old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



