# Using a Security log profile with Application Security

## Description

Demonstrates how to configure a Security Log profile and associate it with an Application Security (ASM) policy within an AS3 declaration. This controls where and how security events are logged.

## Examples

- Explanation of the example:
  - Tenant named "Sample_security_log";
  - Application named "secApp";
    - HTTPS virtual server "service" on 10.0.10.10:443;
      - Pool "web_pool";
      - WAF policy referenced via `policyWAF`;
      - Security Log profile "security_log_profile" attached via `profileSecurityLog`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "security-log-01",
    "label": "Using a Security log profile with Application Security",
    "remark": "Using a Security log profile with Application Security",
    "Sample_security_log": {
      "class": "Tenant",
      "secApp": {
        "class": "Application",
        "template": "https",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": {
            "bigip": "/Common/clientssl"
          },
          "policyWAF": {
            "bigip": "/Common/my_asm_policy"
          },
          "profileSecurityLog": {
            "use": "security_log_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.10.10"
              ]
            }
          ]
        },
        "security_log_profile": {
          "class": "Security_Log_Profile",
          "application": {
            "localStorage": {
              "enabled": true
            }
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

