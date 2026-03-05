# bigip_irule


## Description

The `bigip_irule` module manages iRules on F5 BIG-IP devices across different modules such as LTM and GTM. It allows you to create, update, or delete TCL-based iRules that perform advanced traffic steering, inspection, and manipulation. This module supports loading iRule content from files or inline definitions and ensures consistent deployment of traffic logic across environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the iRule. |
| **content** | **Type:** string | Inline TCL iRule definition. |
| **src** | **Type:** path | Path to a local file containing the iRule. |
| **partition** | **Default:** Common | Partition in which to manage the iRule. |
| **state** | **Choices:** present, absent | Whether the iRule should exist or be removed. |
| **verify_signature** | **Type:** bool | If applicable, verify iRule signature when importing. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the iRule. |
| **partition** | Partition where the iRule resides. |
| **content** | Final iRule TCL content on the device (may be truncated). |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create an iRule from a file
  bigip_irule:
    name: http_redirect_irule
    src: files/http_redirect_irule.tcl
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update an iRule using inline content
  bigip_irule:
    name: http_redirect_irule
    content: |
      when HTTP_REQUEST {
        if { [HTTP::host] equals "example.com" } {
          HTTP::redirect "https://www.example.com[HTTP::uri]"
        }
      }
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an iRule
  bigip_irule:
    name: http_redirect_irule
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



