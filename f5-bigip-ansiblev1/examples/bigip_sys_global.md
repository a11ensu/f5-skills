# bigip_sys_global


## Description

The `bigip_sys_global` module manages global system settings on F5 BIG-IP devices. These settings include host-level attributes such as hostname, GUI preferences, console settings, and other global behavior flags. By automating the configuration of global parameters, you can standardize system behavior across multiple BIG-IP instances, improve compliance with operational standards, and avoid manual configuration drift over time.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **hostname** | **Type:** string | Sets the system hostname of the BIG-IP device. |
| **gui_setup** | **Choices:** enabled, disabled | Enables or disables the initial configuration utility (setup). |
| **gui_security_banner_text** | **Type:** string | Custom text for the GUI security banner. |
| **gui_security_banner** | **Choices:** enabled, disabled | Enables or disables the GUI security banner. |
| **console_timeout** | **Type:** integer | Timeout (in minutes) for console sessions. |
| **lcd_display** | **Choices:** enabled, disabled | Controls whether the LCD display is active on supported hardware. |
| **net_reboot** | **Choices:** enabled, disabled | Controls whether the device reboots on certain network changes. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **hostname** | The configured hostname of the system. |
| **gui_setup** | Whether the setup utility is enabled or disabled. |
| **gui_security_banner** | Whether the GUI security banner is enabled. |
| **gui_security_banner_text** | The text displayed in the GUI security banner. |
| **console_timeout** | The configured console timeout. |
| **lcd_display** | The state of the LCD display. |
| **net_reboot** | Whether net reboot behavior is enabled or disabled. |


## Examples


```yaml
- name: Set system hostname and enable GUI banner
  bigip_sys_global:
    hostname: bigip01.example.com
    gui_security_banner: enabled
    gui_security_banner_text: "Authorized access only."
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure console timeout and disable LCD display
  bigip_sys_global:
    console_timeout: 30
    lcd_display: disabled
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



