# Creating a GSLB pool

## Description

This AS3 declaration focuses on creating a GSLB pool with multiple members from different GSLB servers and data centers. It illustrates use of `GSLB_Pool` properties such as `resourceType`, `loadBalancingMode`, and member definitions referencing servers and virtual servers.

## Examples

- Explanation of the example:
  - Tenant "Sample_gslb_pool_01";
  - Application "A1";
    - Two data centers: "dc_east" and "dc_west";
    - Two GSLB servers:
      - "server_east" in "dc_east" with virtual server `vs_app_east` at `198.51.100.20:80`;
      - "server_west" in "dc_west" with virtual server `vs_app_west` at `198.51.100.30:80`;
    - GSLB pool "pool_app_global":
      - Type A record;
      - Round-robin load balancing;
      - Members:
        - `server_east/vs_app_east`;
        - `server_west/vs_app_west`;
    - Wide IP "wideip_app_global":
      - Domain `app-global.example.com`;
      - Uses "pool_app_global".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-pool-example-01",
    "label": "Creating a GSLB pool",
    "remark": "Example of creating a GSLB pool with multiple members",
    "Sample_gslb_pool_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dc_east": {
          "class": "GSLB_Data_Center"
        },
        "dc_west": {
          "class": "GSLB_Data_Center"
        },
        "server_east": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_east"
          },
          "devices": [
            {
              "address": "192.0.2.40"
            }
          ],
          "virtualServers": [
            {
              "name": "vs_app_east",
              "address": "198.51.100.20",
              "port": 80
            }
          ]
        },
        "server_west": {
          "class": "GSLB_Server",
          "dataCenter": {
            "use": "dc_west"
          },
          "devices": [
            {
              "address": "192.0.2.50"
            }
          ],
          "virtualServers": [
            {
              "name": "vs_app_west",
              "address": "198.51.100.30",
              "port": 80
            }
          ]
        },
        "pool_app_global": {
          "class": "GSLB_Pool",
          "resourceType": "a",
          "loadBalancingMode": "round-robin",
          "members": [
            {
              "server": {
                "use": "server_east"
              },
              "virtualServer": "vs_app_east"
            },
            {
              "server": {
                "use": "server_west"
              },
              "virtualServer": "vs_app_west"
            }
          ]
        },
        "wideip_app_global": {
          "class": "GSLB_Domain",
          "domainName": "app-global.example.com",
          "resourceRecordType": "A",
          "pools": [
            {
              "use": "pool_app_global"
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

