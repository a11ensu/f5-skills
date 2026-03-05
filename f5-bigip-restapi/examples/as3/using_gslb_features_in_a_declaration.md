# Using GSLB features in a declaration

## Description

This AS3 declaration demonstrates how to configure BIG-IP GSLB (DNS) objects, including a Data Center, a Server, a Pool, and a Wide IP, within a single tenant. It illustrates how GSLB objects relate: the Wide IP references a pool, which in turn references one or more virtual servers on GSLB servers.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_gslb_01";
  - Application named "A1";
    - A GSLB Data Center named "dc_seattle";
    - A GSLB Server named "server_sea_01" in that data center:
      - Represents a BIG-IP system at management address `192.0.2.10`;
      - Contains a virtual server `vs_app_01` at `198.51.100.10:80`;
    - A GSLB Pool named "pool_app_http":
      - Contains the member virtual server `server_sea_01/vs_app_01`;
    - A Wide IP named "wideip_app_http":
      - DNS name `app.example.com`;
      - Type A record;
      - Uses the pool "pool_app_http".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-example-01",
    "label": "Using GSLB features",
    "remark": "Example of configuring GSLB objects (Data Center, Server, Pool, Wide IP) via AS3",
    "Sample_gslb_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dc_seattle": {
          "class": "GSLB_Data_Center"
        },
        "server_sea_01": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_seattle"
          },
          "devices": [
            {
              "address": "192.0.2.10"
            }
          ],
          "virtualServers": [
            {
              "name": "vs_app_01",
              "address": "198.51.100.10",
              "port": 80
            }
          ]
        },
        "pool_app_http": {
          "class": "GSLB_Pool",
          "resourceType": "a",
          "members": [
            {
              "server": {
                "use": "server_sea_01"
              },
              "virtualServer": "vs_app_01"
            }
          ]
        },
        "wideip_app_http": {
          "class": "GSLB_Domain",
          "domainName": "app.example.com",
          "resourceRecordType": "A",
          "pools": [
            {
              "use": "pool_app_http"
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

