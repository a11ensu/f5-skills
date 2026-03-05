# bigip_interface


## Description

The `bigip_interface` module manages physical interfaces on F5 BIG-IP devices. It allows you to configure administrative state, speed, duplex, MTU, and flow control settings of network ports. Using this module, you can standardize interface characteristics, disable unused ports, and ensure that BIG-IP interfaces align with upstream switch configurations to avoid mismatches and connectivity issues.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the interface (for example, `1.1`, `1.2`). |
| **enabled** | **Type:** bool | Administrative state of the interface (`true` to enable). |
| **speed** | **Choices:** auto, 10, 100, 1000, 10000, 25000, 40000, 100000 | Interface speed configuration. |
| **duplex** | **Choices:** auto, full, half | Duplex mode of the interface. |
| **mtu** | **Type:** integer | Maximum Transmission Unit for the interface. |
| **flow_control** | **Choices:** none, tx, rx, both | Link-level flow control configuration. |
| **description** | **Type:** string | User-defined description for the interface. |
| **state** | **Choices:** present | Ensures interface is configured as specified. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Interface name that was managed. |
| **enabled** | Final administrative state of the interface. |
| **speed** | Effective speed after configuration. |
| **duplex** | Effective duplex mode after configuration. |
| **mtu** | Effective MTU value. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Enable interface 1.1 at 10G full duplex
  bigip_interface:
    name: 1.1
    enabled: true
    speed: 10000
    duplex: full
    mtu: 1500
    description: Uplink to core switch
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable unused interface 1.3
  bigip_interface:
    name: 1.3
    enabled: false
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure flow control on interface 1.2
  bigip_interface:
    name: 1.2
    flow_control: both
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



