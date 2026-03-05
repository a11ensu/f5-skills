# bigip_trunk


## Description

The `bigip_trunk` module manages trunks on F5 BIG-IP systems. Trunks aggregate multiple physical interfaces into a single logical interface for increased bandwidth and redundancy. This module allows you to create, update, or remove trunks, configure member interfaces, set link aggregation control protocol (LACP) options, and adjust related properties. Automating trunk configuration helps standardize link aggregation across devices and simplifies network deployment and maintenance.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the trunk. |
| **interfaces** | **Type:** list | List of physical interfaces to include in the trunk (for example, `1.1`, `1.2`). |
| **lacp** | **Choices:** enabled, disabled, passive, active | Configures LACP mode for the trunk. |
| **lacp_timeout** | **Choices:** short, long | Sets the LACP timeout interval. |
| **link_selection_policy** | **Choices:** auto, maximum-throughput, maximum-address | Policy used to select links within the trunk. |
| **hash** | **Type:** string | Load-balancing hash algorithm used across member links. |
| **description** | **Type:** string | User-defined description for the trunk. |
| **partition** | **Default:** Common | Administrative partition where the trunk resides. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the trunk exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the trunk. |
| **interfaces** | List of member interfaces in the trunk. |
| **lacp** | LACP mode configured on the trunk. |
| **lacp_timeout** | LACP timeout setting. |
| **link_selection_policy** | Policy used for link selection. |
| **hash** | Load-balancing hash algorithm. |
| **description** | Description of the trunk. |
| **partition** | Partition where the trunk resides. |
| **state** | Final state of the trunk (`present` or `absent`). |


## Examples


```yaml
- name: Create a trunk with LACP active
  bigip_trunk:
    name: trunk1
    interfaces:
      - 1.1
      - 1.2
    lacp: active
    lacp_timeout: short
    description: Uplink trunk to core switches
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Modify trunk interfaces
  bigip_trunk:
    name: trunk1
    interfaces:
      - 1.1
      - 1.2
      - 1.3
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a trunk
  bigip_trunk:
    name: trunk1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



