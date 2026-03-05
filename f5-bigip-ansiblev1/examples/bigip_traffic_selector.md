# bigip_traffic_selector


## Description

The `bigip_traffic_selector` module manages IPSec traffic selectors on F5 BIG-IP devices. Traffic selectors define which traffic is protected by an IPSec policy, specifying local and remote subnets, protocols, and ports. This module allows you to create, modify, or remove traffic selectors associated with IPSec policies or tunnels, ensuring that only the intended traffic is encrypted and routed through secure channels between sites or devices.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the traffic selector. |
| **partition** | **Default:** Common | Administrative partition in which the traffic selector resides. |
| **local_address** | **Type:** string | Local IP address or subnet for the selector. |
| **remote_address** | **Type:** string | Remote IP address or subnet for the selector. |
| **local_port** | **Type:** string | Local port or port range. |
| **remote_port** | **Type:** string | Remote port or port range. |
| **ip_protocol** | **Choices:** tcp, udp, icmp, any | IP protocol for the selector. |
| **direction** | **Choices:** in, out, both | Direction of traffic to which the selector applies. |
| **policy** | **Type:** string | IPSec policy associated with this traffic selector. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the traffic selector exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the traffic selector. |
| **local_address** | Local address or subnet configured. |
| **remote_address** | Remote address or subnet configured. |
| **local_port** | Local port or port range. |
| **remote_port** | Remote port or port range. |
| **ip_protocol** | IP protocol used by the selector. |
| **direction** | Direction of traffic the selector matches. |
| **policy** | IPSec policy associated with the selector. |
| **state** | Final state (`present` or `absent`). |


## Examples


```yaml
- name: Create a bidirectional traffic selector for site-to-site VPN
  bigip_traffic_selector:
    name: ts_site_a_site_b
    local_address: 10.0.0.0/24
    remote_address: 192.168.0.0/24
    ip_protocol: any
    direction: both
    policy: /Common/site_a_site_b_policy
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a TCP traffic selector for specific ports
  bigip_traffic_selector:
    name: ts_web
    local_address: 10.0.0.0/24
    remote_address: 192.168.10.0/24
    ip_protocol: tcp
    local_port: "1024-65535"
    remote_port: "80,443"
    direction: both
    policy: /Common/web_ipsec_policy
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a traffic selector
  bigip_traffic_selector:
    name: ts_site_a_site_b
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



