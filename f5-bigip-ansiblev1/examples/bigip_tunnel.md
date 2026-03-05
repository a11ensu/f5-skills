# bigip_tunnel


## Description

The `bigip_tunnel` module manages tunnels on F5 BIG-IP devices. Tunnels provide encapsulation mechanisms (such as GRE, VXLAN, or IPsec-related tunnels) to transport traffic across networks. This module allows you to create, modify, or delete tunnels, configure local and remote endpoints, associate profiles, and control encapsulation parameters. Automating tunnel configuration simplifies deployment of overlay networks, remote connectivity, and multi-site architectures.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the tunnel. |
| **partition** | **Default:** Common | Administrative partition where the tunnel resides. |
| **description** | **Type:** string | User-defined description for the tunnel. |
| **local_address** | **Type:** string | Local endpoint IP address of the tunnel. |
| **remote_address** | **Type:** string | Remote endpoint IP address of the tunnel. |
| **profile** | **Type:** string | Tunnel profile to use (for example, GRE, VXLAN). |
| **key** | **Type:** integer | Key or VNI used for tunnel identification, if applicable. |
| **mtu** | **Type:** integer | MTU for the tunnel interface. |
| **auto_last_hop** | **Choices:** enabled, disabled | Controls auto last hop behavior on the tunnel. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the tunnel exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the tunnel. |
| **description** | Description of the tunnel. |
| **local_address** | Local endpoint IP address. |
| **remote_address** | Remote endpoint IP address. |
| **profile** | Tunnel profile in use. |
| **key** | Tunnel key or VNI. |
| **mtu** | MTU configured on the tunnel. |
| **auto_last_hop** | Auto last hop setting. |
| **partition** | Partition where the tunnel resides. |
| **state** | Final state (`present` or `absent`). |


## Examples


```yaml
- name: Create a GRE tunnel
  bigip_tunnel:
    name: gre_tunnel1
    profile: /Common/gre
    local_address: 203.0.113.1
    remote_address: 198.51.100.1
    mtu: 1450
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a VXLAN tunnel with key
  bigip_tunnel:
    name: vxlan_tunnel1
    profile: /Common/vxlan
    local_address: 203.0.113.2
    remote_address: 198.51.100.2
    key: 1001
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a tunnel
  bigip_tunnel:
    name: gre_tunnel1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



