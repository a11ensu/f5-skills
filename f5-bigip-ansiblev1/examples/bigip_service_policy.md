# bigip_service_policy


## Description

The `bigip_service_policy` module manages service policies on BIG-IP systems. Service policies define per-virtual-server behaviors such as connection limits, rate shaping, and protocol-specific options. This module enables you to create, update, or delete service policies, configure rules and actions, and associate them with relevant traffic flows. It is useful for enforcing consistent service characteristics across multiple virtual servers.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the service policy. |
| **description** | **Type:** string | Human-readable description of the service policy. |
| **rules** | **Type:** list | List of rules within the service policy, each defining conditions and actions. |
| **rules/name** | **Type:** string | Name of the rule. |
| **rules/actions** | **Type:** list | Actions applied when rule conditions are met (for example, connection limits, logging). |
| **state** | **Choices:** present, absent | `present` creates or updates the service policy; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the service policy managed. |
| **rules** | The rules configured within the service policy. |
| **changed** | Indicates whether the service policy configuration was modified. |


## Examples


```yaml
- name: Create a basic service policy with connection limit
  bigip_service_policy:
    name: limit_conns_policy
    description: Limit connections per client
    rules:
      - name: limit_conns_rule
        actions:
          - type: connection
            max_concurrent: 100
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update service policy description
  bigip_service_policy:
    name: limit_conns_policy
    description: Updated description for connection limits
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a service policy
  bigip_service_policy:
    name: old_policy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



