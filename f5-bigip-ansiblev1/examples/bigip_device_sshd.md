# bigip_device_sshd


## Description

The `bigip_device_sshd` module manages SSHD (SSH daemon) settings on F5 BIG-IP systems. It controls how administrators access the device via SSH, including allowed ciphers, authentication methods, idle timeout, and listen port. This module helps enforce security and compliance policies by standardizing SSH access configuration across BIG-IP fleets.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **allow** | **Type:** list | List of IP addresses or networks allowed to connect via SSH. |
| **banner** | **Type:** string | Login banner text presented on SSH connection. |
| **inactivity_timeout** | **Type:** integer | Idle timeout in seconds before SSH sessions are disconnected. |
| **log_level** | **Choices:** QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, DEBUG3 | Logging level for SSHD. |
| **port** | **Type:** integer | TCP port on which SSHD listens. |
| **protocol** | **Choices:** 2 | SSH protocol version (typically 2 only). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **state** | **Choices:** present | `present` ensures SSHD settings match the provided parameters. |


## Return Values


| Key | Description |
| --- | --- |
| **port** | SSH port configured on the device. |
| **allow** | Networks or hosts allowed to connect. |
| **inactivity_timeout** | Idle timeout for SSH sessions. |
| **log_level** | Effective SSHD log level. |


## Examples


```yaml
- name: Harden SSHD configuration
  bigip_device_sshd:
    port: 22
    allow:
      - 10.0.0.0/24
      - 192.168.10.0/24
    inactivity_timeout: 600
    log_level: INFO
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



