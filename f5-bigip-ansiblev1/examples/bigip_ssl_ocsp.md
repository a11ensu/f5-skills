# bigip_ssl_ocsp


## Description

The `bigip_ssl_ocsp` module manages Online Certificate Status Protocol (OCSP) configurations on F5 BIG-IP devices. It allows you to define OCSP responders, associate them with SSL profiles, and control parameters such as timeouts, caching, and responder certificates. This module helps ensure that BIG-IP can validate certificate revocation status dynamically for enhanced security.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the OCSP configuration object. |
| **partition** | **Default:** Common | Administrative partition where the OCSP object resides. |
| **responder\_url** | **Type:** string<br>**Required:** yes | URL of the OCSP responder. |
| **signing\_cert** | **Type:** string | Name of certificate used to validate OCSP responder signatures. |
| **timeout** | **Type:** integer | Timeout in seconds for OCSP queries. |
| **status\_age** | **Type:** integer | Maximum age in seconds for cached OCSP responses. |
| **nonce** | **Choices:** enabled, disabled | Enables or disables use of OCSP nonce. |
| **state** | **Choices:** present, absent | `present` ensures OCSP configuration exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the OCSP configuration managed. |
| **responder\_url** | Effective OCSP responder URL. |
| **timeout** | Timeout used for OCSP requests. |
| **status\_age** | Maximum cache age for OCSP responses. |
| **nonce** | Final nonce setting for OCSP queries. |
| **state** | Final state of the OCSP configuration. |


## Examples


```yaml
- name: Configure OCSP responder for SSL validation
  bigip_ssl_ocsp:
    name: "ocsp_example"
    partition: "Common"
    responder_url: "http://ocsp.example.com"
    signing_cert: "ocsp_signing_ca.crt"
    timeout: 5
    status_age: 3600
    nonce: enabled
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
