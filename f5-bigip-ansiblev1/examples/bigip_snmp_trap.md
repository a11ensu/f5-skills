# bigip_snmp_trap


## Description

The `bigip_snmp_trap` module configures SNMP trap destinations and related settings on F5 BIG-IP devices. It allows you to define where traps are sent, which SNMP version and community or user to use, and what types of events generate traps. Use this module to integrate BIG-IP alerts with centralized monitoring platforms and ensure critical events are reported reliably.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the SNMP trap destination configuration. |
| **destination** | **Type:** string<br>**Required:** yes | IP address or hostname of the trap receiver. |
| **port** | **Type:** integer<br>**Default:** 162 | UDP port on which the trap receiver listens. |
| **community** | **Type:** string | SNMP community string used for SNMPv1/v2c traps. |
| **version** | **Choices:** 1, 2c, 3 | SNMP version used for sending traps. |
| **snmpv3\_user** | **Type:** string | SNMPv3 user for authenticated/encrypted traps when `version` is 3. |
| **trap\_types** | **Type:** list | List of trap categories or specific events to enable (e.g. link, system, failover). |
| **partition** | **Default:** Common | Administrative partition for this trap configuration. |
| **state** | **Choices:** present, absent | `present` ensures the trap destination exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the trap configuration managed. |
| **destination** | Final trap receiver address. |
| **port** | Port used to send SNMP traps. |
| **version** | SNMP version configured for this trap destination. |
| **community** | Community string used for traps, if applicable. |
| **snmpv3\_user** | SNMPv3 user associated with this trap configuration, when used. |
| **trap\_types** | List of enabled trap categories or events. |
| **state** | Final state of the trap configuration. |


## Examples


```yaml
- name: Configure SNMPv2c trap destination for monitoring system
  bigip_snmp_trap:
    name: nms_trap
    destination: "10.20.30.40"
    port: 162
    version: 2c
    community: "nms-trap"
    trap_types:
      - system
      - failover
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


