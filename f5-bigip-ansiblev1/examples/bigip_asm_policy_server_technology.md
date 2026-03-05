# bigip_asm_policy_server_technology


## Description

The `bigip_asm_policy_server_technology` module configures server technology settings for ASM policies on BIG-IP. It allows you to specify the underlying web server, framework, database, and operating system technologies used by the protected application. These settings help ASM select appropriate attack signatures and parsing behaviors, improving detection accuracy and reducing false positives by tailoring the policy to the application stack.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **policy_name** | **Type:** string<br>**Required:** yes | Name of the ASM policy whose server technologies will be managed. |
| **partition** | **Type:** string<br>**Default:** Common | Partition where the ASM policy resides. |
| **server_technologies** | **Type:** list of strings<br>**Required:** yes | List of server technologies to enable (for example, `Apache`, `IIS`, `PHP`, `MySQL`, `Linux`). |
| **state** | **Choices:** present, absent<br>**Default:** present | `present` ensures the specified technologies are configured; `absent` clears them from the policy. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **policy_name** | Name of the ASM policy whose server technologies were managed. |
| **partition** | Partition where the policy resides. |
| **server_technologies** | Effective list of server technologies configured on the policy. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Set server technologies for Linux/Apache/PHP stack
  bigip_asm_policy_server_technology:
    policy_name: webapp_policy
    server_technologies:
      - Linux
      - Apache
      - PHP
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure Windows/IIS/.NET server technologies
  bigip_asm_policy_server_technology:
    policy_name: portal_policy
    server_technologies:
      - Windows
      - IIS
      - ASP.NET
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Clear all server technologies from policy
  bigip_asm_policy_server_technology:
    policy_name: legacy_policy
    server_technologies: []
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks

