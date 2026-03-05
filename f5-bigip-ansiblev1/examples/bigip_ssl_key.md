# bigip_ssl_key


## Description

The `bigip_ssl_key` module manages SSL private keys on F5 BIG-IP systems. It supports importing existing keys, generating new keys, and removing unused or compromised keys. You can control key size, type, and passphrases where supported. This module is essential for securely managing the cryptographic material used by SSL profiles and virtual servers.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the key object on the BIG-IP. |
| **partition** | **Default:** Common | Administrative partition where the key resides. |
| **state** | **Choices:** present, absent | `present` imports or generates the key; `absent` removes it. |
| **src** | **Type:** string | Local path to an existing key file to upload. |
| **content** | **Type:** string | PEM-formatted key content provided inline. |
| **key\_size** | **Type:** integer | Size of the generated key (e.g. 2048, 4096) when generating keys. |
| **key\_type** | **Choices:** rsa, ec | Type of key to generate when not importing. |
| **passphrase** | **Type:** string | Passphrase for encrypted keys, if applicable. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the key object managed. |
| **partition** | Partition where the key is stored. |
| **generated** | Boolean indicating if a new key was generated. |
| **imported** | Boolean indicating if a key was imported from external source. |
| **state** | Final state of the key object. |


## Examples


```yaml
- name: Import existing private key
  bigip_ssl_key:
    name: "www_example_com.key"
    partition: "Common"
    src: "/etc/pki/tls/private/www_example_com.key"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks


