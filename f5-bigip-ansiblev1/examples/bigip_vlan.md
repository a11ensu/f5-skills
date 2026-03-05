# bigip_vlan


## Description

The `bigip_vlan` module manages VLANs on F5 BIG-IP systems. VLANs segment network traffic by grouping interfaces into broadcast domains. This module allows you to create, modify, or delete VLANs, assign tagged or untagged interfaces, configure MTU, and control related options like fail-safe and CMP hash. Automating VLAN configuration ensures consistent network segmentation and simplifies changes in complex BIG-IP deployments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the VLAN. |
| **partition** | **Default:** Common | Administrative partition where the VLAN resides. |
| **tag** | **Type:** integer | VLAN tag (802.1Q) identifier. |
| **interfaces** | **Type:** list | List of interfaces and tagging mode (tagged/untagged). |
| **mtu** | **Type:** integer | MTU for the VLAN. |
| **fail_safe** | **Choices:** enabled, disabled | Enables VLAN fail-safe detection. |
| **cmp_hash** | **Type:** string | CMP hash configuration for traffic distribution. |
| **description** | **Type:** string | User-defined description for the VLAN. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the VLAN exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the VLAN. |
| **partition** | Partition where the VLAN resides. |
| **tag** | VLAN tag identifier. |
| **interfaces** | Interfaces assigned to the VLAN. |
| **mtu** | MTU configured on the VLAN. |
| **fail_safe** | VLAN fail-safe setting. |
| **cmp_hash** | CMP hash configuration. |
| **description** | Description of the VLAN. |
| **state** | Final state (`present` or `absent`). |


## Examples


```yaml
- name: Create an internal VLAN with tagged interfaces
  bigip_vlan:
    name: internal
    tag: 100
    interfaces:
      - name: 1.1
        tagged: yes
      - name: 1.2
        tagged: yes
    mtu: 1500
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create an external VLAN with untagged interface
  bigip_vlan:
    name: external
    tag: 200
    interfaces:
      - name: 1.3
        tagged: no
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a VLAN
  bigip_vlan:
    name: external
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



