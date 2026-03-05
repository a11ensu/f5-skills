# bigip_ssl_certificate


## Description

The `bigip_ssl_certificate` module manages SSL/TLS certificates on F5 BIG-IP devices. It supports importing certificates from files or inline content, updating existing certificates, and deleting obsolete ones. This module is commonly used in conjunction with key and CSR modules to automate certificate lifecycle tasks and ensure that virtual servers use the correct, up-to-date certificates.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the certificate object on the BIG-IP. |
| **partition** | **Default:** Common | Administrative partition where the certificate resides. |
| **state** | **Choices:** present, absent | `present` imports or updates the certificate; `absent` removes it. |
| **src** | **Type:** string | Local path to the certificate file to upload. |
| **content** | **Type:** string | PEM-formatted certificate content provided inline instead of `src`. |
| **issuer\_cert** | **Type:** string | Optional issuer or chain certificate file or content. |
| **validate\_cert** | **Choices:** yes, no | Whether to validate certificate format during import. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the certificate managed. |
| **partition** | Partition where the certificate is stored. |
| **imported** | Boolean indicating if a new certificate was imported. |
| **updated** | Boolean indicating if an existing certificate was replaced. |
| **state** | Final state of the certificate object. |


## Examples


```yaml
- name: Import SSL certificate from local file
  bigip_ssl_certificate:
    name: "www_example_com.crt"
    partition: "Common"
    src: "/etc/pki/tls/certs/www_example_com.crt"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


