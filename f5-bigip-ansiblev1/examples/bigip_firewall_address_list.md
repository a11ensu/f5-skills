# bigip_firewall_address_list


## Description

The `bigip_firewall_address_list` module manages address lists for BIG-IP Advanced Firewall Manager (AFM). Address lists are reusable collections of IP addresses, subnets, or address ranges that can be referenced by firewall rules and policies. Using this module, you can create, update, or remove address lists, maintain consistent object naming, and simplify large firewall configurations by grouping related network objects.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **addresses** | **Type:** list | List of IP addresses, CIDR networks, or address ranges to include. |
| **description** | **Type:** string | User-defined description for the address list. |
| **name** | **Type:** string<br>**Required:** yes | Name of the address list. |
| **partition** | **Default:** Common | Administrative partition where the address list resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` creates or updates the address list; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **addresses** | Final list of addresses configured in the address list. |
| **description** | Description of the address list. |
| **name** | Name of the managed address list. |


## Examples


```yaml
- name: Create an address list for web frontends
  bigip_firewall_address_list:
    name: web_frontend_addrs
    addresses:
      - 192.0.2.10
      - 192.0.2.11
      - 198.51.100.0/24
    description: "Web frontend IPs and subnet"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an address list
  bigip_firewall_address_list:
    name: old_addrs
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



