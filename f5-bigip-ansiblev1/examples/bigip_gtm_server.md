# bigip_gtm_server


## Description

The `bigip_gtm_server` module manages GTM server objects on F5 BIG-IP devices. GTM servers represent physical or logical servers that host virtual servers participating in GTM pools, including BIG-IP systems, generic hosts, and link controllers. Use this module to create, modify, or delete GTM servers, configure their addresses, datacenter, product type, health monitors, and iQuery settings, enabling GTM to accurately track and load balance traffic across distributed application endpoints.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **addresses** | **Type:** list | List of IP addresses associated with the GTM server. |
| **datacenter** | **Type:** string | Name of the GTM datacenter where this server resides. |
| **description** | **Type:** string | Description of the GTM server. |
| **enabled** | **Choices:** yes, no<br>**Default:** yes | Whether the GTM server is enabled for load balancing. |
| **monitor** | **Type:** string | Monitor rule string applied to this GTM server. |
| **name** | **Type:** string<br>**Required:** yes | Name of the GTM server object. |
| **product** | **Choices:** generic-host, bigip, generic-load-balancer, router, host, windows, unknown | Type of device represented by this GTM server. |
| **prober_preference** | **Choices:** inside-datacenter, outside-datacenter, pool, any | Preference for which GTM systems probe this server. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **virtual_servers** | **Type:** list | List of GTM virtual servers associated with this GTM server (definitions include name, address, port, etc). |
| **link** | **Type:** string | Link associated with this server if used for link load balancing. |
| **partition** | **Default:** Common | Partition in which the GTM server is created. |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the GTM server exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | Name of the GTM server. |
| **addresses** | List of IP addresses configured on the server. |
| **datacenter** | Datacenter associated with the server. |
| **product** | Product type of the server. |
| **monitor** | Monitor rule applied to the server. |
| **virtual_servers** | List of GTM virtual servers defined under this server. |


## Examples

```yaml
- name: Create a GTM server representing a BIG-IP device
  bigip_gtm_server:
    name: dc1-bigip
    product: bigip
    datacenter: dc-seattle
    addresses:
      - 10.1.1.10
      - 10.1.1.11
    monitor: "/Common/bigip"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Add virtual servers to a GTM server
  bigip_gtm_server:
    name: dc1-bigip
    virtual_servers:
      - name: app_vs_443
        address: 192.0.2.10
        port: 443
      - name: app_vs_80
        address: 192.0.2.10
        port: 80
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a GTM server
  bigip_gtm_server:
    name: old-bigip
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



