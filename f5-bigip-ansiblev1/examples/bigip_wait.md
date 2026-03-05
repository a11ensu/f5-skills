# bigip_wait


## Description

The `bigip_wait` module waits for specific conditions on a BIG-IP device before continuing playbook execution. It can pause until certain objects (such as virtual servers, pools, or devices) reach a desired state, or until the device becomes reachable. This is useful after operations such as reboots, configuration changes, or failovers, ensuring that subsequent tasks run only when the BIG-IP is ready and in the expected state.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **timeout** | **Type:** integer<br>**Default:** 300 | Maximum time in seconds to wait for the condition. |
| **sleep** | **Type:** integer<br>**Default:** 5 | Interval in seconds between checks. |
| **msg** | **Type:** string | Custom message to display upon timeout. |
| **condition** | **Type:** string | Expression or condition describing what to wait for (for example, device status). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **elapsed** | Total time in seconds spent waiting. |
| **condition** | The condition that was being waited on. |
| **timeout** | Timeout value used. |
| **changed** | Always `false`; this module does not change configuration. |


## Examples


```yaml
- name: Wait for BIG-IP to be ready after reboot
  bigip_wait:
    timeout: 600
    sleep: 10
    condition: "device_ready"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Wait for a virtual server to become available
  bigip_wait:
    timeout: 300
    sleep: 5
    condition: "virtual_server:/Common/vs_http:available"
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
