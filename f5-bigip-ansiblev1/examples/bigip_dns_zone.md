# bigip_dns_zone


## Description

The `bigip_dns_zone` module manages DNS zones on F5 BIG-IP systems running GTM/DNS services. Zones define authoritative DNS data served by the BIG-IP, including primary/secondary roles, zone transfer settings, and associated DNS profiles. This module enables you to create, update, or delete zones, configure their type (master, slave, hint), specify masters and notify settings, and integrate with DNSSEC and views for granular DNS control.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **dnssec_enabled** | **Type:** bool | Enables or disables DNSSEC for the zone. |
| **dns_profile** | **Type:** string | Name of the DNS profile applied to this zone. |
| **masters** | **Type:** list | List of master servers for secondary/slave zones. |
| **name** | **Type:** string<br>**Required:** yes | Fully qualified domain name of the zone (for example, `example.com`). |
| **notify** | **Type:** bool | When `yes`, sends NOTIFY messages to secondary servers upon zone changes. |
| **partition** | **Default:** Common | Administrative partition where the zone resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present, absent | `present` ensures the zone exists; `absent` removes it. |
| **type** | **Choices:** master, slave, hint | Specifies whether the zone is authoritative (master), secondary (slave), or hint. |
| **view** | **Type:** string | DNS view in which this zone is defined, if applicable. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | The DNS zone name managed by the module. |
| **type** | Zone type (master, slave, hint). |
| **dnssec_enabled** | Indicates whether DNSSEC is active for the zone. |
| **masters** | List of master servers for slave zones. |


## Examples


```yaml
- name: Create a master DNS zone
  bigip_dns_zone:
    name: example.com
    type: master
    dns_profile: /Common/dns
    dnssec_enabled: false
    notify: true
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a slave DNS zone
  bigip_dns_zone:
    name: corp.example.com
    type: slave
    masters:
      - 192.0.2.10
      - 192.0.2.11
    notify: false
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a DNS zone
  bigip_dns_zone:
    name: example.com
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



