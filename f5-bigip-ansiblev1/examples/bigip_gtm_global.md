# bigip_gtm_global


## Description

The `bigip_gtm_global` module manages global GTM (DNS) settings on F5 BIG-IP devices. It allows configuration of system-wide options affecting all GTM objects, such as load-balancing defaults, synchronization and statistics collection, logging behavior, and metrics thresholds. Use this module to standardize GTM behavior across the device, tune performance and failover responsiveness, and ensure that DNS resolution policies are consistently applied across all managed zones and pools.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **load_balancing_decision_log_verbosity** | **Choices:** disabled, basic, verbose | Controls the verbosity of logging for GTM load-balancing decisions. |
| **synchronization** | **Choices:** enabled, disabled | Enables or disables GTM configuration synchronization with other GTM systems in the sync group. |
| **statistics_interval** | **Type:** integer | Interval, in seconds, at which GTM collects statistics. |
| **max_concurrent_dns_queries** | **Type:** integer | Maximum number of concurrent DNS queries that GTM will process. |
| **log_publisher** | **Type:** string | Specifies the log publisher to use for GTM-related logs. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present<br>**Default:** present | Ensures the specified global GTM settings are applied. |


## Return Values

| Key | Description |
| --- | --- |
| **load_balancing_decision_log_verbosity** | The configured GTM decision logging level. |
| **synchronization** | Whether GTM synchronization is enabled. |
| **statistics_interval** | The statistics collection interval in seconds. |
| **max_concurrent_dns_queries** | The maximum number of concurrent DNS queries configured. |
| **log_publisher** | The log publisher used for GTM logs. |


## Examples

```yaml
- name: Configure basic GTM global settings
  bigip_gtm_global:
    synchronization: enabled
    statistics_interval: 300
    max_concurrent_dns_queries: 20000
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Enable verbose GTM decision logging with a specific publisher
  bigip_gtm_global:
    load_balancing_decision_log_verbosity: verbose
    log_publisher: /Common/local-db-publisher
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



