# bigip_provision


## Description

The `bigip_provision` module manages the provisioning level of software modules on F5 BIG-IP devices. It allows you to enable, disable, or adjust resource allocation (such as dedicated or nominal levels) for modules like LTM, GTM/DNS, ASM, APM, and others. This module ensures that the correct feature set is available on the device and helps maintain consistent provisioning across multiple BIG-IP systems in automated workflows.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **module** | **Type:** string<br>**Required:** yes | Name of the BIG-IP module to manage (for example, `ltm`, `gtm`, `asm`, `apm`, `afm`, `swg`, `avr`, `ilx`, etc.). |
| **level** | **Choices:** none, minimum, nominal, dedicated | Provisioning level for the specified module. `none` disables the module; other values control resource allocation and may trigger reboots. |
| **state** | **Choices:** present, absent | When `present`, ensures the specified provisioning level is set. When `absent`, de-provisions the module (equivalent to `level: none`). |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |
| **partition** | **Default:** Common | Device partition context; generally left as `Common` for provisioning. |
| **validate_certs** | **Choices:** yes, no | Whether to validate TLS certificates when connecting to the BIG-IP. Commonly disabled in lab environments. |


## Return Values


| Key | Description |
| --- | --- |
| **module** | The BIG-IP module that was provisioned or de-provisioned. |
| **level** | The resulting provisioning level applied to the module. |
| **changed** | Indicates if any changes were made to the device configuration. |
| **previous_level** | The provisioning level before the module was modified. |


## Examples


```yaml
- name: Provision LTM module at nominal level
  bigip_provision:
    module: ltm
    level: nominal
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Deprovision ASM module
  bigip_provision:
    module: asm
    level: none
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Ensure APM is provisioned at minimum level
  bigip_provision:
    module: apm
    level: minimum
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove GTM/DNS provisioning using state
  bigip_provision:
    module: gtm
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



