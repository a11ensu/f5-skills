# bigip_qkview


## Description

The `bigip_qkview` module manages QKview files on BIG-IP devices. QKview is a diagnostic archive containing configuration, logs, and system information used by F5 support for troubleshooting. This module allows you to generate new QKview archives, download them to the Ansible control node, and optionally remove them from the BIG-IP after retrieval. It supports specifying filenames, destinations, and options to control QKview creation behavior.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **filename** | **Type:** string | Name of the QKview file to create on the BIG-IP. If omitted, the system may generate a default name. |
| **dest** | **Type:** string | Local path on the Ansible control node where the QKview file will be saved after download. |
| **force** | **Choices:** yes, no | If `yes`, forces regeneration and download even if a QKview with the same name already exists locally. |
| **delete_from_device** | **Choices:** yes, no | Whether to delete the QKview file from the BIG-IP after successful download. |
| **options** | **Type:** list | Additional QKview command-line options (for example, excluding certain data). |
| **state** | **Choices:** present, absent | `present` generates/downloads a QKview; `absent` removes a specified QKview from the device. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **filename** | Name of the QKview file created on the BIG-IP. |
| **dest** | Local filesystem path where the QKview was stored. |
| **downloaded** | Indicates whether the QKview was downloaded during this task. |
| **deleted_from_device** | Indicates if the QKview file was removed from the BIG-IP. |
| **changed** | Shows whether any actions (create, download, delete) altered state. |


## Examples


```yaml
- name: Generate and download a QKview
  bigip_qkview:
    filename: myqkview.qkview
    dest: /tmp/myqkview.qkview
    delete_from_device: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Generate QKview with extra options and keep on device
  bigip_qkview:
    filename: support_case_12345.qkview
    dest: /var/tmp/support_case_12345.qkview
    options:
      - --exclude-core
    delete_from_device: no
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an old QKview from the device
  bigip_qkview:
    filename: old.qkview
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



