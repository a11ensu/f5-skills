# bigip_imish_config


## Description

The `bigip_imish_config` module manages advanced routing configuration sections on F5 BIG-IP systems via the imish (ZebOS/FRR-like) shell. It enables automated configuration of dynamic routing protocols such as BGP, OSPF, and RIP by pushing or removing configuration fragments. This module is useful for maintaining consistent routing policies across multiple BIG-IP devices and integrating them into larger routed networks.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **lines** | **Type:** list | List of imish configuration lines to apply in order. |
| **parents** | **Type:** list | List of parent configuration commands to enter before applying `lines`. |
| **match** | **Choices:** line, none, exact | Control how existing configuration is compared to desired lines. |
| **replace** | **Choices:** line, block | Whether to replace individual lines or entire blocks. |
| **multiline_delimiter** | **Type:** string | Delimiter for multiline configs, if required. |
| **save** | **Type:** bool | If `true`, saves the running config to startup. |
| **state** | **Choices:** present, absent | Whether lines should be present or removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **commands** | List of imish commands sent to the device. |
| **updates** | List of configuration changes applied. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Configure BGP neighbor in imish
  bigip_imish_config:
    parents:
      - router bgp 65000
    lines:
      - neighbor 192.0.2.10 remote-as 65010
      - neighbor 192.0.2.10 description Branch1
    state: present
    save: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an OSPF network statement
  bigip_imish_config:
    parents:
      - router ospf
    lines:
      - network 10.10.0.0/16 area 0.0.0.0
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Replace an entire BGP address-family block
  bigip_imish_config:
    parents:
      - router bgp 65000
      - address-family ipv4 unicast
    lines:
      - network 192.0.2.0/24
      - network 198.51.100.0/24
    replace: block
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



