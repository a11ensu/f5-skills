# Using Firewall (Carrier Grade) NAT features in a declaration

## Description

This declaration shows how to configure AFM Carrier Grade NAT (CGNAT) using AS3. It creates LSN pools with different translation types, enables CGNAT on a virtual server, and attaches AFM firewall logging for NAT-related events.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_02";
  - Folder (application) named "cgnat_example";
    - Creates two LSN pools: "lsn_pool_dynamic" (dynamic-translation) and "lsn_pool_pba" (port block allocation);
    - Configures a CGNAT profile "my_cgnat_profile" referencing the dynamic LSN pool;
    - Creates a security log profile "my_cgnat_log_profile" to log CGNAT events;
    - Defines a virtual server "cgnat_vs" listening on 10.0.2.10:0 with CGNAT profile and logging applied.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_02",
    "label": "Sample 2",
    "remark": "Using Firewall (Carrier Grade) NAT features in a declaration",
    "Sample_network_security_02": {
      "class": "Tenant",
      "cgnat_example": {
        "class": "Application",
        "template": "generic",
        "lsn_pool_dynamic": {
          "class": "LSN_Pool",
          "translation": "dynamic-translation",
          "members": [
            {
              "address": "203.0.113.10"
            },
            {
              "address": "203.0.113.11"
            }
          ]
        },
        "lsn_pool_pba": {
          "class": "LSN_Pool",
          "translation": "pba",
          "members": [
            {
              "address": "203.0.113.20"
            }
          ],
          "blockSize": 64,
          "blockIdleTimeout": 3600
        },
        "my_cgnat_profile": {
          "class": "LSN_Profile",
          "lsnPool": {
            "use": "lsn_pool_dynamic"
          },
          "hairpinMode": "enabled"
        },
        "my_cgnat_log_profile": {
          "class": "Security_Log_Profile",
          "network": {
            "logPublisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logTranslationFields": [
              "source",
              "destination",
              "translated-source",
              "translated-destination"
            ],
            "logTranslationEvents": [
              "nat44-creation",
              "nat44-deletion"
            ]
          }
        },
        "cgnat_vs": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.2.10"
          ],
          "virtualPort": 0,
          "lsn": {
            "use": "my_cgnat_profile"
          },
          "securityLogProfiles": [
            {
              "use": "my_cgnat_log_profile"
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

