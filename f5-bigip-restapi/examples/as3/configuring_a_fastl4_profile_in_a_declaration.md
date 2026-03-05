# Configuring a FastL4 profile in a declaration

## Description

Configures a FastL4 profile and applies it to a L4 virtual server for high-performance, low-latency forwarding of TCP/UDP traffic.

## Examples

- Explanation of the example:
  - Tenant named "Sample_fastl4";
  - Application named "fastL4App";
    - L4 service "fastService" on 10.0.22.10:80;
      - Pool "fast_pool";
      - FastL4 profile "fastl4_profile" of class "FastL4_Profile";
      - Attached via `profileL4`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "fastl4-01",
    "label": "Configuring a FastL4 profile",
    "remark": "Configuring a FastL4 profile in a declaration",
    "Sample_fastl4": {
      "class": "Tenant",
      "fastL4App": {
        "class": "Application",
        "fastService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.22.10"
          ],
          "virtualPort": 80,
          "pool": "fast_pool",
          "profileL4": {
            "use": "fastl4_profile"
          }
        },
        "fast_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.22.10"
              ]
            }
          ]
        },
        "fastl4_profile": {
          "class": "FastL4_Profile",
          "idleTimeout": 300
        }
      }
    }
  }
}
```

## Tested json templates

---

