# bigip_profile_sip


## Description

The `bigip_profile_sip` module manages SIP profiles on F5 BIG-IP devices. SIP profiles define how BIG-IP processes Session Initiation Protocol (SIP) signaling, including header manipulation, message routing, persistence, and support for features such as SIP over TCP or UDP. By using this module, administrators can configure SIP-aware load balancing for VoIP and real-time communications, ensuring proper handling of dialogs, registrations, and high-availability scenarios.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | User-defined description of the SIP profile. |
| **dialog_aware** | **Choices:** yes, no | Enables dialog-aware load balancing and persistence. |
| **insert_record_route** | **Choices:** yes, no | Inserts a Record-Route header for SIP messages. |
| **name** | **Type:** string<br>**Required:** yes | Name of the SIP profile. |
| **parent** | **Type:** string | Parent SIP profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **srtp** | **Choices:** enabled, disabled | Enables or disables support for SRTP-related attributes. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **description** | Description set on the profile. |
| **dialog_aware** | Indicates if dialog-aware mode is enabled. |
| **insert_record_route** | Indicates if Record-Route insertion is enabled. |
| **name** | Name of the SIP profile managed. |
| **partition** | Partition where the profile is configured. |
| **srtp** | Indicates if SRTP support is enabled. |


## Examples


```yaml
- name: Create SIP profile for VoIP service
  bigip_profile_sip:
    name: sip_voip_profile
    description: SIP profile for VoIP load balancing
    parent: sip
    dialog_aware: yes
    insert_record_route: yes
    srtp: enabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Disable SRTP on SIP profile
  bigip_profile_sip:
    name: sip_voip_profile
    srtp: disabled
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove SIP profile
  bigip_profile_sip:
    name: old_sip_profile
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



