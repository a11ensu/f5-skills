# bigip_policy_rule


## Description

The `bigip_policy_rule` module manages individual rules within an LTM policy on F5 BIG-IP devices. Rules define conditions that match specific traffic characteristics (such as host, URI, HTTP method, or headers) and actions that manipulate or route that traffic (such as selecting a pool, redirecting, or inserting headers). This module allows you to create, reorder, modify, or delete rules in an existing policy, enabling fine-grained, declarative control over application traffic behavior.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the rule within the policy. |
| **policy** | **Type:** string<br>**Required:** yes | Name of the parent policy that contains the rule. |
| **partition** | **Default:** Common | Partition of the policy and rule. |
| **description** | **Type:** string | Description of the rule. |
| **ordinal** | **Type:** int | Position of the rule in the policy evaluation order (lower is evaluated first). |
| **conditions** | **Type:** list | List of condition definitions for matching traffic (e.g., host, path, method). |
| **actions** | **Type:** list | List of actions taken when conditions are met (e.g., forward, select pool, redirect). |
| **state** | **Choices:** present, absent | Desired state of the rule. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the rule managed by the module. |
| **policy** | Parent policy name. |
| **partition** | Partition where the rule resides. |
| **description** | Description currently set on the rule. |
| **ordinal** | Effective ordinal of the rule in the policy. |
| **conditions** | List of conditions configured on the rule. |
| **actions** | List of actions configured on the rule. |
| **state** | Final state of the rule (`present` or `absent`). |


## Examples


```yaml
- name: Create a rule to route traffic by host
  bigip_policy_rule:
    name: host_routing_rule
    policy: http_forwarding_policy
    partition: Common
    ordinal: 10
    conditions:
      - type: http-host
        host: "app.example.com"
    actions:
      - type: forward
        pool: /Common/app_pool
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Add a redirect rule for HTTP to HTTPS
  bigip_policy_rule:
    name: redirect_to_https
    policy: http_forwarding_policy
    ordinal: 5
    conditions:
      - type: http-scheme
        values:
          - http
    actions:
      - type: http-redirect
        location: "https://%{http_host}%{http_uri}"
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove an obsolete rule
  bigip_policy_rule:
    name: old_rule
    policy: http_forwarding_policy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



