# bigip_file_copy


## Description

The `bigip_file_copy` module manages files in BIG-IP datastores such as `/var/tmp`, UCS, iFile, and SSL-related directories. It allows you to upload files from the Ansible controller to the BIG-IP or download files from the device to the controller. This module supports idempotent file deployment for configuration artifacts like SSL certificates, iRules, UCS archives, and custom scripts, ensuring that required files are present and up to date.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **dest** | **Type:** string<br>**Required:** yes | Destination path on the BIG-IP or local controller, depending on direction. |
| **direction** | **Choices:** upload, download<br>**Default:** upload | Direction of file transfer: `upload` (controller to BIG-IP) or `download` (BIG-IP to controller). |
| **file** | **Type:** string | Local path to the source file on the controller when uploading. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the file exists at destination; `absent` removes it from BIG-IP. |
| **validate_checksum** | **Type:** bool | When `yes`, uses checksums to avoid unnecessary transfers. |


## Return Values


| Key | Description |
| --- | --- |
| **dest** | Destination path where the file resides after the task. |
| **direction** | Direction of the transfer performed. |
| **changed** | Indicates whether a file transfer or deletion occurred. |


## Examples


```yaml
- name: Upload an SSL certificate to BIG-IP
  bigip_file_copy:
    file: files/server.crt
    dest: /config/ssl/ssl.crt/server.crt
    direction: upload
    state: present
    validate_checksum: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Download a UCS archive from BIG-IP
  bigip_file_copy:
    dest: backups/bigip-ucs.ucs
    direction: download
    file: /var/local/ucs/bigip-ucs.ucs
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a temporary file from BIG-IP
  bigip_file_copy:
    dest: /var/tmp/old_script.sh
    state: absent
    direction: upload
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
