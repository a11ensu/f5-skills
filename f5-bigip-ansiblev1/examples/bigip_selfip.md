# bigip_selfip


## Description

The `bigip_selfip` module manages Self IP addresses on BIG-IP devices. Self IPs represent the BIG-IP’s presence on directly connected VLANs and are used for both data-plane and management-plane communication. This module allows you to create, update, or remove Self IPs, configure their netmasks, VLAN bindings, traffic group assignments, and port lockdown settings to control which services are reachable through each Self IP.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the Self IP object. |
| **address** | **Type:** string | IP address of the Self IP (for example, `192.0.2.10`). |
| **netmask** | **Type:** string | Netmask for the Self IP (for example, `255.255.255.0`). |
| **vlan** | **Type:** string | VLAN to which this Self IP is bound. |
| **traffic_group** | **Type:** string | Traffic group for high availability (for example, `traffic-group-1`). |
| **allow_service** | **Type:** list | List defining port lockdown behavior (for example, `default`, `all`, `none`, or specific services/ports). |
| **floating** | **Choices:** yes, no | Whether the Self IP is floating between devices in a device group. |
| **state** | **Choices:** present, absent | `present` creates or updates the Self IP; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the Self IP managed. |
| **address** | IP address assigned to the Self IP. |
| **vlan** | VLAN associated with the Self IP. |
| **floating** | Indicates whether the Self IP is floating. |
| **allow_service** | Effective port lockdown configuration. |
| **changed** | Shows whether the Self IP configuration was altered. |


## Examples


```yaml
- name: Create non-floating Self IP on external VLAN
  bigip_selfip:
    name: external_self
    address: 198.51.100.10
    netmask: 255.255.255.0
    vlan: vlan_external
    allow_service:
      - default
    floating: no
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create floating Self IP for HA traffic
  bigip_selfip:
    name: ha_floating
    address: 10.0.0.10
    netmask: 255.255.255.0
    vlan: vlan_ha
    traffic_group: traffic-group-1
    allow_service:
      - none
    floating: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove deprecated Self IP
  bigip_selfip:
    name: old_selfip
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



