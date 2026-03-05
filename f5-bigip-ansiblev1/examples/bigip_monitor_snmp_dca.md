# bigip_monitor_snmp_dca


## Description

The `bigip_monitor_snmp_dca` module manages SNMP Data Collecting Agent (DCA) monitors on F5 BIG-IP systems. SNMP DCA monitors query SNMP-enabled devices for specific OIDs and evaluate returned values to determine health or performance status. This module allows you to create, modify, and remove SNMP DCA monitors, configure agents, OIDs, community strings, intervals, timeouts, and threshold values, enabling network and device health monitoring through SNMP.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **agent** | **Type:** string | SNMP agent address or profile used by the monitor. |
| **community** | **Type:** string | SNMP community string for authentication (v1/v2c). |
| **debug** | **Type:** string | Debug options for the SNMP DCA monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing SNMP DCA monitor to inherit settings from. |
| **description** | **Type:** string | Description of the SNMP DCA monitor. |
| **interval** | **Type:** integer | Interval in seconds between SNMP polls. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the SNMP DCA monitor. |
| **oid** | **Type:** string | SNMP OID that the monitor queries. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the SNMP request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for SNMP polls. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |
| **version** | **Choices:** 1, 2c, 3 | SNMP protocol version used by the monitor. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between SNMP polls. |
| **timeout** | Timeout configured for SNMP requests. |
| **oid** | OID queried by the monitor. |
| **agent** | SNMP agent configured for the monitor. |
| **version** | SNMP version used. |


## Examples


```yaml
- name: Create an SNMP DCA monitor
  bigip_monitor_snmp_dca:
    name: snmp_dca_monitor_1
    agent: "198.51.100.40"
    community: "public"
    version: "2c"
    oid: ".1.3.6.1.2.1.1.3.0"
    interval: 30
    timeout: 91
    description: "SNMP sysUpTime health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update SNMP DCA monitor OID
  bigip_monitor_snmp_dca:
    name: snmp_dca_monitor_1
    oid: ".1.3.6.1.2.1.2.2.1.8.1"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove SNMP DCA monitor
  bigip_monitor_snmp_dca:
    name: snmp_dca_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



