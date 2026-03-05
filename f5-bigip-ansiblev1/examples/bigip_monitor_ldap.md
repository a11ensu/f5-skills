# bigip_monitor_ldap


## Description

The `bigip_monitor_ldap` module manages LDAP health monitors on F5 BIG-IP LTM systems. LDAP monitors connect to LDAP servers and optionally perform bind operations and queries to verify directory service availability. This module allows you to create, modify, and remove LDAP monitors, configure base DNs, filters, send/receive strings, credentials, intervals, and timeouts, as well as destination and security options, enabling accurate health checks for LDAP-dependent applications.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **base** | **Type:** string | LDAP base DN used for search operations. |
| **debug** | **Type:** string | Debug options for the LDAP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing LDAP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the LDAP monitor. |
| **destination** | **Type:** string | IP address and port for LDAP connections, in `IP:port` or `*:port` format. |
| **filter** | **Type:** string | LDAP search filter to apply when querying. |
| **interval** | **Type:** integer | Interval in seconds between LDAP health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the LDAP monitor. |
| **password** | **Type:** string | Password used for LDAP bind operations. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String expected in the LDAP response to consider it up. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **security** | **Choices:** none, ssl, tls | Specifies the security mode for LDAP (plain, SSL, or StartTLS). |
| **send** | **Type:** string | LDAP request payload or operation string, if applicable. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the LDAP request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for LDAP health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |
| **username** | **Type:** string | Username (bind DN) used for LDAP bind operations. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between LDAP health checks. |
| **timeout** | Timeout configured for LDAP requests. |
| **base** | Base DN used in LDAP searches. |
| **filter** | LDAP search filter configured for the monitor. |
| **security** | Security mode (none, ssl, tls) used by the monitor. |


## Examples


```yaml
- name: Create an LDAP monitor
  bigip_monitor_ldap:
    name: ldap_monitor_1
    destination: "198.51.100.20:389"
    base: "dc=example,dc=com"
    filter: "(objectClass=*)"
    username: "cn=monitor,dc=example,dc=com"
    password: "secret"
    interval: 10
    timeout: 31
    description: "LDAP bind and search health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update LDAP monitor to use StartTLS
  bigip_monitor_ldap:
    name: ldap_monitor_1
    security: tls
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove LDAP monitor
  bigip_monitor_ldap:
    name: ldap_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



