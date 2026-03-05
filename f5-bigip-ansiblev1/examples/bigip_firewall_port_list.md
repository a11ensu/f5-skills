# bigip_firewall_port_list


## Description

The `bigip_firewall_port_list` module manages port lists on BIG-IP AFM. Port lists are reusable groups of service ports or ranges that can be referenced by firewall rules and policies, simplifying configuration and improving consistency. This module allows you to create, update, or delete port lists, define TCP/UDP port ranges, and maintain standardized service definitions.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the port list. |
| **name** | **Type:** string<br>**Required:** yes | Name of the port list. |
| **partition** | **Default:** Common | Administrative partition where the port list resides. |
| **ports** | **Type:** list | List of ports or port ranges (for example, `80`, `443`, `1000-2000`). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` creates or updates the port list; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the port list. |
| **ports** | Ports and ranges configured in the list. |
| **description** | Description of the port list. |


## Examples


```yaml
- name: Create a port list for web services
  bigip_firewall_port_list:
    name: web_ports
    description: "HTTP and HTTPS ports"
    ports:
      - 80
      - 443
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a port list
  bigip_firewall_port_list:
    name: old_ports
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



