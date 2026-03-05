# bigip_sys_daemon_log_tmm


## Description

The `bigip_sys_daemon_log_tmm` module manages logging configuration for the Traffic Management Microkernel (TMM) daemon on F5 BIG-IP systems. It allows you to adjust log levels for various TMM facilities, control log destinations, and fine-tune verbosity for troubleshooting or compliance requirements. By automating TMM logging settings, you can ensure consistent logging behavior across devices and reduce manual configuration errors during operations or incident response.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **app_service** | **Type:** string | The application service to which the TMM logging configuration belongs, if any. |
| **description** | **Type:** string | User-defined description for the TMM logging configuration object. |
| **log_level** | **Choices:** debug, info, notice, warning, error, critical, alert, emergency | Specifies the overall log level for TMM messages. |
| **name** | **Type:** string<br>**Required:** yes | The name of the TMM logging configuration. |
| **partition** | **Default:** Common | Administrative partition in which the TMM logging object resides. |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the TMM logging configuration exists; when `absent`, removes it. |
| **facility** | **Type:** string | The TMM subsystem or facility for which logging is configured. |
| **destination** | **Type:** string | The log destination, such as a remote syslog server or local destination. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the TMM logging configuration object. |
| **description** | Description associated with the logging configuration. |
| **log_level** | Effective log level for TMM messages. |
| **facility** | TMM facility for which logging is configured. |
| **destination** | Destination where TMM logs are sent. |
| **partition** | Partition in which the logging configuration resides. |
| **state** | Final state of the logging configuration (`present` or `absent`). |


## Examples


```yaml
- name: Configure TMM logging at debug level to remote destination
  bigip_sys_daemon_log_tmm:
    name: tmm_debug_remote
    description: TMM debug logging to remote syslog
    facility: tmm
    log_level: debug
    destination: /Common/remote_syslog
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure TMM logging at warning level to local destination
  bigip_sys_daemon_log_tmm:
    name: tmm_warning_local
    facility: tmm
    log_level: warning
    destination: /Common/local_syslog
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a TMM logging configuration
  bigip_sys_daemon_log_tmm:
    name: tmm_debug_remote
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



