# bigip_remote_syslog


## Description

The `bigip_remote_syslog` module configures remote syslog settings on BIG-IP devices. It manages the list of remote syslog servers, their transport protocols, ports, and log facilities. This enables centralized logging to external syslog collectors for auditing, troubleshooting, and compliance. The module can add, update, or remove remote syslog destinations and adjust global logging behavior without manual GUI or TMSH interaction.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string | Identifier for the remote syslog configuration or server entry, if applicable. |
| **remote_servers** | **Type:** list | List of remote syslog servers to configure. Each item can include host, port, and protocol. |
| **remote_servers/host** | **Type:** string | Hostname or IP address of the remote syslog server. |
| **remote_servers/port** | **Type:** integer | UDP/TCP port for syslog messages (commonly 514). |
| **remote_servers/protocol** | **Choices:** udp, tcp, tcp+tls | Transport protocol to use when sending syslog messages. |
| **facility** | **Type:** string | Syslog facility to use for messages (for example, `local0`, `local1`). |
| **state** | **Choices:** present, absent | `present` ensures the remote syslog configuration exists; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **remote_servers** | The list of remote syslog servers configured after the task. |
| **facility** | Facility used for outbound syslog messages. |
| **changed** | Indicates whether the remote syslog configuration was altered. |


## Examples


```yaml
- name: Configure two remote syslog servers over UDP
  bigip_remote_syslog:
    remote_servers:
      - host: 192.0.2.10
        port: 514
        protocol: udp
      - host: logs.example.com
        port: 514
        protocol: udp
    facility: local0
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure remote syslog over TCP with TLS
  bigip_remote_syslog:
    remote_servers:
      - host: secure-logs.example.com
        port: 6514
        protocol: tcp+tls
    facility: local1
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove all remote syslog configuration
  bigip_remote_syslog:
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



