# bigip_profile_client_ssl


## Description

The `bigip_profile_client_ssl` module manages client SSL profiles on F5 BIG-IP devices. These profiles define how BIG-IP terminates SSL/TLS from clients, including which certificates and keys are presented, supported cipher suites, protocol versions, and security options like renegotiation and session resumption. By using this module, administrators can standardize SSL settings across virtual servers, enforce security policies, and simplify certificate lifecycle operations (deployment, rotation, and decommissioning) in automated workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **alert_timeout** | **Type:** integer | Time in seconds before an SSL alert times out. |
| **authenticate** | **Choices:** always, request, require, none | Controls client certificate authentication behavior. |
| **ciphers** | **Type:** string | OpenSSL-style cipher string defining allowed ciphers. |
| **description** | **Type:** string | User-defined description of the client SSL profile. |
| **key** | **Type:** string | Name of the SSL key object to use. |
| **cert** | **Type:** string | Name of the SSL certificate object to use. |
| **chain** | **Type:** string | Name of the certificate chain object to present. |
| **default_profile** | **Type:** string | Parent client SSL profile to inherit settings from. |
| **name** | **Type:** string<br>**Required:** yes | Name of the client SSL profile. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **secure_renegotiation** | **Choices:** require, request, none | Controls TLS secure renegotiation behavior. |
| **server_name** | **Type:** string | SNI server name used for certificate selection. |
| **session_ticket** | **Choices:** enabled, disabled | Enables or disables TLS session tickets. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |
| **tls_versions** | **Type:** list | List of allowed TLS protocol versions (for example, TLSv1.2, TLSv1.3). |


## Return Values


| Key | Description |
| --- | --- |
| **ciphers** | Effective cipher string configured. |
| **cert** | Certificate associated with the profile. |
| **chain** | Chain certificate used by the profile. |
| **description** | Description set on the profile. |
| **name** | Name of the client SSL profile managed. |
| **partition** | Partition where the profile is configured. |
| **secure_renegotiation** | Final secure renegotiation setting. |
| **session_ticket** | Indicates if session tickets are enabled. |
| **tls_versions** | List of allowed protocol versions. |


## Examples


```yaml
- name: Create client SSL profile with TLS 1.2/1.3
  bigip_profile_client_ssl:
    name: clientssl_webapp
    description: Client SSL for external web app
    cert: webapp.crt
    key: webapp.key
    chain: intermediate_ca
    ciphers: DEFAULT:!RC4:!3DES
    tls_versions:
      - TLSv1.2
      - TLSv1.3
    secure_renegotiation: require
    session_ticket: enabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Update ciphers on existing client SSL profile
  bigip_profile_client_ssl:
    name: clientssl_webapp
    ciphers: HIGH:!aNULL:!MD5
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove client SSL profile
  bigip_profile_client_ssl:
    name: old_clientssl
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



