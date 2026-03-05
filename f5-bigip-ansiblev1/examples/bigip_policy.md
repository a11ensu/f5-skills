# bigip_policy


## Description

The `bigip_policy` module manages Local Traffic Manager (LTM) policies on F5 BIG-IP systems. Policies define a set of ordered rules that inspect traffic and perform actions such as selecting pools, modifying headers, or redirecting requests. This module lets you create, update, publish, or delete policies, control their strategy (e.g., first-match or all-match), and attach them to virtual servers indirectly via other modules. It is central for implementing advanced, rule-based traffic steering and application delivery logic.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the policy. |
| **partition** | **Default:** Common | Partition the policy belongs to. |
| **description** | **Type:** string | Description of the policy. |
| **strategy** | **Choices:** first-match, all-match | Evaluation strategy for rules within the policy. |
| **controls** | **Type:** list | List of traffic types the policy controls (e.g., forwarding, http). |
| **requires** | **Type:** list | Features or protocols required (e.g., http, client-ssl). |
| **status** | **Choices:** published, draft | Status of the policy definition. |
| **state** | **Choices:** present, absent | Desired state of the policy. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the managed policy. |
| **partition** | Partition where the policy resides. |
| **description** | Current description of the policy. |
| **strategy** | Active evaluation strategy. |
| **controls** | Controls configured on the policy. |
| **requires** | Requirements associated with the policy. |
| **status** | Current status of the policy (draft or published). |
| **state** | Final state of the policy (`present` or `absent`). |


## Examples


```yaml
- name: Create an HTTP forwarding policy
  bigip_policy:
    name: http_forwarding_policy
    partition: Common
    description: "Policy for HTTP traffic steering"
    strategy: first-match
    controls:
      - forwarding
    requires:
      - http
    status: published
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Create a draft policy for testing
  bigip_policy:
    name: test_policy
    description: "Draft policy for testing new rules"
    strategy: all-match
    controls:
      - forwarding
    requires:
      - http
    status: draft
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove an unused policy
  bigip_policy:
    name: legacy_policy
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



