# bigip_device_traffic_group


## Description

The `bigip_device_traffic_group` module manages traffic groups on F5 BIG-IP systems. Traffic groups define which device in a cluster actively processes a set of floating IPs and virtual servers, supporting failover and load distribution across devices. This module lets you create, modify, or remove traffic groups, configure their failover methods, and associate them with HA groups to implement advanced, policy-driven failover behavior.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **auto_failback_enabled** | **Type:** bool | When `yes`, automatically fails back to a preferred device when it becomes available. |
| **auto_failback_time** | **Type:** integer | Delay in seconds before auto-failback occurs. |
| **description** | **Type:** string | Description of the traffic group. |
| **ha_group** | **Type:** string | Name of an HA group associated with this traffic group. |
| **mac_address** | **Type:** string | Custom MAC address for the floating IPs in this traffic group. |
| **name** | **Type:** string<br>**Required:** yes | Name of the traffic group. |
| **partition** | **Default:** Common | Administrative partition where the traffic group resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the traffic group exists; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **auto_failback_enabled** | Indicates if auto-failback is enabled. |
| **auto_failback_time** | Delay before auto-failback. |
| **ha_group** | HA group associated with the traffic group. |
| **mac_address** | MAC address used by the traffic group. |


## Examples


```yaml
- name: Create a traffic group associated with an HA group
  bigip_device_traffic_group:
    name: traffic-group-1
    description: "Primary application traffic group"
    ha_group: ha_group_1
    auto_failback_enabled: true
    auto_failback_time: 60
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



