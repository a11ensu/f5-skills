# bigip_device_certificate


## Description

The `bigip_device_certificate` module manages the BIG-IP device certificate used for management interfaces and device identity. It supports importing new certificates and keys, generating certificate signing requests (CSRs), and replacing the default self-signed certificate. By automating device certificate operations, you can integrate BIG-IP into enterprise PKI, improve management plane security, and keep certificates updated without manual intervention.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Default:** default | Name of the device certificate object (usually `default`). |
| **cert** | **Type:** string | PEM-formatted certificate content to install as the device certificate. |
| **key** | **Type:** string | PEM-formatted private key content corresponding to the certificate. |
| **passphrase** | **Type:** string | Passphrase for an encrypted private key, if applicable. |
| **csr** | **Type:** bool<br>**Default:** no | If yes, generates a CSR instead of installing a certificate. |
| **common_name** | **Type:** string | Common Name (CN) to use when generating a CSR. |
| **country** | **Type:** string | Country code (C) for the CSR subject. |
| **state_or_province** | **Type:** string | State or province (ST) for the CSR subject. |
| **locality** | **Type:** string | Locality or city (L) for the CSR subject. |
| **organization** | **Type:** string | Organization (O) for the CSR subject. |
| **organizational_unit** | **Type:** string | Organizational Unit (OU) for the CSR subject. |
| **email** | **Type:** string | Email address for the CSR subject. |
| **key_size** | **Choices:** 1024, 2048, 4096<br>**Default:** 2048 | Key size used when generating a new key for the CSR. |
| **state** | **Choices:** present | `present` ensures the device certificate or CSR matches the provided parameters. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server\_port, validate\_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the device certificate object. |
| **csr** | CSR content generated, when requested. |
| **common_name** | Common Name used in the CSR or certificate. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Generate CSR for device certificate
  bigip_device_certificate:
    name: default
    csr: yes
    common_name: bigip1.example.com
    country: US
    state_or_province: California
    locality: San Jose
    organization: Example Corp
    organizational_unit: Network
    email: netops@example.com
    key_size: 2048
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Install new device certificate and key
  bigip_device_certificate:
    name: default
    cert: "{{ lookup('file', 'files/bigip1_device.crt') }}"
    key: "{{ lookup('file', 'files/bigip1_device.key') }}"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Install encrypted device key and certificate
  bigip_device_certificate:
    name: default
    cert: "{{ lookup('file', 'files/bigip1_device.crt') }}"
    key: "{{ lookup('file', 'files/bigip1_device_encrypted.key') }}"
    passphrase: "{{ device_key_passphrase }}"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



