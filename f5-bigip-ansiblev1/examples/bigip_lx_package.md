# bigip_lx_package


## Description

The `bigip_lx_package` module manages JavaScript iRules LX (LX) packages on F5 BIG-IP devices. It allows you to import, update, or remove Node.js-based LX extensions packaged as RPMs or archives. With this module, you can automate deployment of custom traffic logic, REST extensions, or integrations that leverage the iRules LX framework, ensuring consistent behavior across BIG-IP clusters and environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Logical name of the LX package on the BIG-IP. |
| **src** | **Type:** path | Local path to the LX package file (for example, RPM) to upload. |
| **version** | **Type:** string | Expected version string for the LX package. |
| **state** | **Choices:** present, absent | Whether the LX package should be installed or removed. |
| **force** | **Type:** bool | If `true`, reinstall or overwrite an existing package of the same name. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the LX package on the device. |
| **version** | Installed version of the package. |
| **state** | Final state of the LX package (present/absent). |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Install an LX package from RPM
  bigip_lx_package:
    name: custom_lx_extension
    src: files/custom_lx_extension-1.0.0-0.noarch.rpm
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Reinstall LX package with new version
  bigip_lx_package:
    name: custom_lx_extension
    src: files/custom_lx_extension-1.1.0-0.noarch.rpm
    state: present
    force: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an LX package
  bigip_lx_package:
    name: custom_lx_extension
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



