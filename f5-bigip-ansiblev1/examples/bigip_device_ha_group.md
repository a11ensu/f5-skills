# bigip_device_ha_group


## Description

The `bigip_device_ha_group` module manages HA (High Availability) groups on F5 BIG-IP systems. HA groups allow you to define scoring based on trunk, pool, and VIP status to determine which device should be active in a failover pair or cluster. This module lets you create, modify, or remove HA groups, configure their scoring components, and associate them with traffic groups for advanced, metric-based failover decisions.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the HA group. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HA group. |
| **partition** | **Default:** Common | Administrative partition where the HA group resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **score** | **Type:** integer | Base or minimum score for the HA group. |
| **trunks** | **Type:** list | List of trunks and their weights contributing to the HA score. |
| **pools** | **Type:** list | List of pools and their weights contributing to the HA score. |
| **virtual_servers** | **Type:** list | List of virtual servers and their weights contributing to the HA score. |
| **state** | **Choices:** present, absent | `present` ensures the HA group exists; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **score** | Calculated or configured score for the HA group. |
| **trunks** | Trunks that contribute to the HA score. |
| **pools** | Pools that contribute to the HA score. |
| **virtual_servers** | Virtual servers that contribute to the HA score. |


## Examples


```yaml
- name: Create an HA group with trunk and pool scoring
  bigip_device_ha_group:
    name: ha_group_1
    description: "HA group based on trunk and pool availability"
    score: 10
    trunks:
      - name: trunk1
        weight: 5
    pools:
      - name: web_pool
        weight: 10
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



