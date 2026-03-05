# Remote storage

## Description

Configures a Security Log profile that sends Application Security logs to a remote publisher (for example, a SIEM). The example shows enabling remote storage instead of local storage.

## Examples

- Explanation of the example:
  - Tenant named "Sample_security_log_remote";
  - Application named "secApp";
    - HTTPS virtual server "service" on 10.0.10.30:443;
      - Pool "web_pool";
      - Security Log profile "remote_security_log" with remote publisher;
      - Attached via `profileSecurityLog`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "security-log-remote",
    "label": "Security log remote storage",
    "remark": "Remote storage",
    "Sample_security_log_remote": {
      "class": "Tenant",
      "secApp": {
        "class": "Application",
        "template": "https",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.10.30"
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
            "use": "remote_security_log"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.10.30"
              ]
            }
          ]
        },
        "remote_security_log": {
          "class": "Security_Log_Profile",
          "application": {
            "remoteStorage": {
              "enabled": true,
              "logPublisher": {
                "bigip": "/Common/my-remote-publisher"
              }
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

