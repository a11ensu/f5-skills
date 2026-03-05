# bigip_gtm_pool_member


## Description

The `bigip_gtm_pool_member` module manages individual members of GTM (DNS) pools on F5 BIG-IP systems. A GTM pool member typically represents a specific GTM virtual server within a pool. Use this module to add, modify, or remove pool members, control their enabled/disabled state, set ratios for weighted load balancing, and tune member-specific limits, allowing precise control over how traffic is distributed among endpoints in a GTM pool.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the pool member. |
| **enabled** | **Choices:** yes, no<br>**Default:** yes | Whether this pool member is enabled for load balancing. |
| **limit_max_bps** | **Type:** integer | Maximum bits per second allowed to this member. |
| **limit_max_bps_status** | **Choices:** enabled, disabled | Enables or disables enforcement of `limit_max_bps`. |
| **limit_max_connections** | **Type:** integer | Maximum concurrent connections for this member. |
| **limit_max_connections_status** | **Choices:** enabled, disabled | Enables or disables enforcement of `limit_max_connections`. |
| **limit_max_pps** | **Type:** integer | Maximum packets per second allowed to this member. |
| **limit_max_pps_status** | **Choices:** enabled, disabled | Enables or disables enforcement of `limit_max_pps`. |
| **member_order** | **Type:** integer | Order of the member within the pool for global-availability or ordered methods. |
| **name** | **Type:** string<br>**Required:** yes | Name of the GTM virtual server that acts as the pool member (for example, `server:vs_name`). |
| **partition** | **Default:** Common | Partition where the pool and member reside. |
| **pool** | **Type:** string<br>**Required:** yes | Name of the GTM pool to which this member belongs. |
| **priority_group** | **Type:** integer | Priority group for the member when using priority-based load balancing. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **ratio** | **Type:** integer | Load balancing ratio for this member when ratio-based methods are used. |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the member exists in the pool; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | Name of the GTM pool member (virtual server). |
| **pool** | Name of the GTM pool containing this member. |
| **enabled** | Whether the member is enabled. |
| **ratio** | Effective ratio used for load balancing. |
| **limits** | Dictionary of connection, bandwidth, and packet limits applied to the member. |
| **member_order** | Effective order of the member in the pool. |


## Examples

```yaml
- name: Add a GTM pool member with ratio
  bigip_gtm_pool_member:
    pool: app_pool
    name: "dc1-bigip:app_vs_443"
    ratio: 2
    description: "Primary DC member"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable a GTM pool member and set limits
  bigip_gtm_pool_member:
    pool: app_pool
    name: "dc2-bigip:app_vs_443"
    enabled: no
    limit_max_connections: 50000
    limit_max_connections_status: enabled
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a GTM pool member
  bigip_gtm_pool_member:
    pool: app_pool
    name: "dc3-bigip:app_vs_443"
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



