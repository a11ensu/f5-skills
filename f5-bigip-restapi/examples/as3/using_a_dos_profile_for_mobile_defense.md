# Using a DoS profile for Mobile Defense

## Description

This declaration configures a DoS profile specifically for Mobile Defense, enabling mobile-specific protections and attaching the profile to an HTTP virtual server. It also configures logging of Mobile Defense events through a Security Log Profile.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dos_02";
  - Folder of the Partition is named "mobile_defense_example";
    - A service address "vs_addr" with IP 10.0.2.10;
    - An HTTP virtual server "serviceMain" on 10.0.2.10:80:
      - Uses BIG-IP TCP and HTTP profiles;
      - References DoS profile "mobile_dos_profile";
      - Uses security log profile "mobile_dos_log_profile";
    - A DoS profile "mobile_dos_profile" with:
      - `mobileDefense.enabled` set to true;
      - Mobile Defense detection and mitigation thresholds configured;
    - A Security Log Profile "mobile_dos_log_profile" with:
      - DoS logging enabled for Mobile Defense events, using `/Common/local-db-publisher`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "dos_02",
    "label": "Sample 2",
    "remark": "Using a DoS profile for Mobile Defense",
    "Sample_dos_02": {
      "class": "Tenant",
      "mobile_defense_example": {
        "class": "Application",
        "template": "generic",
        "vs_addr": {
          "class": "Service_Address",
          "virtualAddress": "10.0.2.10"
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
            "use": "mobile_dos_profile"
          },
          "securityLogProfiles": [
            {
              "use": "mobile_dos_log_profile"
            }
          ]
        },
        "mobile_dos_profile": {
          "class": "DoS_Profile",
          "mobileDefense": {
            "enabled": true,
            "detectionThreshold": 1000,
            "mitigationThreshold": 2000
          }
        },
        "mobile_dos_log_profile": {
          "class": "Security_Log_Profile",
          "dosProtection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logMobileDefense": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

