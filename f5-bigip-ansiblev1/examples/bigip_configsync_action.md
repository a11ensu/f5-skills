# bigip_configsync_action


## Description

The `bigip_configsync_action` module performs configuration synchronization actions on BIG-IP devices in a device group. It can push the local configuration to peers, pull from another device, or trigger incremental sync operations. By automating config sync, this module helps maintain consistent configuration across HA pairs or clusters and integrates BIG-IP redundancy management into broader orchestration workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **device_group** | **Type:** string<br>**Required:** yes | Name of the device group on which to perform the sync action. |
| **direction** | **Choices:** to-group, from-group | Direction of the sync: push local config to group or pull from group. |
| **force_full_load_push** | **Type:** bool | If yes, forces a full configuration load push to the group. |
| **sync_most_recent** | **Type:** bool | If yes, syncs from the device with the most recent configuration when pulling. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **device_group** | Name of the device group targeted by the sync. |
| **direction** | Direction of the sync operation. |
| **changed** | Indicates whether any changes were made (sync was triggered). |


## Examples


```yaml
- name: Push configuration to device group
  bigip_configsync_action:
    device_group: dg_bigip_cluster
    direction: to-group
    force_full_load_push: no
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Force full load push to device group
  bigip_configsync_action:
    device_group: dg_bigip_cluster
    direction: to-group
    force_full_load_push: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Pull most recent configuration from group
  bigip_configsync_action:
    device_group: dg_bigip_cluster
    direction: from-group
    sync_most_recent: yes
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

