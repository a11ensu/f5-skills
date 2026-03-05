# bigip_monitor_ftp


## Description

The `bigip_monitor_ftp` module manages FTP health monitors on F5 BIG-IP LTM systems. FTP monitors actively connect to FTP servers, perform a login (optionally with credentials), and optionally issue commands to verify that the FTP service is responsive. This module allows you to create, modify, and remove FTP monitors, configure send and receive strings, set intervals and timeouts, and control whether the monitor uses passive mode or specific destination settings for health checks.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Specifies debug options for the FTP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing FTP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the FTP monitor. |
| **destination** | **Type:** string | IP address and port for the monitor traffic, in `IP:port` or `*:port` format. |
| **interval** | **Type:** integer | Interval in seconds between health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual intervention to mark the resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the FTP monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String the monitor expects to receive from the server to consider it up. |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | String the monitor sends to the FTP server, such as commands. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the monitor times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for health checks. |
| **up\_interval** | **Type:** integer | Interval in seconds between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | The configured interval between FTP health checks. |
| **timeout** | The timeout value for the monitor. |
| **send** | The send string used by the monitor. |
| **recv** | The receive string used to determine health. |
| **reverse** | Indicates whether the reverse option is enabled. |


## Examples


```yaml
- name: Create an FTP monitor
  bigip_monitor_ftp:
    name: ftp_monitor_1
    send: "USER anonymous\r\nPASS guest@\r\nQUIT\r\n"
    recv: "230"
    interval: 10
    timeout: 31
    description: "FTP login health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update FTP monitor receive string
  bigip_monitor_ftp:
    name: ftp_monitor_1
    recv: "220"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove FTP monitor
  bigip_monitor_ftp:
    name: ftp_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



