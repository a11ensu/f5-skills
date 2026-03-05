# bigip_firewall_rule


## Description

The `bigip_firewall_rule` module manages individual AFM firewall rules. Rules define match conditions (source, destination, service, protocol) and actions (accept, drop, reject) within a firewall policy or rule list. This module lets you create, update, or delete rules, set their position, enable logging, and reference address/port lists, enabling granular and ordered control of network traffic.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **action** | **Choices:** accept, drop, reject | Action taken when the rule matches. |
| **destination** | **Type:** dict | Destination match criteria (address, port, lists). |
| **ip_protocol** | **Type:** string | IP protocol (for example, `tcp`, `udp`, `icmp`). |
| **log** | **Type:** bool | Enables logging for this rule when matched. |
| **name** | **Type:** string<br>**Required:** yes | Name of the firewall rule. |
| **partition** | **Default:** Common | Administrative partition where the rule resides. |
| **policy** | **Type:** string | Name of the firewall policy or rule list this rule belongs to. |
| **position** | **Type:** integer | Position/order of the rule within the policy or list. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **source** | **Type:** dict | Source match criteria (address, port, lists). |
| **state** | **Choices:** present, absent | `present` creates or updates the rule; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the firewall rule. |
| **action** | Action configured for the rule. |
| **position** | Position of the rule in the policy or list. |
| **log** | Indicates whether logging is enabled for the rule. |


## Examples


```yaml
- name: Create an allow rule for web traffic
  bigip_firewall_rule:
    name: allow_web
    policy: policy_web
    action: accept
    ip_protocol: tcp
    source:
      address_list: web_frontend_addrs
    destination:
      port_list: web_ports
    log: true
    position: 1
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a firewall rule
  bigip_firewall_rule:
    name: allow_web
    policy: policy_web
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



