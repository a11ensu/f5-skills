# bigip_gtm_topology_region


## Description

The `bigip_gtm_topology_region` module manages GTM topology regions on F5 BIG-IP devices. Topology regions are reusable groupings of geographic locations, IP subnets, or other attributes that can be referenced by topology records. Use this module to create, modify, or delete regions, define their constituent subnets or geolocation elements, and simplify the management of complex, location-based DNS routing policies within GTM configurations.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the topology region. |
| **elements** | **Type:** list | List of elements (such as `continent`, `country`, `subnet`) that make up this region. |
| **name** | **Type:** string<br>**Required:** yes | Name of the topology region. |
| **partition** | **Default:** Common | Partition in which the region is managed. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the topology region exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | Name of the topology region. |
| **elements** | List of elements that define the region. |
| **description** | Description associated with the region. |


## Examples

```yaml
- name: Create a topology region for North America
  bigip_gtm_topology_region:
    name: region_na
    elements:
      - "continent NA"
    description: "All North American clients"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a corporate subnet region
  bigip_gtm_topology_region:
    name: region_corp
    elements:
      - "subnet 203.0.113.0/24"
      - "subnet 203.0.114.0/24"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a topology region
  bigip_gtm_topology_region:
    name: old_region
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



