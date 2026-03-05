# bigip_device_info


## Description

The `bigip_device_info` module collects detailed information from F5 BIG-IP devices. It can retrieve system facts such as software version, platform, license status, interfaces, VLANs, virtual servers, pools, and many other configuration objects. This module is typically used for inventory, reporting, validation, or as a data source for subsequent tasks in playbooks that dynamically configure BIG-IP based on its current state.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **gather_subset** | **Type:** list | List of information subsets to collect (for example, `system-info`, `virtual-servers`). |
| **include** | **Type:** list | Additional specific objects or paths to include in the output. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **filter** | **Type:** string | Optional filter expression to limit returned objects. |
| **state** | **Choices:** gathered | When `gathered`, collects and returns the requested information. |


## Return Values


| Key | Description |
| --- | --- |
| **ansible_facts** | Dictionary of facts collected from the BIG-IP device. |
| **gather_subset** | The subsets of data that were requested. |
| **queried_objects** | Specific configuration objects returned, if applicable. |


## Examples


```yaml
- name: Gather basic BIG-IP device information
  bigip_device_info:
    gather_subset:
      - system-info
      - software
      - interfaces
    state: gathered
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



