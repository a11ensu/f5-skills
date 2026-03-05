# bigip_virtual_address


## Description

The `bigip_virtual_address` module manages LTM virtual addresses on F5 BIG-IP devices. A virtual address represents the IP endpoint used by one or more virtual servers. This module allows you to create, modify, or remove virtual addresses, configure properties like ARP/ICMP behavior, route advertisement, and traffic mirroring. Automating virtual address configuration ensures consistent front-end addressing and simplifies changes in load-balanced application environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the virtual address object. |
| **address** | **Type:** string | IP address of the virtual address. |
| **partition** | **Default:** Common | Administrative partition where the virtual address resides. |
| **arp** | **Choices:** enabled, disabled | Controls ARP responses from the virtual address. |
| **icmp_echo** | **Choices:** enabled, disabled | Controls ICMP echo (ping) responses. |
| **traffic_group** | **Type:** string | Traffic group to which the virtual address belongs. |
| **route_advertisement** | **Choices:** enabled, disabled | Controls route advertisement for the virtual address. |
| **connection_limit** | **Type:** integer | Maximum number of concurrent connections allowed. |
| **mask** | **Type:** string | Network mask for the virtual address. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the virtual address exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the virtual address object. |
| **address** | IP address configured. |
| **partition** | Partition where the virtual address resides. |
| **arp** | ARP setting for the virtual address. |
| **icmp_echo** | ICMP echo setting. |
| **traffic_group** | Traffic group assignment. |
| **route_advertisement** | Whether route advertisement is enabled. |
| **connection_limit** | Connection limit configured. |
| **mask** | Network mask configured. |
| **state** | Final state (`present` or `absent`). |


## Examples


```yaml
- name: Create a virtual address with ARP and ICMP enabled
  bigip_virtual_address:
    name: va_web
    address: 203.0.113.10
    arp: enabled
    icmp_echo: enabled
    traffic_group: /Common/traffic-group-1
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable ICMP on an existing virtual address
  bigip_virtual_address:
    name: va_web
    icmp_echo: disabled
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a virtual address
  bigip_virtual_address:
    name: va_web
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



