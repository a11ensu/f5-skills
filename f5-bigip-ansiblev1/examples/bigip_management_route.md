# bigip_management_route


## Description

The `bigip_management_route` module manages management routes on F5 BIG-IP systems. These routes control how the management interface (MGMT) reaches remote networks for services such as SSH, HTTPS, NTP, and DNS. Using this module, you can create, modify, or delete static routes specific to the management plane without affecting data-plane routing, ensuring secure and predictable out-of-band connectivity.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the management route. |
| **network** | **Type:** string | Destination network in CIDR or IP/mask format (for example, `10.10.0.0/16`). |
| **gateway** | **Type:** string | Next-hop IP address reachable via the management interface. |
| **mtu** | **Type:** integer | MTU for the route, if different from interface default. |
| **description** | **Type:** string | User-defined description for the management route. |
| **state** | **Choices:** present, absent | Whether the management route should exist or be removed. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the management route. |
| **network** | Destination network configured. |
| **gateway** | Gateway associated with the route. |
| **mtu** | Configured MTU for the route, if set. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a management route to monitoring network
  bigip_management_route:
    name: mgmt_to_monitoring
    network: 10.20.0.0/16
    gateway: 192.0.2.1
    description: Route to monitoring and logging systems
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update MTU on management route
  bigip_management_route:
    name: mgmt_to_monitoring
    mtu: 1400
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a management route
  bigip_management_route:
    name: mgmt_to_monitoring
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



