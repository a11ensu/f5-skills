# bigip_ike_peer


## Description

The `bigip_ike_peer` module manages IPSec IKE peer configuration on F5 BIG-IP devices. It allows you to create, modify, or delete IKE peers that define how BIG-IP establishes and authenticates VPN tunnels with remote gateways. You can configure proposals, authentication methods, local/remote IDs, and traffic selectors to automate secure site-to-site VPN deployments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the IKE peer object. |
| **version** | **Choices:** 1, 2 | IKE protocol version used for this peer. |
| **remote_address** | **Type:** string | IP address or hostname of the remote IKE gateway. |
| **local_address** | **Type:** string | Local IP address used for IKE negotiations. |
| **auth_method** | **Choices:** psk, rsa-signature | Authentication method for the peer. |
| **psk** | **Type:** string | Pre-shared key when `auth_method` is `psk`. |
| **cert** | **Type:** string | Name of certificate when using certificate-based auth. |
| **local_id** | **Type:** string | Local IKE identity (ID). |
| **remote_id** | **Type:** string | Remote IKE identity (ID). |
| **phase1_proposals** | **Type:** list | List of IKE phase 1 proposals (encryption, hash, DH group, etc.). |
| **lifetime** | **Type:** integer | IKE SA lifetime in seconds. |
| **nat_traversal** | **Type:** bool | Enable or disable NAT traversal for this peer. |
| **dpd** | **Type:** bool | Enable or disable Dead Peer Detection. |
| **state** | **Choices:** present, absent | Whether the IKE peer should exist or be removed. |
| **partition** | **Default:** Common | Partition in which to manage the IKE peer. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the IKE peer. |
| **remote_address** | Remote gateway address configured for the peer. |
| **version** | IKE version being used. |
| **auth_method** | Authentication method applied to the peer. |
| **phase1_proposals** | Effective IKE phase 1 proposals. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create an IKEv2 peer using pre-shared key
  bigip_ike_peer:
    name: branch1_ike
    version: 2
    remote_address: 203.0.113.10
    local_address: 198.51.100.1
    auth_method: psk
    psk: supersecretkey
    phase1_proposals:
      - aes256-sha256-modp2048
    lifetime: 28800
    nat_traversal: true
    dpd: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update IKE peer proposals
  bigip_ike_peer:
    name: branch1_ike
    phase1_proposals:
      - aes256-sha256-modp2048
      - aes128-sha1-modp1024
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an IKE peer
  bigip_ike_peer:
    name: branch1_ike
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



