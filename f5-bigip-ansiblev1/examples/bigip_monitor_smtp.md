# bigip_monitor_smtp


## Description

The `bigip_monitor_smtp` module manages SMTP health monitors on F5 BIG-IP LTM systems. SMTP monitors connect to mail servers, perform SMTP handshakes, and optionally send commands to validate that the service is accepting connections and responding correctly. This module allows you to create, modify, and remove SMTP monitors, configure send and receive strings, intervals, timeouts, and destination settings, ensuring reliable health checks for SMTP-based services.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **debug** | **Type:** string | Debug options for the SMTP monitor, if supported. |
| **defaults\_from** | **Type:** string | Name of an existing SMTP monitor to inherit settings from. |
| **description** | **Type:** string | Description of the SMTP monitor. |
| **destination** | **Type:** string | IP address and port for SMTP connections, in `IP:port` or `*:port` format. |
| **domain** | **Type:** string | Domain name used in the SMTP HELO/EHLO command. |
| **interval** | **Type:** integer | Interval in seconds between SMTP health checks. |
| **manual\_resume** | **Type:** bool | When `yes`, requires manual action to mark a resource up after it is marked down. |
| **name** | **Type:** string<br>**Required:** yes | Name of the SMTP monitor. |
| **partition** | **Default:** Common | Device partition in which the monitor resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |
| **recv** | **Type:** string | String expected in the SMTP response (for example, `220`). |
| **reverse** | **Type:** bool | When `yes`, reverses the meaning of the receive string (match means down). |
| **send** | **Type:** string | SMTP commands to send, such as HELO and QUIT. |
| **state** | **Choices:** present, absent | `present` ensures the monitor exists; `absent` removes it. |
| **time\_until\_up** | **Type:** integer | Seconds a resource must pass checks before being marked up. |
| **timeout** | **Type:** integer | Seconds before the SMTP request times out and marks the resource down. |
| **transparent** | **Type:** bool | When `yes`, uses the client’s source IP address for SMTP health checks. |
| **up\_interval** | **Type:** integer | Interval between checks when the resource is marked up. |


## Return Values


| Key | Description |
| --- | --- |
| **interval** | Interval between SMTP health checks. |
| **timeout** | Timeout configured for SMTP requests. |
| **send** | SMTP command sequence used by the monitor. |
| **recv** | Receive string used to determine health. |
| **domain** | Domain name used in HELO/EHLO. |


## Examples


```yaml
- name: Create an SMTP monitor
  bigip_monitor_smtp:
    name: smtp_monitor_1
    destination: "203.0.113.30:25"
    domain: "example.com"
    send: "HELO example.com\r\nQUIT\r\n"
    recv: "220"
    interval: 10
    timeout: 31
    description: "SMTP greeting health check"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update SMTP monitor receive string
  bigip_monitor_smtp:
    name: smtp_monitor_1
    recv: "250"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove SMTP monitor
  bigip_monitor_smtp:
    name: smtp_monitor_1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



