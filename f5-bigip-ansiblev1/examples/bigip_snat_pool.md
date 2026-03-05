# bigip_snat_pool


## Description

The `bigip_snat_pool` module manages SNAT (Secure Network Address Translation) pools on BIG-IP devices. SNAT pools define one or more translation addresses used to source NAT traffic from internal clients to external networks. This module lets you create, modify, or delete SNAT pools and manage their member addresses, enabling scalable outbound connection handling and IP address conservation in complex network topologies.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the SNAT pool. |
| **members** | **Type:** list | List of IP addresses that form the SNAT pool members. |
| **partition** | **Default:** Common | Administrative partition where the SNAT pool resides. |
| **state** | **Choices:** present, absent | `present` creates or updates the SNAT pool; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the SNAT pool managed. |
| **members** | List of SNAT translation addresses configured in the pool. |
| **changed** | Indicates whether the SNAT pool configuration was altered. |


## Examples


```yaml
- name: Create SNAT pool with two addresses
  bigip_snat_pool:
    name: snat_pool_web
    members:
      - 198.51.100.100
      - 198.51.100.101
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update SNAT pool members
  bigip_snat_pool:
    name: snat_pool_web
    members:
      - 198.51.100.102
      - 198.51.100.103
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove SNAT pool
  bigip_snat_pool:
    name: old_snat_pool
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



