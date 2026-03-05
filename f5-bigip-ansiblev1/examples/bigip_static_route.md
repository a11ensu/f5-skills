# bigip_static_route


## Description

The `bigip_static_route` module manages static routing entries on F5 BIG-IP devices. It allows you to create, update, or remove IPv4 and IPv6 static routes, including management routes. You can define destination networks, gateways, VLANs, and route domains, as well as configure attributes such as MTU, route description, and whether the route is enabled or disabled. This module is useful for automating network path configuration and ensuring consistent routing across BIG-IP instances.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Specifies a user-defined description for the static route. |
| **destination** | **Type:** string | Destination IP address and prefix for the route in CIDR notation (for example, `10.0.0.0/24`). |
| **gateway_address** | **Type:** string | Specifies the gateway IP address used for forwarding packets to the destination. |
| **name** | **Type:** string<br>**Required:** yes | The name of the static route. |
| **network** | **Type:** string | Specifies the route destination in the form of `host`, `network`, or `default`. Deprecated in favor of `destination`. |
| **partition** | **Default:** Common | Specifies the administrative partition in which the route resides. |
| **route_domain** | **Type:** integer | The route domain ID associated with this route. |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the static route exists with the specified attributes; when `absent`, removes it. |
| **type** | **Choices:** interface, gateway, reject, blackhole | Defines the type of static route. |
| **use_gateway** | **Choices:** yes, no | Indicates whether to use a gateway for this route. |
| **vlan** | **Type:** string | Specifies the VLAN through which traffic for this route is forwarded. |
| **mtu** | **Type:** integer | Sets the Maximum Transmission Unit (MTU) for packets sent via this route. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device (for example, server, user, password, server_port, validate_certs). |


## Return Values


| Key | Description |
| --- | --- |
| **description** | The description configured on the static route. |
| **destination** | The destination network or host configured for the static route. |
| **gateway_address** | The gateway IP address associated with the route. |
| **name** | The name of the static route. |
| **partition** | The administrative partition where the route resides. |
| **route_domain** | The route domain ID associated with the route. |
| **state** | The final state of the static route (`present` or `absent`). |
| **type** | The type of route configured (for example, `gateway`). |
| **vlan** | The VLAN used by the route, if configured. |
| **mtu** | The MTU value applied to the route, if configured. |


## Examples


```yaml
- name: Create a gateway static route
  bigip_static_route:
    name: default_gw
    destination: 0.0.0.0/0
    gateway_address: 10.10.10.1
    type: gateway
    description: Default route to upstream router
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create an interface route on a specific VLAN
  bigip_static_route:
    name: internal_net
    destination: 192.168.100.0/24
    vlan: internal
    type: interface
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create an IPv6 static route with route domain
  bigip_static_route:
    name: v6_route
    destination: "2001:db8:10::/64"
    gateway_address: "2001:db8:10::1"
    route_domain: 1
    type: gateway
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a static route
  bigip_static_route:
    name: internal_net
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



