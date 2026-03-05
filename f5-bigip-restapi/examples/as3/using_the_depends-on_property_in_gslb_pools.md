# Using the depends-on property in GSLB pools

## Description

This AS3 declaration shows how to use the `dependsOn` property in a GSLB pool to ensure that related GSLB objects (such as servers and data centers) are created before the pool is deployed. This is useful when object creation order matters for successful configuration.

## Examples

- Explanation of the example:
  - Tenant "Sample_gslb_depends_01";
  - Application "A1";
    - Data center "dc_main";
    - GSLB server "server_main":
      - Device `192.0.2.60`;
      - Virtual server `vs_main` at `198.51.100.40:80`;
    - GSLB pool "pool_depends":
      - Type A record;
      - Has `dependsOn` referencing:
        - "dc_main";
        - "server_main";
      - Member: `server_main/vs_main`;
    - Wide IP "wideip_depends":
      - Domain `depends.example.com`;
      - Uses "pool_depends".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-depends-example-01",
    "label": "Using the depends-on property in GSLB pools",
    "remark": "Example showing dependsOn for GSLB_Pool object creation ordering",
    "Sample_gslb_depends_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dc_main": {
          "class": "GSLB_Data_Center"
        },
        "server_main": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_main"
          },
          "devices": [
            {
              "address": "192.0.2.60"
            }
          ],
          "virtualServers": [
            {
              "name": "vs_main",
              "address": "198.51.100.40",
              "port": 80
            }
          ]
        },
        "pool_depends": {
          "class": "GSLB_Pool",
          "resourceType": "a",
          "dependsOn": [
            "dc_main",
            "server_main"
          ],
          "members": [
            {
              "server": {
                "use": "server_main"
              },
              "virtualServer": "vs_main"
            }
          ]
        },
        "wideip_depends": {
          "class": "GSLB_Domain",
          "domainName": "depends.example.com",
          "resourceRecordType": "A",
          "pools": [
            {
              "use": "pool_depends"
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

