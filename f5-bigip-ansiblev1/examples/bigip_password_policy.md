# bigip_password_policy


## Description

The `bigip_password_policy` module configures the local authentication password policy on F5 BIG-IP devices. It allows you to enforce security requirements such as minimum length, character complexity, password history, lockout thresholds, and expiration periods for local user accounts. By using this module, administrators can align BIG-IP password policies with organizational security standards and compliance frameworks, ensuring consistent and auditable password rules across devices without manual GUI configuration.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **minimum_length** | **Type:** int | Minimum allowed length for passwords. |
| **maximum_length** | **Type:** int | Maximum allowed length for passwords. |
| **password_history** | **Type:** int | Number of previous passwords to remember and disallow. |
| **required_lowercase** | **Type:** int | Minimum number of lowercase characters required. |
| **required_uppercase** | **Type:** int | Minimum number of uppercase characters required. |
| **required_numeric** | **Type:** int | Minimum number of numeric characters required. |
| **required_special** | **Type:** int | Minimum number of special characters required. |
| **max_login_failures** | **Type:** int | Maximum failed login attempts before lockout. |
| **lockout_duration** | **Type:** int | Lockout duration in minutes after exceeding failures. |
| **password_expiration** | **Type:** int | Number of days before passwords expire. |
| **warning_period** | **Type:** int | Number of days before expiration to start warning users. |
| **enforce_policy** | **Type:** bool | Enables or disables enforcement of the configured policy. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (host, user, password, server_port, validate_certs, etc.). |
| **state** | **Choices:** present | Ensures the password policy is configured as specified. |


## Return Values


| Key | Description |
| --- | --- |
| **minimum_length** | Effective minimum password length. |
| **maximum_length** | Effective maximum password length. |
| **password_history** | Number of previous passwords remembered. |
| **required_lowercase** | Required count of lowercase characters. |
| **required_uppercase** | Required count of uppercase characters. |
| **required_numeric** | Required count of numeric characters. |
| **required_special** | Required count of special characters. |
| **max_login_failures** | Configured maximum login failures. |
| **lockout_duration** | Lockout duration in minutes. |
| **password_expiration** | Password expiration period in days. |
| **warning_period** | Warning period before password expiration. |
| **enforce_policy** | Indicates whether the policy is enforced. |


## Examples


```yaml
- name: Enforce strong password policy
  bigip_password_policy:
    minimum_length: 12
    maximum_length: 64
    required_lowercase: 1
    required_uppercase: 1
    required_numeric: 1
    required_special: 1
    password_history: 5
    password_expiration: 90
    warning_period: 14
    max_login_failures: 5
    lockout_duration: 30
    enforce_policy: true
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Relax password policy for lab environment
  bigip_password_policy:
    minimum_length: 8
    required_lowercase: 0
    required_uppercase: 0
    required_numeric: 0
    required_special: 0
    password_history: 0
    enforce_policy: true
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



