# bigip_device_group_member


## Description

The `bigip_device_group_member` module manages members of BIG-IP device groups. It allows you to add or remove devices from a specified device group, ensuring that only the desired BIG-IP units participate in configuration or traffic synchronization. This module is useful for building automated HA topologies, onboarding new devices into existing sync groups, or removing decommissioned nodes from device clusters.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **device** | **Type:** string<br>**Required:** yes | Name of the BIG-IP device to add or remove from the group. |
| **device_group** | **Type:** string<br>**Required:** yes | Name of the device group to manage membership for. |
| **partition** | **Default:** Common | Administrative partition where the device group resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` adds the device to the group; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **device** | The device that was added or removed. |
| **device_group** | The device group affected. |
| **state** | Final membership state of the device in the group. |


## Examples


```yaml
- name: Add a device to a device group
  bigip_device_group_member:
    device_group: dg_sync_failover
    device: bigip-a.example.com
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



