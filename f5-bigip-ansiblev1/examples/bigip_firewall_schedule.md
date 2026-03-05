# bigip_firewall_schedule


## Description

The `bigip_firewall_schedule` module manages AFM firewall schedules on BIG-IP systems. Schedules define time windows (days and hours) during which firewall rules are active, enabling time-based access control (for example, maintenance windows or business hours). This module allows you to create, update, or delete schedules and configure their recurring time periods for use in firewall rules.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the schedule. |
| **name** | **Type:** string<br>**Required:** yes | Name of the schedule. |
| **partition** | **Default:** Common | Administrative partition where the schedule resides. |
| **periods** | **Type:** list | List of time periods (day-of-week and start/stop times). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` creates or updates the schedule; `absent` removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the firewall schedule. |
| **periods** | Time periods configured in the schedule. |
| **description** | Description of the schedule. |


## Examples


```yaml
- name: Create a business-hours schedule
  bigip_firewall_schedule:
    name: business_hours
    description: "Weekday business hours"
    periods:
      - days: [ mon, tue, wed, thu, fri ]
        start_time: "08:00"
        end_time: "18:00"
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a firewall schedule
  bigip_firewall_schedule:
    name: business_hours
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
