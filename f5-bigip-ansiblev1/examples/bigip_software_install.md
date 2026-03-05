# bigip_software_install


## Description

The `bigip_software_install` module installs a BIG-IP software image onto a specified volume on the device. It manages the full installation workflow, including selecting the image, target volume, and optional reboot behavior. Use this module to automate upgrades or downgrades and prepare alternate boot locations for staged software rollouts with minimal manual intervention.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **image** | **Type:** string<br>**Required:** yes | Name of the BIG-IP software image already present on the device. |
| **volume** | **Type:** string<br>**Required:** yes | Target boot volume on which to install the software (e.g. `HD1.2`). |
| **reboot** | **Choices:** yes, no<br>**Default:** no | Whether to reboot automatically after installation completes. |
| **install\_config** | **Choices:** yes, no | Whether to copy configuration from current volume to the new one. |
| **state** | **Choices:** installed | Ensures the image is installed on the specified volume. |
| **timeout** | **Type:** integer | Maximum time in seconds to wait for installation to complete. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **image** | Software image installed on the volume. |
| **volume** | Volume where the image was installed. |
| **rebooted** | Boolean indicating whether the device was rebooted. |
| **install\_config** | Boolean indicating if configuration was copied to the new volume. |
| **status** | Final installation status (e.g. `in_progress`, `completed`). |


## Examples


```yaml
- name: Install BIG-IP image on alternate volume without reboot
  bigip_software_install:
    image: "BIGIP-16.1.4-0.0.12.iso"
    volume: "HD1.2"
    reboot: no
    install_config: yes
    state: installed
    timeout: 3600
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


