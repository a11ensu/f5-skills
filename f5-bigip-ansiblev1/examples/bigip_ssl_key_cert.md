# bigip_ssl_key_cert


## Description

The `bigip_ssl_key_cert` module manages SSL key and certificate pairs together on F5 BIG-IP devices. It simplifies provisioning by allowing you to import or remove both the private key and certificate in a single task, ensuring they are correctly associated. This is useful for bulk onboarding of SSL assets and for maintaining consistency between keys and certificates used by SSL profiles.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Base name for the key and certificate objects. |
| **partition** | **Default:** Common | Administrative partition where key and certificate reside. |
| **state** | **Choices:** present, absent | `present` imports or updates key and certificate; `absent` removes both. |
| **key\_src** | **Type:** string | Local path to the private key file. |
| **cert\_src** | **Type:** string | Local path to the certificate file. |
| **key\_content** | **Type:** string | Inline PEM-formatted key content. |
| **cert\_content** | **Type:** string | Inline PEM-formatted certificate content. |
| **passphrase** | **Type:** string | Passphrase for encrypted private key, if applicable. |
| **validate\_cert** | **Choices:** yes, no | Whether to validate certificate format during import. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Base name of the key and certificate objects managed. |
| **partition** | Partition where the key and certificate are stored. |
| **key\_imported** | Boolean indicating if the key was imported. |
| **cert\_imported** | Boolean indicating if the certificate was imported. |
| **state** | Final state of the key/cert pair. |


## Examples


```yaml
- name: Import key and certificate pair
  bigip_ssl_key_cert:
    name: "www_example_com"
    partition: "Common"
    key_src: "/etc/pki/tls/private/www_example_com.key"
    cert_src: "/etc/pki/tls/certs/www_example_com.crt"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


