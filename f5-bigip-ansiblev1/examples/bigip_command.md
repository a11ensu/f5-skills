# bigip_command


## Description

The `bigip_command` module executes arbitrary commands on F5 BIG-IP devices. It supports both tmsh and bash commands, capturing their output for use in playbooks. The module can run commands in check mode, handle complex multi-line inputs, and optionally fail on non-zero exit codes. This is useful for ad hoc tasks, troubleshooting, data collection, and operations that are not yet modeled by dedicated Ansible modules.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **commands** | **Type:** list<br>**Required:** yes | List of commands to run on the BIG-IP. Each item is a string. |
| **chdir** | **Type:** string | Directory to change to before running the command (for bash commands). |
| **warn** | **Type:** bool<br>**Default:** yes | If yes, warns when using non-idempotent commands. |
| **wait_for** | **Type:** list | List of conditions to wait for in the command output. |
| **match** | **Choices:** any, all<br>**Default:** all | Whether all or any `wait_for` conditions must be met. |
| **retries** | **Type:** integer<br>**Default:** 1 | Number of retries to check the `wait_for` conditions. |
| **interval** | **Type:** integer<br>**Default:** 1 | Interval in seconds between retries. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **stdout** | List of command standard output strings, one per command. |
| **stdout_lines** | List of lists, where each sublist is the output of a command split into lines. |
| **stderr** | List of command standard error strings, one per command. |
| **rc** | List of return codes from each command. |
| **changed** | Indicates whether any changes were made (usually `false` unless command changes state). |


## Examples


```yaml
- name: Show BIG-IP version
  bigip_command:
    commands:
      - show sys version
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Run bash command to list log files
  bigip_command:
    commands:
      - run util bash -c "ls -1 /var/log"
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Wait for configuration sync to complete
  bigip_command:
    commands:
      - show cm sync-status
    wait_for:
      - result[0] contains "In Sync"
    retries: 10
    interval: 6
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

