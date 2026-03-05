# bigip_software_image


## Description

The `bigip_software_image` module manages BIG-IP software image files on the device. It supports uploading images from a local or remote source, verifying their presence, and optionally removing unused images to free disk space. This module is typically used as part of an upgrade workflow to ensure the correct BIG-IP version image is available on the target system before installation.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **image** | **Type:** string<br>**Required:** yes | Name of the BIG-IP software image file on the device (e.g. `BIGIP-15.1.4.iso`). |
| **src** | **Type:** string | Local or remote path/URL from which to upload the image. Required when ensuring presence and image is missing. |
| **checksum** | **Type:** string | Optional checksum for validating the uploaded image. |
| **state** | **Choices:** present, absent | `present` ensures the image is uploaded; `absent` removes it. |
| **timeout** | **Type:** integer | Maximum time in seconds to wait for image upload to complete. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **image** | Name of the software image managed. |
| **uploaded** | Boolean indicating whether an upload occurred during the task. |
| **checksum\_verified** | Boolean indicating if the image checksum was successfully verified. |
| **state** | Final state of the image (`present` or `absent`). |


## Examples


```yaml
- name: Upload BIG-IP software image if not present
  bigip_software_image:
    image: "BIGIP-16.1.4-0.0.12.iso"
    src: "/var/tmp/BIGIP-16.1.4-0.0.12.iso"
    state: present
    timeout: 1800
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


