# Using a DoS profile in a declaration

## Description

This AS3 declaration creates an L4 virtual server protected by a custom AFM DoS profile. The profile enables application-level DoS protection, attaches a Device DOS Configuration, and configures logging via a Security Log Profile. The DoS profile is then referenced by the virtual server to enforce protections.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dos_01";
  - Folder of the Partition is named "dos_profile_example";
    - A service address object "vs_addr" with IP 10.0.1.10;
    - A TCP virtual server "serviceMain" on 10.0.1.10:80:
      - Uses BIG-IP TCP profile "/Common/f5-tcp-progressive";
      - Uses BIG-IP HTTP profile "/Common/http";
      - References DoS profile "my_dos_profile" via `profileDOS`;
      - Uses security log profile "my_dos_log_profile" for DoS logging;
    - A Device DOS Config "my_device_dos_config" with:
      - Application DoS enabled;
    - A DoS profile "my_dos_profile" with:
      - `application.enabled` set to true;
      - `deviceConfig` referencing "my_device_dos_config";
    - A Security Log Profile "my_dos_log_profile" with:
      - DoS logging enabled and local-db-publisher as the publisher.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "dos_01",
    "label": "Sample 1",
    "remark": "Using a DoS profile in a declaration",
    "Sample_dos_01": {
      "class": "Tenant",
      "dos_profile_example": {
        "class": "Application",
        "template": "generic",
        "vs_addr": {
          "class": "Service_Address",
          "virtualAddress": "10.0.1.10"
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
            "use": "my_dos_profile"
          },
          "securityLogProfiles": [
            {
              "use": "my_dos_log_profile"
            }
          ]
        },
        "my_device_dos_config": {
          "class": "Device_DOS_Configuration",
          "application": {
            "enabled": true
          }
        },
        "my_dos_profile": {
          "class": "DoS_Profile",
          "application": {
            "enabled": true,
            "deviceConfig": {
              "use": "my_device_dos_config"
            }
          }
        },
        "my_dos_log_profile": {
          "class": "Security_Log_Profile",
          "dosProtection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logDoSApplication": true,
            "logDoSNetwork": true,
            "logDoSPacket": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

