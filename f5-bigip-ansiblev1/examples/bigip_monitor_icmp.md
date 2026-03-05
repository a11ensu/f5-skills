# bigip_monitor_icmp


## Description

The `bigip_monitor_icmp` module manages ICMP health monitors on F5 BIG-IP LTM systems. ICMP monitors send ICMP echo requests (pings) to servers or nodes to verify basic network reachability. This module allows you to create, modify, and remove ICMP monitors, configure intervals and timeouts, and control behavior such as manual resume, transparent mode, and destination settings, providing a simple but effective way to detect network or host failures.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the ICMP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing ICMP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the ICMP monitor. |
| **destination** | **Type:** string | Target IP address for ICMP echo requests. |
| **interval** | **Type:** integer | Interval in seconds between ICMP checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the ICMP monitor. |
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
| **interval** | Interval between ICMP health checks. |
| **timeout** | Timeout configured for ICMP responses. |
| **destination** | Destination IP used by the monitor. |
| **manual\_resume** | Indicates whether manual resume is enabled. |


## Examples


```yaml
- name: Create an ICMP monitor
  bigip_monitor_icmp:
    name: icmp_monitor_1
    destination: "198.51.100.10"
    interval: 5
    timeout: 16
    description: "Basic ICMP reachability monitor"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update ICMP monitor timeout
  bigip_monitor_icmp:
    name: icmp_monitor_1
    timeout: 30
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove ICMP monitor
  bigip_monitor_icmp:
    name: icmp_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



