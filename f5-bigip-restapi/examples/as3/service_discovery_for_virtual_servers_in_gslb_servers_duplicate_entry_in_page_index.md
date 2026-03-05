# Service Discovery for virtual servers in GSLB Servers (Duplicate entry in page index)

## Description

This AS3 declaration is functionally the same as the earlier “Service Discovery for virtual servers in GSLB Servers” example, repeated due to a duplicate index entry. It again demonstrates using service discovery on a GSLB_Server to automatically populate virtual servers for use in a GSLB pool and Wide IP.

## Examples

- Explanation of the example:
  - Tenant "Sample_gslb_sd_02";
  - Application "A1";
    - GSLB Data Center "dc_secondary";
    - GSLB Server "server_secondary":
      - Device `192.0.2.70`;
      - Uses tag-based service discovery with tag `"gslb-app2"`;
    - GSLB Pool "pool_app_sd2":
      - Members discovered automatically from "server_secondary";
    - GSLB Wide IP "wideip_app_sd2":
      - Domain `app-sd2.example.com`;
      - Uses "pool_app_sd2".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-sd-example-02",
    "label": "Service Discovery for virtual servers in GSLB Servers (duplicate index entry)",
    "remark": "Duplicate example of service discovery for GSLB_Server virtual servers",
    "Sample_gslb_sd_02": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dc_secondary": {
          "class": "GSLB_Data_Center"
        },
        "server_secondary": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_secondary"
          },
          "devices": [
            {
              "address": "192.0.2.70"
            }
          ],
          "serviceDiscoveryType": "tag",
          "tag": "gslb-app2"
        },
        "pool_app_sd2": {
          "class": "GSLB_Pool",
          "resourceType": "a",
          "members": [
            {
              "server": {
                "use": "server_secondary"
              },
              "virtualServerDiscoveryMode": "auto"
            }
          ]
        },
        "wideip_app_sd2": {
          "class": "GSLB_Domain",
          "domainName": "app-sd2.example.com",
          "resourceRecordType": "A",
          "pools": [
            {
              "use": "pool_app_sd2"
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates
