# Configuring a SNAT pool

## Description

This declaration creates a SNAT pool and assigns it to a virtual service. SNAT pools provide a set of source addresses that the BIG-IP can use when performing source NAT.

## Examples

- Explanation of the example:
  - Tenant "Sample_snatpool_01";
  - Application "A1";
    - SNAT pool "snat_pool_app" with addresses:
      - `203.0.113.10`, `203.0.113.11`;
    - HTTP service "service":
      - Virtual `10.0.20.10:80`;
      - `snat` references "snat_pool_app";
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_snatpool_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "snat_pool_app": {
          "class": "SNAT_Pool",
          "snatAddresses": [
            "203.0.113.10",
            "203.0.113.11"
          ]
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.20.10"
          ],
          "virtualPort": 80,
          "snat": {
            "use": "snat_pool_app"
          },
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.220"
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

---

