# Service Discovery for virtual servers in GSLB Servers

## Description

This AS3 declaration uses service discovery to populate GSLB Server virtual servers automatically based on LTM virtual servers on a target BIG-IP device. Instead of statically defining virtualServers in the GSLB_Server, it uses a `serviceDiscoveryType` and `tag` to dynamically discover and map them.

## Examples

- Explanation of the example:
  - Tenant named "Sample_gslb_sd_01";
  - Application "A1";
    - GSLB Data Center "dc_primary";
    - GSLB Server "server_primary":
      - Uses service discovery:
        - `serviceDiscoveryType: "tag"` (example);
        - Discovers LTM virtual servers tagged with `"gslb-app1"`;
      - Discovers virtual servers from BIG-IP device `192.0.2.20`;
    - GSLB Pool "pool_app_sd":
      - Members use discovered virtual servers from "server_primary";
    - GSLB Wide IP "wideip_app_sd":
      - Domain name `app-sd.example.com`;
      - Uses "pool_app_sd".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-sd-example-01",
    "label": "Service Discovery for virtual servers in GSLB Servers",
    "remark": "Example of using service discovery for GSLB Server virtual servers",
    "Sample_gslb_sd_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dc_primary": {
          "class": "GSLB_Data_Center"
        },
        "server_primary": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_primary"
          },
          "devices": [
            {
              "address": "192.0.2.20"
            }
          ],
          "serviceDiscoveryType": "tag",
          "tag": "gslb-app1"
        },
        "pool_app_sd": {
          "class": "GSLB_Pool",
          "resourceType": "a",
          "members": [
            {
              "server": {
                "use": "server_primary"
              },
              "virtualServerDiscoveryMode": "auto"
            }
          ]
        },
        "wideip_app_sd": {
          "class": "GSLB_Domain",
          "domainName": "app-sd.example.com",
          "resourceRecordType": "A",
          "pools": [
            {
              "use": "pool_app_sd"
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates

---

