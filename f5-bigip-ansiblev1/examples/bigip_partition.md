# bigip_partition


## Description

The `bigip_partition` module manages administrative partitions on F5 BIG-IP devices. Partitions provide logical separation of configuration objects, enabling multi-tenancy, delegation of administrative control, and isolation of application components. With this module, you can create, update, or remove partitions, set descriptions, and control whether route domains and other objects can be created within them. It is useful for organizing large configurations and aligning BIG-IP objects with organizational or application boundaries.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the partition. |
| **description** | **Type:** string | Text description associated with the partition. |
| **default_route_domain** | **Type:** int | Default route domain ID for the partition. |
| **traffic_group** | **Type:** string | Traffic group associated with the partition, such as `/Common/traffic-group-1`. |
| **device_group** | **Type:** string | Device group for configuration synchronization. |
| **state** | **Choices:** present, absent | Desired state of the partition. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | The name of the partition managed by the module. |
| **description** | The description currently set on the partition. |
| **default_route_domain** | The effective default route domain for the partition. |
| **traffic_group** | Traffic group associated with the partition. |
| **device_group** | Device group configured for the partition. |
| **state** | Final state of the partition (`present` or `absent`). |


## Examples


```yaml
- name: Create an application partition
  bigip_partition:
    name: AppTeamA
    description: "Partition for Application Team A"
    default_route_domain: 0
    traffic_group: /Common/traffic-group-1
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Update partition description
  bigip_partition:
    name: AppTeamA
    description: "Updated description for App Team A"
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove an unused partition
  bigip_partition:
    name: LegacyApps
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



