# bigip_device_auth_ldap


## Description

The `bigip_device_auth_ldap` module configures LDAP-based authentication for BIG-IP device logins. It manages LDAP authentication and AAA settings such as servers, base DNs, bind credentials, search filters, and SSL/TLS options. By automating these parameters, you can integrate BIG-IP with enterprise directories like Active Directory, centralize user management, and enforce secure, standardized access to administrative interfaces.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Default:** /Common/ldap | Name of the LDAP auth configuration object. |
| **servers** | **Type:** list | List of LDAP servers (hostnames or IP addresses). |
| **port** | **Type:** integer<br>**Default:** 389 | TCP port used to connect to LDAP servers. |
| **ssl** | **Choices:** disabled, ldaps, starttls | SSL/TLS mode for the LDAP connection. |
| **bind_dn** | **Type:** string | DN used to bind to the LDAP server for searching users. |
| **bind_password** | **Type:** string | Password for the bind DN. |
| **base_dn** | **Type:** string | Base DN from which user searches begin. |
| **user_key** | **Type:** string<br>**Default:** sAMAccountName | LDAP attribute used as the username key. |
| **user_template** | **Type:** string | Template for constructing user DNs (for example, `uid=%s,ou=People,dc=example,dc=com`). |
| **group_dn** | **Type:** string | Base DN used for group searches. |
| **group_member_attribute** | **Type:** string | Attribute used to identify group membership (for example, `memberOf`). |
| **check_member_attribute** | **Type:** bool<br>**Default:** no | Whether to verify user membership in a specific group. |
| **timeout** | **Type:** integer<br>**Default:** 10 | Timeout in seconds for LDAP operations. |
| **realm** | **Type:** string | Realm name used in prompts or logging. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` creates or updates the LDAP auth configuration; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server\_port, validate\_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the LDAP auth configuration. |
| **servers** | List of LDAP servers configured. |
| **ssl** | SSL/TLS mode in use. |
| **base_dn** | Base DN for user searches. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Configure LDAP authentication against Active Directory
  bigip_device_auth_ldap:
    name: /Common/ad_ldap
    servers:
      - ad1.example.com
      - ad2.example.com
    port: 389
    ssl: starttls
    bind_dn: "CN=ldap-bind,OU=Service Accounts,DC=example,DC=com"
    bind_password: "{{ ad_bind_password }}"
    base_dn: "DC=example,DC=com"
    user_key: sAMAccountName
    timeout: 10
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure simple LDAPS authentication
  bigip_device_auth_ldap:
    name: /Common/secure_ldap
    servers:
      - ldap-secure.example.com
    port: 636
    ssl: ldaps
    user_template: "uid=%s,ou=People,dc=example,dc=com"
    timeout: 5
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove LDAP authentication profile
  bigip_device_auth_ldap:
    name: /Common/ad_ldap
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



