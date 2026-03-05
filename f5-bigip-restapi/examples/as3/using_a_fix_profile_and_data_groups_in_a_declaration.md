# Using a FIX profile and data groups in a declaration

## Description

This declaration configures a FIX (Financial Information eXchange) TCP service using a FIX profile and external data groups. It shows how to reference a FIX profile and associate address/data group lists for FIX message handling.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_03";
  - Application "A1";
    - FIX TCP service "fix_service" on 10.0.3.10:9876;
      - Uses TCP profile `/Common/fix-tcp` (or `/Common/tcp`);
      - Uses FIX profile "fix_profile";
      - Pool "fix_pool" with FIX servers;
    - FIX_Profile "fix_profile":
      - References address data group "fix_allow_list";
      - References string data group "fix_tag_map";
    - Data_Group "fix_allow_list":
      - Type "addr";
      - Contains allowed source addresses;
    - Data_Group "fix_tag_map":
      - Type "string";
      - Contains tag mappings or other FIX-related strings;
    - Pool "fix_pool":
      - Monitored by "tcp";
      - Members: 192.0.3.10:9876 and 192.0.3.11:9876.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-03",
    "label": "Using a FIX profile and data groups in a declaration",
    "remark": "FIX service with FIX profile and data groups",
    "Sample_nonhttp_03": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "fix_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.3.10"
          ],
          "virtualPort": 9876,
          "profileTCP": {
            "bigip": "/Common/tcp"
          },
          "profileFIX": {
            "use": "fix_profile"
          },
          "pool": "fix_pool"
        },
        "fix_profile": {
          "class": "FIX_Profile",
          "description": "FIX profile using data groups",
          "allowedFrom": {
            "use": "fix_allow_list"
          },
          "tagMap": {
            "use": "fix_tag_map"
          }
        },
        "fix_allow_list": {
          "class": "Data_Group",
          "keyDataType": "addr",
          "records": [
            {
              "key": "192.0.3.0/24"
            },
            {
              "key": "10.10.10.0/24"
            }
          ]
        },
        "fix_tag_map": {
          "class": "Data_Group",
          "keyDataType": "string",
          "records": [
            {
              "key": "SenderCompID",
              "value": "49"
            },
            {
              "key": "TargetCompID",
              "value": "56"
            }
          ]
        },
        "fix_pool": {
          "class": "Pool",
          "monitors": [
            "tcp"
          ],
          "members": [
            {
              "servicePort": 9876,
              "serverAddresses": [
                "192.0.3.10",
                "192.0.3.11"
              ]
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates


