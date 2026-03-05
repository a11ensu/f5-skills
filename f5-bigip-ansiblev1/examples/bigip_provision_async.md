# bigip_provision_async


## Description

The `bigip_provision_async` module manages BIG-IP module provisioning using asynchronous operations. It is designed for long-running provisioning tasks that may require a device reboot or significant system changes. The module initiates provisioning changes and optionally waits for completion, allowing playbooks to continue or periodically check status without blocking. This is useful in large environments or when automating multi-step deployments that depend on module provisioning state.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **module** | **Type:** string<br>**Required:** yes | Name of the BIG-IP module to manage (for example, `ltm`, `gtm`, `asm`, `apm`, `afm`). |
| **level** | **Choices:** none, minimum, nominal, dedicated | Desired provisioning level for the module. |
| **state** | **Choices:** present, absent | `present` ensures the module is provisioned at the specified level; `absent` de-provisions the module. |
| **wait** | **Choices:** yes, no<br>**Default:** yes | Whether to wait for the asynchronous provisioning task to complete before returning. |
| **timeout** | **Type:** integer | Maximum time in seconds to wait for completion when `wait` is enabled. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **module** | The BIG-IP module that was targeted for provisioning. |
| **level** | The requested provisioning level. |
| **task_id** | Identifier of the asynchronous provisioning task on the BIG-IP. |
| **status** | Status of the asynchronous operation (for example, `in-progress`, `completed`, `failed`). |
| **changed** | Indicates if a provisioning change was initiated. |


## Examples


```yaml
- name: Start asynchronous provisioning of APM at nominal level
  bigip_provision_async:
    module: apm
    level: nominal
    wait: no
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Provision ASM asynchronously and wait for completion
  bigip_provision_async:
    module: asm
    level: minimum
    wait: yes
    timeout: 1800
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Deprovision GTM/DNS asynchronously
  bigip_provision_async:
    module: gtm
    state: absent
    wait: no
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



