# bigip_snmp


## Description

The `bigip_snmp` module configures global SNMP settings on F5 BIG-IP devices. It allows you to enable or disable SNMP, set system contact and location, configure allowed SNMP clients, and manage agent behavior such as SNMP versions and security options. Use this module to standardize SNMP configuration across devices and ensure consistent monitoring integration with network management systems.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **agent\_status** | **Choices:** enabled, disabled | Enables or disables the SNMP agent globally. |
| **allowed\_addresses** | **Type:** list of strings | List of IP addresses or networks allowed to query SNMP. If unset, BIG-IP defaults apply. |
| **contact** | **Type:** string | System contact information presented via SNMP, typically an email or role account. |
| **location** | **Type:** string | Physical or logical system location for SNMP identification (e.g. datacenter, rack). |
| **snmpv1** | **Choices:** enabled, disabled | Enables or disables SNMPv1 support. |
| **snmpv2c** | **Choices:** enabled, disabled | Enables or disables SNMPv2c support. |
| **snmpv3** | **Choices:** enabled, disabled | Enables or disables SNMPv3 support. |
| **sys\_name** | **Type:** string | Overrides system name reported via SNMP. If omitted, hostname is used. |
| **trap\_destination** | **Type:** list | Optional list of default trap destinations in global SNMP config. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present | Ensures the specified SNMP configuration is applied. |


## Return Values


| Key | Description |
| --- | --- |
| **agent\_status** | Final status of the SNMP agent after configuration. |
| **allowed\_addresses** | List of IPs or networks allowed to query SNMP after changes. |
| **contact** | Effective SNMP system contact string. |
| **location** | Effective SNMP system location string. |
| **snmp\_versions** | Dictionary indicating enablement of SNMP versions (v1, v2c, v3). |
| **sys\_name** | System name reported via SNMP after configuration. |


## Examples


```yaml
- name: Enable SNMP with restricted clients
  bigip_snmp:
    agent_status: enabled
    contact: "netops@example.com"
    location: "DC1-Rack22-U10"
    allowed_addresses:
      - "10.0.0.0/24"
      - "192.168.100.10"
    snmpv2c: enabled
    snmpv3: enabled
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


