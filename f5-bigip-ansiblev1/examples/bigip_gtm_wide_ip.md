# bigip_gtm_wide_ip


## Description

The `bigip_gtm_wide_ip` module manages GTM Wide IPs on F5 BIG-IP systems. Wide IPs represent DNS names that GTM answers and map them to one or more GTM pools. Use this module to create, modify, or delete Wide IPs; attach pools with ordering and ratios; configure persistence, TTL, and load-balancing methods; and control how GTM responds to DNS queries for application hostnames across globally distributed data centers.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **aliases** | **Type:** list | List of additional DNS names (CNAMEs) associated with the Wide IP. |
| **description** | **Type:** string | Description of the Wide IP. |
| **enabled** | **Choices:** yes, no<br>**Default:** yes | Whether the Wide IP is enabled for answering DNS queries. |
| **name** | **Type:** string<br>**Required:** yes | Fully qualified domain name of the Wide IP (for example, `app.example.com`). |
| **partition** | **Default:** Common | Partition in which the Wide IP is created. |
| **pools** | **Type:** list | List of GTM pools associated with this Wide IP, each with optional order and ratio. |
| **persist_cidr_ipv4** | **Type:** integer | CIDR mask for IPv4 persistence. |
| **persist_cidr_ipv6** | **Type:** integer | CIDR mask for IPv6 persistence. |
| **persistence** | **Choices:** disabled, enabled | Enables or disables persistence for the Wide IP. |
| **pool_lb_mode** | **Choices:** round-robin, ratio, global-availability, topology, vs-capacity, completion-rate, drop-packet, packet-rate, qos, round-trip-time, kilobytes-per-second, least-connections, lowest-round-trip-time, fewest-hops, observed, predictive, ratio-least-connections, ratio-member, ratio-node, ratio-session, ratio-qos | Load-balancing method used among the associated pools. |
| **response_type** | **Choices:** a, aaaa, cname, mx, naptr, srv | DNS response type for this Wide IP. |
| **ttl** | **Type:** integer | DNS time-to-live value for responses for this Wide IP. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the Wide IP exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | DNS name of the Wide IP. |
| **enabled** | Whether the Wide IP is enabled. |
| **pools** | List of pools and their order/ratio associated with the Wide IP. |
| **pool_lb_mode** | Load-balancing method used across pools. |
| **ttl** | TTL applied to DNS responses. |
| **aliases** | DNS aliases associated with the Wide IP. |


## Examples

```yaml
- name: Create a Wide IP for app.example.com
  bigip_gtm_wide_ip:
    name: app.example.com
    response_type: a
    pool_lb_mode: round-robin
    pools:
      - name: app_pool
        order: 0
        ratio: 2
      - name: app_pool_backup
        order: 1
        ratio: 1
    ttl: 60
    description: "Global app entry point"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Enable persistence for a Wide IP
  bigip_gtm_wide_ip:
    name: app.example.com
    persistence: enabled
    persist_cidr_ipv4: 24
    persist_cidr_ipv6: 56
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a Wide IP
  bigip_gtm_wide_ip:
    name: legacy.example.com
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



