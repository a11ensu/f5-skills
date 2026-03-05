# bigip_profile_server_ssl


## Description

The `bigip_profile_server_ssl` module manages server SSL profiles on F5 BIG-IP systems. Server SSL profiles define how BIG-IP initiates and maintains SSL/TLS connections to back-end servers, including which ciphers and protocol versions are used, certificate validation options, and SNI settings. By configuring these profiles, administrators can enforce strong security to servers, re-encrypt traffic, and handle scenarios such as different certificates or protocols per pool or virtual server in automated deployments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **ciphers** | **Type:** string | OpenSSL-style cipher string defining allowed ciphers for server-side connections. |
| **description** | **Type:** string | User-defined description of the server SSL profile. |
| **name** | **Type:** string<br>**Required:** yes | Name of the server SSL profile. |
| **parent** | **Type:** string | Parent server SSL profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **server_name** | **Type:** string | SNI server name sent to the back-end server. |
| **session_ticket** | **Choices:** enabled, disabled | Enables or disables TLS session tickets on server side. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |
| **tls_versions** | **Type:** list | List of allowed TLS protocol versions for server connections. |
| **validate_certificate** | **Choices:** yes, no | Enables or disables validation of server certificates. |


## Return Values


| Key | Description |
| --- | --- |
| **ciphers** | Effective cipher string configured. |
| **description** | Description set on the profile. |
| **name** | Name of the server SSL profile managed. |
| **partition** | Partition where the profile is configured. |
| **server_name** | SNI name used for back-end servers. |
| **session_ticket** | Indicates if session tickets are enabled. |
| **tls_versions** | List of allowed protocol versions. |
| **validate_certificate** | Indicates if server certificate validation is enabled. |


## Examples


```yaml
- name: Create server SSL profile with TLS 1.2 only
  bigip_profile_server_ssl:
    name: serverssl_app
    description: Server SSL profile for app servers
    parent: serverssl
    ciphers: HIGH:!aNULL:!MD5
    tls_versions:
      - TLSv1.2
    validate_certificate: yes
    server_name: app.internal.local
    session_ticket: disabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Allow TLS 1.3 to servers
  bigip_profile_server_ssl:
    name: serverssl_app
    tls_versions:
      - TLSv1.2
      - TLSv1.3
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove server SSL profile
  bigip_profile_server_ssl:
    name: old_serverssl
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



