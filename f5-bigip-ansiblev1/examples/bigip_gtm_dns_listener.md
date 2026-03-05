# bigip_gtm_dns_listener


## Description

The `bigip_gtm_dns_listener` module configures DNS listeners on F5 BIG-IP GTM/DNS systems. DNS listeners are specialized virtual servers that receive DNS queries over UDP and/or TCP and forward them to the DNS services on the BIG-IP. Use this module to create, modify, or delete listeners, control which VLANs they listen on, configure address and port, and manage DNS profiles and logging, ensuring that DNS traffic is properly accepted and processed by the BIG-IP DNS subsystem.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **address** | **Type:** string<br>**Required:** yes | IP address on which the DNS listener will listen for DNS queries. |
| **allow_wildcard_zones** | **Choices:** yes, no | Enables or disables wildcard zone behavior for this listener, if supported. |
| **description** | **Type:** string | Description of the DNS listener. |
| **name** | **Type:** string<br>**Required:** yes | Name of the DNS listener. |
| **partition** | **Default:** Common | Partition where the DNS listener resides. |
| **port** | **Type:** integer<br>**Default:** 53 | Port on which the listener accepts DNS queries. |
| **protocol** | **Choices:** udp, tcp, udp-tcp | Protocol(s) the listener will accept. |
| **profiles** | **Type:** list | List of profiles (e.g. DNS, TCP, UDP) to associate with the listener. |
| **source_address_translation** | **Type:** string | Source address translation configuration (for example, `automap`). |
| **vlans** | **Type:** list | List of VLANs on which this listener will receive traffic. |
| **vlans_enabled** | **Choices:** yes, no | When `yes`, restricts listener to specified VLANs; when `no`, listens on all VLANs. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the DNS listener exists with the specified settings; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **address** | IP address on which the listener is configured. |
| **name** | Name of the DNS listener. |
| **partition** | Partition where the listener is created. |
| **port** | Port number used by the listener. |
| **protocol** | Protocol(s) configured for the listener. |
| **profiles** | Profiles attached to the listener. |
| **vlans** | VLANs on which the listener is active. |
| **vlans_enabled** | Indicates if the listener is restricted to specific VLANs. |


## Examples

```yaml
- name: Create a UDP/TCP DNS listener on 10.0.0.10:53
  bigip_gtm_dns_listener:
    name: dns_listener_1
    address: 10.0.0.10
    port: 53
    protocol: udp-tcp
    profiles:
      - /Common/dns
      - /Common/udp
      - /Common/tcp
    vlans:
      - /Common/external
    vlans_enabled: yes
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a TCP-only DNS listener on a non-standard port
  bigip_gtm_dns_listener:
    name: dns_listener_tcp_1053
    address: 10.0.0.20
    port: 1053
    protocol: tcp
    profiles:
      - /Common/dns
      - /Common/tcp
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a DNS listener
  bigip_gtm_dns_listener:
    name: dns_listener_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



