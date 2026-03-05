# Specifying a GSLB virtual server name in a declaration

## Description

This AS3 declaration shows how to explicitly specify a GSLB virtual server name when defining members of a GSLB pool. The GSLB_Server contains a list of virtualServers with `name`, `address`, and `port`, and the GSLB_Pool refers to those virtual servers using the `virtualServer` field.

## Examples

- Explanation of the example:
  - Tenant "Sample_gslb_vsname_01";
  - Application "A1";
    - GSLB Data Center "dc_europe";
    - GSLB Server "server_paris":
      - Device at `192.0.2.30`;
      - Two virtual servers:
        - `vs_web_01` at `203.0.113.10:80`;
        - `vs_web_02` at `203.0.113.11:80`;
    - GSLB Pool "pool_web_eu":
      - Members referencing virtual servers by name:
        - Member for `vs_web_01`;
        - Member for `vs_web_02`;
    - GSLB Wide IP "wideip_web_eu":
      - Domain `web-eu.example.com`;
      - Uses "pool_web_eu".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-vsname-example-01",
    "label": "Specifying a GSLB virtual server name",
    "remark": "Example showing explicit virtual server names in GSLB pools",
    "Sample_gslb_vsname_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dc_europe": {
          "class": "GSLB_Data_Center"
        },
        "server_paris": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_europe"
          },
          "devices": [
            {
              "address": "192.0.2.30"
            }
          ],
          "virtualServers": [
            {
              "name": "vs_web_01",
              "address": "203.0.113.10",
              "port": 80
            },
            {
              "name": "vs_web_02",
              "address": "203.0.113.11",
              "port": 80
            }
          ]
        },
        "pool_web_eu": {
          "class": "GSLB_Pool",
          "resourceType": "a",
          "members": [
            {
              "server": {
                "use": "server_paris"
              },
              "virtualServer": "vs_web_01"
            },
            {
              "server": {
                "use": "server_paris"
              },
              "virtualServer": "vs_web_02"
            }
          ]
        },
        "wideip_web_eu": {
          "class": "GSLB_Domain",
          "domainName": "web-eu.example.com",
          "resourceRecordType": "A",
          "pools": [
            {
              "use": "pool_web_eu"
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

