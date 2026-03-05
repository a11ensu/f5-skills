# bigip_smtp


## Description

The `bigip_smtp` module configures SMTP settings on BIG-IP devices. These settings control how the system sends email notifications, such as alerts or reports, through an external SMTP server. The module allows you to define the mail server, sender address, authentication details, and connection security options, ensuring that BIG-IP-generated emails are delivered reliably and securely to administrators or monitoring systems.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string | Name of the SMTP configuration profile, if applicable. |
| **server** | **Type:** string | Hostname or IP address of the SMTP server. |
| **port** | **Type:** integer | SMTP port (commonly 25, 465, or 587). |
| **from_address** | **Type:** string | Default sender email address used by BIG-IP when sending mail. |
| **username** | **Type:** string | Username for SMTP authentication, if required. |
| **password** | **Type:** string | Password for SMTP authentication. |
| **use_tls** | **Choices:** yes, no | Whether to use TLS/SSL when connecting to the SMTP server. |
| **state** | **Choices:** present, absent | `present` ensures the SMTP configuration is set; `absent` removes or resets it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **server** | SMTP server configured on the BIG-IP. |
| **port** | Port used for SMTP communication. |
| **from_address** | Sender address used for system emails. |
| **use_tls** | Indicates whether TLS is enabled for SMTP. |
| **changed** | Shows whether the SMTP configuration was modified. |


## Examples


```yaml
- name: Configure SMTP server for alerts
  bigip_smtp:
    server: smtp.example.com
    port: 587
    from_address: bigip-alerts@example.com
    username: bigip_smtp_user
    password: secret_password
    use_tls: yes
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure SMTP relay without authentication
  bigip_smtp:
    server: smtp-relay.internal
    port: 25
    from_address: bigip@example.com
    use_tls: no
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove SMTP configuration
  bigip_smtp:
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



