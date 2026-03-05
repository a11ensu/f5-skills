# bigip_virtual_server


## Description

The `bigip_virtual_server` module manages LTM virtual servers on F5 BIG-IP devices. Virtual servers define how client traffic is received and processed, including IP/port, protocol, profiles, pools, and persistence. This module allows you to create, modify, or remove virtual servers, associate them with pools and profiles, and control options such as SNAT, connection limits, and policies. Automating virtual server configuration is central to deploying and maintaining load-balanced applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the virtual server. |
| **partition** | **Default:** Common | Administrative partition for the virtual server. |
| **destination** | **Type:** string | Destination in the form `IP:port` or `IP%route-domain:port`. |
| **ip_protocol** | **Choices:** tcp, udp, http, all, others | IP protocol the virtual server listens on. |
| **pool** | **Type:** string | Default pool to which traffic is sent. |
| **profiles** | **Type:** list | List of profiles (for example, TCP, HTTP, SSL) attached to the virtual server. |
| **source** | **Type:** string | Source address or network allowed to connect. |
| **source_address_translation** | **Type:** string | SNAT configuration, such as `automap` or a specific SNAT pool. |
| **enabled** | **Choices:** yes, no | Whether the virtual server is enabled. |
| **description** | **Type:** string | User-defined description for the virtual server. |
| **policies** | **Type:** list | LTM policies applied to the virtual server. |
| **connection_limit** | **Type:** integer | Maximum concurrent connections allowed. |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the virtual server exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the virtual server. |
| **destination** | Destination address and port. |
| **partition** | Partition in which the virtual server resides. |
| **pool** | Default pool associated with the virtual server. |
| **profiles** | Profiles attached to the virtual server. |
| **source_address_translation** | SNAT configuration. |
| **enabled** | Whether the virtual server is enabled. |
| **policies** | Policies applied to the virtual server. |
| **connection_limit** | Connection limit configured. |
| **state** | Final state (`present` or `absent`). |


## Examples


```yaml
- name: Create an HTTP virtual server with automap SNAT
  bigip_virtual_server:
    name: vs_http
    destination: 203.0.113.20:80
    pool: /Common/web_pool
    ip_protocol: tcp
    profiles:
      - /Common/http
      - /Common/tcp
    source_address_translation: automap
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create an HTTPS virtual server with SSL profile
  bigip_virtual_server:
    name: vs_https
    destination: 203.0.113.21:443
    pool: /Common/web_pool
    ip_protocol: tcp
    profiles:
      - /Common/clientssl
      - /Common/http
      - /Common/tcp
    source_address_translation: automap
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Disable and remove a virtual server
  bigip_virtual_server:
    name: vs_http
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



