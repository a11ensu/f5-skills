# bigip_gtm_virtual_server


## Description

The `bigip_gtm_virtual_server` module manages GTM virtual server objects on F5 BIG-IP systems. GTM virtual servers represent application endpoints (IP and port) that participate in GTM pools, typically mapped from underlying LTM virtual servers or external services. Use this module to create, modify, or delete GTM virtual servers, configure their addresses, ports, associated GTM servers, and translation settings, enabling GTM to direct DNS traffic to the correct application instances across data centers.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **address** | **Type:** string<br>**Required:** yes | IP address of the GTM virtual server. |
| **description** | **Type:** string | Description of the GTM virtual server. |
| **enabled** | **Choices:** yes, no<br>**Default:** yes | Whether the GTM virtual server is enabled for load balancing. |
| **name** | **Type:** string<br>**Required:** yes | Name of the GTM virtual server. |
| **port** | **Type:** integer<br>**Default:** 0 | Service port of the virtual server (`0` often meaning any). |
| **server** | **Type:** string<br>**Required:** yes | Name of the GTM server object that owns this virtual server. |
| **translation_address** | **Type:** string | Translated IP address, if NAT or SNAT is used. |
| **translation_port** | **Type:** integer | Translated port, if different from the original port. |
| **monitor** | **Type:** string | Optional monitor rule applied directly to the virtual server. |
| **partition** | **Default:** Common | Partition in which the GTM virtual server is created. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the GTM virtual server exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | Name of the GTM virtual server. |
| **server** | GTM server that owns this virtual server. |
| **address** | Configured IP address of the virtual server. |
| **port** | Configured service port. |
| **enabled** | Whether the virtual server is enabled. |
| **translation_address** | Translation address, if configured. |
| **translation_port** | Translation port, if configured. |


## Examples

```yaml
- name: Create a GTM virtual server for HTTPS
  bigip_gtm_virtual_server:
    name: app_vs_443
    server: dc1-bigip
    address: 192.0.2.10
    port: 443
    description: "HTTPS endpoint in DC1"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Add translation address and port to a GTM virtual server
  bigip_gtm_virtual_server:
    name: app_vs_443
    server: dc1-bigip
    address: 192.0.2.10
    port: 443
    translation_address: 10.10.10.10
    translation_port: 8443
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a GTM virtual server
  bigip_gtm_virtual_server:
    name: old_app_vs_80
    server: dc1-bigip
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



