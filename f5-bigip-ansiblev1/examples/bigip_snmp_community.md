# bigip_snmp_community


## Description

The `bigip_snmp_community` module manages SNMP communities on F5 BIG-IP systems. It allows you to create, modify, or remove communities, define their access permissions (read-only or read-write), and restrict access by source IP addresses or networks. This module helps enforce secure, role-based SNMP access and limits exposure of SNMP data to trusted management hosts only.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the SNMP community. |
| **community** | **Type:** string | Community string used for SNMP queries. If omitted, `name` may be used depending on BIG-IP defaults. |
| **access** | **Choices:** ro, rw | Specifies access level: read-only (`ro`) or read-write (`rw`). |
| **ip\_addresses** | **Type:** list of strings | List of IP addresses or networks allowed to use this community. |
| **oid** | **Type:** string | Optional OID subtree to which this community has access. |
| **partition** | **Default:** Common | Administrative partition in which the SNMP community is configured. |
| **state** | **Choices:** present, absent | `present` ensures the community exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the SNMP community that was managed. |
| **community** | Effective community string after configuration. |
| **access** | Final access level (`ro` or `rw`) for the community. |
| **ip\_addresses** | List of source addresses allowed to use this community. |
| **oid** | OID subtree associated with this community, if any. |
| **state** | Final state of the community (`present` or `absent`). |


## Examples


```yaml
- name: Create read-only SNMP community for NMS
  bigip_snmp_community:
    name: nms_ro
    community: "nms-public"
    access: ro
    ip_addresses:
      - "10.10.10.0/24"
      - "192.168.50.5"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


