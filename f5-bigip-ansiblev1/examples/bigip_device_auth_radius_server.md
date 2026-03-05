# bigip_device_auth_radius_server


## Description

The `bigip_device_auth_radius_server` module manages individual RADIUS server objects used by BIG-IP for device authentication. It allows you to define server addresses, authentication and accounting ports, timeouts, and shared secrets. These server objects can then be referenced by RADIUS authentication profiles or pools, enabling modular and reusable RADIUS configurations across multiple BIG-IP services.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the RADIUS server object. |
| **address** | **Type:** string<br>**Required:** yes | IP address or hostname of the RADIUS server. |
| **auth_port** | **Type:** integer<br>**Default:** 1812 | RADIUS authentication port. |
| **acct_port** | **Type:** integer<br>**Default:** 1813 | RADIUS accounting port. |
| **timeout** | **Type:** integer<br>**Default:** 3 | Timeout in seconds for RADIUS requests. |
| **retries** | **Type:** integer<br>**Default:** 3 | Number of retries for failed requests. |
| **secret** | **Type:** string | Shared secret used with this RADIUS server. |
| **description** | **Type:** string | Descriptive text for the RADIUS server object. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the RADIUS server; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server\_port, validate\_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the RADIUS server object. |
| **address** | IP address or hostname configured. |
| **auth_port** | Authentication port in use. |
| **acct_port** | Accounting port in use. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Create RADIUS server object
  bigip_device_auth_radius_server:
    name: radius1
    address: 192.0.2.10
    auth_port: 1812
    acct_port: 1813
    timeout: 5
    retries: 3
    secret: "{{ radius_shared_secret }}"
    description: "Primary RADIUS server"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update RADIUS server timeout
  bigip_device_auth_radius_server:
    name: radius1
    address: 192.0.2.10
    timeout: 7
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove RADIUS server object
  bigip_device_auth_radius_server:
    name: radius1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



