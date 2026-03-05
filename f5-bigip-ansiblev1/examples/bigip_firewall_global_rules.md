# bigip_firewall_global_rules


## Description

The `bigip_firewall_global_rules` module manages global firewall rule settings on BIG-IP AFM. Global rules are evaluated before context-specific policies and can allow, reject, or drop traffic based on criteria like source, destination, and service. This module enables you to configure global allow/deny lists, default actions, and logging behavior, providing a top-level security posture for all traffic through the device.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **default_action** | **Choices:** accept, drop, reject | Default action for unmatched traffic. |
| **log_rule_matches** | **Type:** bool | Enables logging for global rule matches. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **rules** | **Type:** list | List of global firewall rules with match conditions and actions. |
| **state** | **Choices:** present | `present` ensures global rules configuration matches the provided parameters. |


## Return Values


| Key | Description |
| --- | --- |
| **default_action** | Effective default action for unmatched traffic. |
| **rules** | Global rules configured on the device. |
| **log_rule_matches** | Indicates whether logging is enabled for global rules. |


## Examples


```yaml
- name: Configure global firewall rules
  bigip_firewall_global_rules:
    default_action: drop
    log_rule_matches: true
    rules:
      - name: allow_dns
        action: accept
        protocol: udp
        dst_port: 53
      - name: allow_icmp
        action: accept
        protocol: icmp
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



