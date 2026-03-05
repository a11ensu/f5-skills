# Local storage

## Description

Shows how to configure a Security Log profile that logs Application Security events to local storage (the BIG‑IP system). This is useful for small deployments or lab environments.

## Examples

- Explanation of the example:
  - Tenant named "Sample_security_log_local";
  - Application named "secApp";
    - HTTPS virtual server "service" on 10.0.10.20:443;
      - Pool "web_pool";
      - Security Log profile "local_security_log" with local storage enabled;
      - Attached via `profileSecurityLog`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "security-log-local",
    "label": "Security log local storage",
    "remark": "Local storage",
    "Sample_security_log_local": {
      "class": "Tenant",
      "secApp": {
        "class": "Application",
        "template": "https",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.10.20"
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
            "use": "local_security_log"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.10.20"
              ]
            }
          ]
        },
        "local_security_log": {
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

