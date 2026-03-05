# bigip_routedomain


## Description

The `bigip_routedomain` module manages route domains on BIG-IP systems. Route domains provide network virtualization by isolating overlapping IP spaces and routing instances within a single device. This module allows you to create, modify, or delete route domains, configure their IDs, parent-child relationships, VLANs, and strict isolation behavior. It is essential for multi-tenant or complex network designs requiring separate routing tables.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the route domain. |
| **id** | **Type:** integer | Numeric ID of the route domain, used as a suffix in IP addresses (for example, `%1`). |
| **parent** | **Type:** string | Parent route domain name or ID for hierarchical routing. |
| **vlans** | **Type:** list | List of VLANs associated with this route domain. |
| **strict** | **Choices:** yes, no | Whether to enforce strict isolation between route domains. |
| **flow_eviction_policy** | **Type:** string | Name of a flow eviction policy associated with the route domain, if any. |
| **state** | **Choices:** present, absent | `present` creates or updates the route domain; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the route domain managed. |
| **id** | Numeric ID assigned to the route domain. |
| **vlans** | VLANs associated with the route domain. |
| **strict** | Indicates whether strict isolation is enabled. |
| **changed** | Shows whether the route domain configuration was altered. |


## Examples


```yaml
- name: Create route domain 1 with strict isolation
  bigip_routedomain:
    name: rd1
    id: 1
    vlans:
      - vlan_external
      - vlan_internal
    strict: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create child route domain with parent rd1
  bigip_routedomain:
    name: rd2
    id: 2
    parent: rd1
    vlans:
      - vlan_tenant2
    strict: no
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove unused route domain
  bigip_routedomain:
    name: rd_old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



