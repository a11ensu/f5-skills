# bigip_monitor_external


## Description

The `bigip_monitor_external` module manages external health monitors on F5 BIG-IP LTM systems. External monitors execute custom scripts on the BIG-IP to determine the health of pool members or nodes. This module allows you to create, modify, and remove external monitors, configure arguments passed to the script, set interval and timeout values, and control whether the monitor is enabled or disabled, enabling flexible and application-specific health checks beyond built-in monitor types.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **args** | **Type:** list | List of arguments to pass to the external monitor script. |
| **debug** | **Type:** string | Specifies the debug options or flags for the external script, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing monitor to inherit default settings from. |
| **description** | **Type:** string | Description of the external monitor. |
| **destination** | **Type:** string | Specifies the IP address and port to which the monitor sends traffic, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a node or pool member up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the external monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **run** | **Type:** string | Specifies the external script name to run as the monitor. |
| **state** | **Choices:** present, absent | When `present`, ensures the monitor exists; when `absent`, removes it. |
| **time\_until\_up** | **Type:** integer | Number of seconds a resource must continuously pass health checks before being marked up. |
| **timeout** | **Type:** integer | Number of seconds before the monitor times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, the monitor uses the client’s source IP address instead of the BIG-IP’s self IP. |
| **up\_interval** | **Type:** integer | Interval in seconds between checks when the resource is already marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **args** | The list of arguments configured for the external monitor. |
| **interval** | The interval between monitor probes. |
| **timeout** | The timeout configured for the monitor. |
| **manual\_resume** | Indicates whether manual resume is enabled. |
| **run** | The external script associated with the monitor. |


## Examples


```yaml
- name: Create an external monitor
  bigip_monitor_external:
    name: ext_check_app
    run: check_app.sh
    args:
      - "--mode=health"
      - "--verbose"
    interval: 10
    timeout: 30
    description: "External script-based health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update external monitor interval and timeout
  bigip_monitor_external:
    name: ext_check_app
    interval: 20
    timeout: 40
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an external monitor
  bigip_monitor_external:
    name: ext_check_app
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



