# bigip_ltm_global


## Description

The `bigip_ltm_global` module manages global Local Traffic Manager (LTM) settings on F5 BIG-IP systems. It allows you to configure system-wide behaviors that affect all virtual servers and pools, such as default persistence, reselect behavior, connection limits, SNAT defaults, and other global tuning parameters. Using this module, you can standardize traffic-handling policies across devices and maintain consistent behavior in large-scale environments.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **default_persistence_profile** | **Type:** string | Name of the default persistence profile applied when none is specified on a virtual server. |
| **default_snat** | **Choices:** none, automap | Global default SNAT behavior when not overridden at the virtual server level. |
| **reselect_tries** | **Type:** integer | Number of times the system attempts to reselect a pool member after a failure. |
| **max_retries** | **Type:** integer | Maximum number of connection retries for failed connections. |
| **eviction_policy** | **Type:** string | Global eviction policy for managing connection table limits. |
| **syncookies** | **Type:** bool | Enable or disable global SYN cookie protection. |
| **log_publisher** | **Type:** string | Default LTM log publisher for traffic-related logs. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |
| **state** | **Choices:** present | Ensures global LTM settings match the provided values. |


## Return Values


| Key | Description |
| --- | --- |
| **default_persistence_profile** | Effective global default persistence profile. |
| **default_snat** | Effective global SNAT setting. |
| **reselect_tries** | Configured number of reselection attempts. |
| **max_retries** | Configured connection retry limit. |
| **syncookies** | Indicates whether global SYN cookies are enabled. |
| **log_publisher** | Global LTM log publisher in use. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Configure global LTM defaults
  bigip_ltm_global:
    default_persistence_profile: /Common/source_addr
    default_snat: automap
    reselect_tries: 3
    max_retries: 5
    syncookies: true
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Set global LTM log publisher
  bigip_ltm_global:
    log_publisher: /Common/security_logs_publisher
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



