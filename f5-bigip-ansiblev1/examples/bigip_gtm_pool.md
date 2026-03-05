# bigip_gtm_pool


## Description

The `bigip_gtm_pool` module manages GTM (DNS) pools on F5 BIG-IP systems. GTM pools group virtual servers or links that provide the same application or service so DNS can distribute requests among them. Use this module to create, modify, or delete GTM pools, configure load-balancing methods, health monitors, fallback behavior, limits, and member order, enabling resilient and intelligent DNS-based traffic distribution across data centers and environments.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **alternate_lb_method** | **Choices:** round-robin, ratio, global-availability, topology, return-to-dns, vs-capacity, completion-rate, drop-packet, fallback-ip, packet-rate, qos, round-trip-time, virtual-server-capacity, kilobytes-per-second, least-connections, lowest-round-trip-time, fewest-hops, observed, predictive, ratio-least-connections, ratio-member, ratio-node, ratio-session, ratio-qos | Specifies the alternate load balancing method used when the preferred method is unavailable. |
| **description** | **Type:** string | Description of the GTM pool for administrative reference. |
| **enabled** | **Choices:** yes, no<br>**Default:** yes | Whether the pool is enabled. Disabled pools are excluded from DNS load balancing. |
| **fallback_lb_method** | **Choices:** round-robin, ratio, global-availability, topology, return-to-dns, vs-capacity, completion-rate, drop-packet, fallback-ip, packet-rate, qos, round-trip-time, virtual-server-capacity, kilobytes-per-second, least-connections, lowest-round-trip-time, fewest-hops, observed, predictive, ratio-least-connections, ratio-member, ratio-node, ratio-session, ratio-qos | Load balancing method used when both preferred and alternate methods are unavailable. |
| **limit_max_bps** | **Type:** integer | Maximum bits per second allowed for the pool before traffic is limited. |
| **limit_max_bps_status** | **Choices:** enabled, disabled | Enables or disables enforcement of `limit_max_bps`. |
| **limit_max_connections** | **Type:** integer | Maximum concurrent connections allowed to the pool. |
| **limit_max_connections_status** | **Choices:** enabled, disabled | Enables or disables enforcement of `limit_max_connections`. |
| **limit_max_pps** | **Type:** integer | Maximum packets per second allowed for the pool. |
| **limit_max_pps_status** | **Choices:** enabled, disabled | Enables or disables enforcement of `limit_max_pps`. |
| **load_balancing_mode** | **Choices:** round-robin, ratio, global-availability, topology, return-to-dns, vs-capacity, completion-rate, drop-packet, fallback-ip, packet-rate, qos, round-trip-time, virtual-server-capacity, kilobytes-per-second, least-connections, lowest-round-trip-time, fewest-hops, observed, predictive, ratio-least-connections, ratio-member, ratio-node, ratio-session, ratio-qos | The preferred load balancing method for the pool. |
| **manual_resume** | **Choices:** yes, no | When `yes`, requires manual intervention to resume pool availability after failure. |
| **members** | **Type:** list | List of GTM pool members to associate with the pool. Each item typically references a GTM virtual server. |
| **monitor** | **Type:** string | Monitor rule string (for example, `"/Common/https and /Common/tcp"` or `"default"`). |
| **name** | **Type:** string<br>**Required:** yes | Name of the GTM pool. |
| **partition** | **Default:** Common | Partition in which the pool is managed. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **qos_hit_ratio** | **Type:** integer | Weight of hit ratio in QoS calculations. |
| **qos_hops** | **Type:** integer | Weight of hops in QoS calculations. |
| **qos_kilobytes_second** | **Type:** integer | Weight of throughput in QoS calculations. |
| **qos_lcs** | **Type:** integer | Weight of link capacity in QoS calculations. |
| **qos_packet_rate** | **Type:** integer | Weight of packet rate in QoS calculations. |
| **qos_rtt** | **Type:** integer | Weight of round-trip time in QoS calculations. |
| **qos_topology** | **Type:** integer | Weight of topology in QoS calculations. |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the GTM pool exists with specified settings; when `absent`, removes it. |
| **type** | **Choices:** a, aaaa, cname, mx, naptr, srv | DNS record type that the pool serves. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | Name of the GTM pool managed by the module. |
| **enabled** | Indicates whether the pool is enabled. |
| **load_balancing_mode** | The active load balancing mode for the pool. |
| **monitor** | Monitor rule currently configured on the pool. |
| **members** | List of members associated with the pool and their effective states. |
| **limits** | Dictionary of active connection, bandwidth, and packet rate limits. |


## Examples

```yaml
- name: Create a GTM pool for app.example.com
  bigip_gtm_pool:
    name: app_pool
    type: a
    load_balancing_mode: round-robin
    monitor: "/Common/https"
    description: "Primary application GTM pool"
    members:
      - server: dc1-bigip
        virtual_server: app_vs_443
      - server: dc2-bigip
        virtual_server: app_vs_443
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure QoS load balancing with limits
  bigip_gtm_pool:
    name: app_pool
    type: a
    load_balancing_mode: qos
    qos_rtt: 10
    qos_topology: 5
    limit_max_connections: 100000
    limit_max_connections_status: enabled
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an obsolete GTM pool
  bigip_gtm_pool:
    name: legacy_pool
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



