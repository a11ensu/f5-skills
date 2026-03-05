# bigip_device_auth_radius


## Description

The `bigip_device_auth_radius` module configures RADIUS-based authentication for BIG-IP device logins. It manages RADIUS AAA settings such as server lists, timeouts, retries, shared secrets, and accounting options. Using this module, you can integrate BIG-IP with centralized RADIUS services for user authentication and authorization, aligning device access control with existing network access policies.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Default:** /Common/radius | Name of the RADIUS auth configuration object. |
| **servers** | **Type:** list | List of RADIUS server names or IP addresses. |
| **server_pool** | **Type:** string | Name of a RADIUS server pool to use instead of individual servers. |
| **auth_port** | **Type:** integer<br>**Default:** 1812 | RADIUS authentication port. |
| **acct_port** | **Type:** integer<br>**Default:** 1813 | RADIUS accounting port. |
| **timeout** | **Type:** integer<br>**Default:** 3 | Timeout in seconds for RADIUS requests. |
| **retries** | **Type:** integer<br>**Default:** 3 | Number of retries for failed RADIUS requests. |
| **secret** | **Type:** string | Shared secret used with RADIUS servers. |
| **nas_ip** | **Type:** string | NAS-IP-Address value sent to the RADIUS server. |
| **realm** | **Type:** string | Realm name used for prompts or logging. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the RADIUS auth configuration; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server\_port, validate\_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the RADIUS auth configuration. |
| **servers** | List of RADIUS servers configured. |
| **auth_port** | Authentication port in use. |
| **acct_port** | Accounting port in use. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Configure RADIUS authentication with two servers
  bigip_device_auth_radius:
    name: /Common/radius_auth
    servers:
      - 192.0.2.10
      - 192.0.2.11
    auth_port: 1812
    acct_port: 1813
    timeout: 5
    retries: 3
    secret: "{{ radius_shared_secret }}"
    realm: "RADIUS-REALM"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure RADIUS authentication using server pool
  bigip_device_auth_radius:
    name: /Common/radius_pool_auth
    server_pool: /Common/radius_server_pool
    timeout: 4
    retries: 2
    secret: "{{ radius_pool_secret }}"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove RADIUS authentication profile
  bigip_device_auth_radius:
    name: /Common/radius_auth
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



