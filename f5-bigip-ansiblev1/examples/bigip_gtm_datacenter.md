# bigip_gtm_datacenter


## Description

The `bigip_gtm_datacenter` module manages GTM (DNS) datacenter objects on F5 BIG-IP devices. It allows you to create, modify, or remove datacenters that represent logical or physical locations containing GTM servers and virtual servers. Use this module to define the network location, contact information, and failover behavior of datacenters so GTM can make intelligent DNS load-balancing decisions and maintain service availability during site outages.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **contact** | **Type:** string | Specifies the contact information for the datacenter, such as an email address, phone number, or name. |
| **description** | **Type:** string | Description of the datacenter for administrative reference. |
| **enabled** | **Choices:** yes, no<br>**Default:** yes | Whether the datacenter is enabled. Disabled datacenters are not considered in GTM load-balancing decisions. |
| **location** | **Type:** string | Specifies the physical or logical location of the datacenter (for example, “Seattle DC1”). |
| **name** | **Type:** string<br>**Required:** yes | Name of the datacenter object. |
| **partition** | **Default:** Common | Device partition to manage the datacenter in. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the datacenter exists with the specified settings; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **contact** | The configured contact information for the datacenter. |
| **description** | The description set on the datacenter. |
| **enabled** | Whether the datacenter is enabled after the task completes. |
| **location** | The configured location string of the datacenter. |
| **name** | Name of the datacenter managed by the module. |
| **partition** | Partition where the datacenter resides. |


## Examples

```yaml
- name: Create a new GTM datacenter
  bigip_gtm_datacenter:
    name: dc-seattle
    location: "Seattle, WA"
    contact: "noc@example.com"
    description: "Primary production datacenter"
    enabled: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable an existing GTM datacenter
  bigip_gtm_datacenter:
    name: dc-seattle
    enabled: no
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an obsolete GTM datacenter
  bigip_gtm_datacenter:
    name: dc-old
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



