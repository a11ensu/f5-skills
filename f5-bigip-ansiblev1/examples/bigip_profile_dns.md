# bigip_profile_dns


## Description

The `bigip_profile_dns` module manages DNS profiles on F5 BIG-IP systems. DNS profiles control how BIG-IP handles DNS queries and responses, including protocol settings, caching behavior, DNSSEC options, and logging. By configuring DNS profiles, administrators can tune performance for high query volumes, enable advanced features like DNS express or DNSSEC validation, and apply security controls to protect authoritative or recursive DNS services delivered through BIG-IP GTM/DNS modules.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **allow_query** | **Type:** list | List of networks or addresses allowed to query. |
| **cache** | **Choices:** enabled, disabled | Enables or disables DNS caching for the profile. |
| **description** | **Type:** string | User-defined description of the DNS profile. |
| **dnssec** | **Choices:** enabled, disabled | Enables or disables DNSSEC processing. |
| **logging** | **Choices:** enabled, disabled | Enables or disables DNS logging for this profile. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DNS profile. |
| **parent** | **Type:** string | Parent DNS profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **recursion** | **Choices:** enabled, disabled | Enables or disables recursive query handling. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |
| **unhandled_query_action** | **Choices:** allow, reject, drop | Action for queries that do not match specific rules. |


## Return Values


| Key | Description |
| --- | --- |
| **allow_query** | List of networks allowed to query. |
| **cache** | Indicates if caching is enabled. |
| **description** | Description set on the profile. |
| **dnssec** | Indicates if DNSSEC is enabled. |
| **logging** | Logging setting for the DNS profile. |
| **name** | Name of the DNS profile managed. |
| **partition** | Partition where the profile is configured. |
| **recursion** | Indicates if recursion is enabled. |
| **unhandled_query_action** | Action taken for unhandled queries. |


## Examples


```yaml
- name: Create DNS profile with caching and DNSSEC
  bigip_profile_dns:
    name: dns_auth_profile
    description: Authoritative DNS profile with DNSSEC
    cache: enabled
    dnssec: enabled
    recursion: disabled
    logging: enabled
    allow_query:
      - 0.0.0.0/0
    unhandled_query_action: allow
    parent: dns
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Create recursive DNS profile for internal clients
  bigip_profile_dns:
    name: dns_recursive_internal
    description: Recursive DNS for internal network
    cache: enabled
    dnssec: disabled
    recursion: enabled
    allow_query:
      - 10.0.0.0/8
    unhandled_query_action: drop
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove DNS profile
  bigip_profile_dns:
    name: old_dns_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



