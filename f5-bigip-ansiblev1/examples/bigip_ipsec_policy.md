# bigip_ipsec_policy


## Description

The `bigip_ipsec_policy` module manages IPSec policies on F5 BIG-IP systems. It defines how traffic is protected within VPN tunnels, including encryption algorithms, authentication methods, and lifetimes. By using this module, you can create, modify, or delete IPSec policies and align BIG-IP VPN parameters with remote peers for interoperable, secure site-to-site or remote-access VPN deployments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the IPSec policy. |
| **ipsec_protocol** | **Choices:** esp, ah | IPSec protocol used for the policy. |
| **encryption_algorithms** | **Type:** list | List of encryption algorithms (for example, `aes256`, `aes128`). |
| **authentication_algorithms** | **Type:** list | List of authentication algorithms (for example, `sha256`, `sha1`). |
| **pfs** | **Type:** bool | Enable or disable Perfect Forward Secrecy. |
| **pfs_dh_group** | **Type:** string | DH group used when PFS is enabled. |
| **lifetime** | **Type:** integer | IPSec SA lifetime in seconds. |
| **mode** | **Choices:** tunnel, transport | IPSec mode for the policy. |
| **state** | **Choices:** present, absent | Whether the IPSec policy should exist or be removed. |
| **partition** | **Default:** Common | Partition in which to manage the IPSec policy. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the IPSec policy. |
| **ipsec_protocol** | Protocol (ESP or AH) configured. |
| **encryption_algorithms** | Effective encryption algorithms used. |
| **authentication_algorithms** | Effective authentication algorithms used. |
| **lifetime** | Configured IPSec SA lifetime. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create an ESP tunnel IPSec policy with AES256/SHA256
  bigip_ipsec_policy:
    name: branch1_ipsec_policy
    ipsec_protocol: esp
    mode: tunnel
    encryption_algorithms:
      - aes256
    authentication_algorithms:
      - sha256
    pfs: true
    pfs_dh_group: modp2048
    lifetime: 3600
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update IPSec policy to add AES128 as secondary encryption
  bigip_ipsec_policy:
    name: branch1_ipsec_policy
    encryption_algorithms:
      - aes256
      - aes128
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an IPSec policy
  bigip_ipsec_policy:
    name: branch1_ipsec_policy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



