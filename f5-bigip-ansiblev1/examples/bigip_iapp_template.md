# bigip_iapp_template


## Description

The `bigip_iapp_template` module manages TCL iApp templates on F5 BIG-IP systems. It allows you to import new templates, update existing ones, or remove obsolete templates. Templates define reusable application deployment logic, including presentation, implementation, and validation scripts, enabling standardized, automated application provisioning workflows across devices and environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the iApp template to manage. |
| **content** | **Type:** string | Full TCL template body to upload to the BIG-IP. |
| **src** | **Type:** path | Local file path to a TCL iApp template to upload. |
| **state** | **Choices:** present, absent | Whether the template should exist or be removed. |
| **partition** | **Default:** Common | Partition in which the template is stored. |
| **force** | **Type:** bool | If `true`, replaces an existing template with the same name. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the iApp template. |
| **partition** | Partition where the template resides. |
| **content** | Template content as stored on the device (may be truncated). |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Upload an iApp template from file
  bigip_iapp_template:
    name: my_http_iapp
    src: files/my_http_iapp.tmpl
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Replace an existing iApp template with inline content
  bigip_iapp_template:
    name: my_http_iapp
    content: "{{ lookup('file', 'templates/my_http_iapp.tmpl') }}"
    state: present
    force: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an iApp template
  bigip_iapp_template:
    name: my_http_iapp
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



