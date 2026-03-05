# bigip_device_group


## Description

The `bigip_device_group` module manages device groups on F5 BIG-IP systems. Device groups define sets of BIG-IP devices that participate in configuration or traffic synchronization, such as Sync-Failover or Sync-Only groups. This module lets you create, modify, or remove device groups, control their type and sync behavior, and set auto-sync and network failover options to support high availability and centralized configuration management.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **auto_sync** | **Type:** bool | When `yes`, automatically synchronizes configuration changes across the group. |
| **description** | **Type:** string | Description of the device group. |
| **full_sync** | **Type:** bool | When `yes`, always performs full configuration syncs instead of incremental ones. |
| **name** | **Type:** string<br>**Required:** yes | Name of the device group. |
| **network_failover** | **Type:** bool | Enables or disables network failover for this device group. |
| **partition** | **Default:** Common | Administrative partition where the device group resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **save_on_auto_sync** | **Type:** bool | When `yes`, saves the configuration automatically after auto-sync. |
| **state** | **Choices:** present, absent | `present` ensures the device group exists; `absent` removes it. |
| **type** | **Choices:** sync-failover, sync-only | Type of device group to create or manage. |


## Return Values


| Key | Description |
| --- | --- |
| **type** | The type of the device group (sync-failover or sync-only). |
| **auto_sync** | Indicates whether auto-sync is enabled. |
| **network_failover** | Indicates whether network failover is enabled. |
| **full_sync** | Indicates whether full sync is enforced. |


## Examples


```yaml
- name: Create a Sync-Failover device group
  bigip_device_group:
    name: dg_sync_failover
    type: sync-failover
    auto_sync: true
    network_failover: true
    save_on_auto_sync: true
    description: "Primary HA sync-failover group"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



