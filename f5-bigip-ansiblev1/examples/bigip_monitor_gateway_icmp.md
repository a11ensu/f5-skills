# bigip_monitor_gateway_icmp


## Description

The `bigip_monitor_gateway_icmp` module manages gateway ICMP monitors on F5 BIG-IP LTM systems. Gateway ICMP monitors verify reachability of upstream network gateways or routers using ICMP echo requests, helping detect network path failures rather than just server failures. This module allows you to create, modify, and remove gateway ICMP monitors, configure intervals and timeouts, and control behavior such as manual resume, transparent mode, and destination settings for more advanced network health monitoring.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Specifies debug options for the monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing gateway ICMP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the gateway ICMP monitor. |
| **destination** | **Type:** string | IP address for ICMP probes, usually the gateway IP. |
| **interval** | **Type:** integer | Interval in seconds between ICMP echo requests. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual intervention to mark the resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the gateway ICMP monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the ICMP request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for ICMP probes. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | The configured interval between ICMP checks. |
| **timeout** | The timeout value for ICMP responses. |
| **destination** | The destination IP used by the monitor. |
| **manual\_resume** | Indicates if manual resume is enabled. |


## Examples


```yaml
- name: Create a gateway ICMP monitor
  bigip_monitor_gateway_icmp:
    name: gw_icmp_monitor_1
    destination: "192.0.2.1"
    interval: 5
    timeout: 16
    description: "Gateway reachability monitor"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update gateway ICMP monitor timeout
  bigip_monitor_gateway_icmp:
    name: gw_icmp_monitor_1
    timeout: 30
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a gateway ICMP monitor
  bigip_monitor_gateway_icmp:
    name: gw_icmp_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



