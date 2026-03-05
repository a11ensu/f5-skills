# bigip_log_publisher


## Description

The `bigip_log_publisher` module manages log publishers on F5 BIG-IP systems. Log publishers group one or more log destinations and are referenced by profiles or modules (such as ASM, AFM, or APM) to control where logs are sent. This module lets you create, update, or delete log publishers and manage their associated destinations for consistent logging configurations.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the log publisher. |
| **destinations** | **Type:** list | List of log destinations to associate with this publisher. |
| **partition** | **Default:** Common | Partition in which to manage the log publisher. |
| **state** | **Choices:** present, absent | Whether the log publisher should exist or be removed. |
| **description** | **Type:** string | User-defined description for the log publisher. |
| **provider** | **Type:** dict | Connection details for the BIG-IP. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the log publisher. |
| **destinations** | List of log destinations associated with the publisher. |
| **partition** | Partition where the publisher resides. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create a log publisher with two destinations
  bigip_log_publisher:
    name: security_logs_publisher
    destinations:
      - /Common/remote_syslog_1
      - /Common/hsl_pool_dest
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update log publisher to use a single destination
  bigip_log_publisher:
    name: security_logs_publisher
    destinations:
      - /Common/remote_syslog_1
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a log publisher
  bigip_log_publisher:
    name: security_logs_publisher
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
