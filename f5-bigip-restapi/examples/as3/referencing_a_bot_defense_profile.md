# Referencing a Bot Defense profile

## Description

This declaration shows how to attach an existing Bot Defense profile (Advanced WAF) to an HTTP virtual server that is also protected by a DoS profile. It references the Bot Defense profile using the `bigip` pointer and enables combined DoS and bot logging.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dos_06";
  - Folder of the Partition is named "bot_defense_reference";
    - A service address "vs_addr" with IP 10.0.6.10;
    - An HTTP virtual server "serviceMain" on 10.0.6.10:80:
      - Uses TCP and HTTP profiles;
      - References DoS profile "app_dos_profile";
      - References existing Bot Defense profile "/Common/my-bot-defense" via `profileBotDefense`;
      - Uses security log profile "dos_bot_log_profile";
    - A DoS profile "app_dos_profile" with application DoS enabled;
    - A Security Log Profile "dos_bot_log_profile" with:
      - DoS logging enabled;
      - Bot Defense logging enabled via `/Common/local-db-publisher`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "dos_06",
    "label": "Sample 6",
    "remark": "Referencing a Bot Defense profile",
    "Sample_dos_06": {
      "class": "Tenant",
      "bot_defense_reference": {
        "class": "Application",
        "template": "generic",
        "vs_addr": {
          "class": "Service_Address",
          "virtualAddress": "10.0.6.10"
        },
        "serviceMain": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            {
              "use": "vs_addr"
            }
          ],
          "virtualPort": 80,
          "profileTCP": {
            "bigip": "/Common/f5-tcp-progressive"
          },
          "profileHTTP": {
            "bigip": "/Common/http"
          },
          "profileDOS": {
            "use": "app_dos_profile"
          },
          "profileBotDefense": {
            "bigip": "/Common/my-bot-defense"
          },
          "securityLogProfiles": [
            {
              "use": "dos_bot_log_profile"
            }
          ]
        },
        "app_dos_profile": {
          "class": "DoS_Profile",
          "application": {
            "enabled": true
          }
        },
        "dos_bot_log_profile": {
          "class": "Security_Log_Profile",
          "dosProtection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            }
          },
          "botDefense": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            }
          }
        }
      }
    }
  }
}
```

## Tested json templates
