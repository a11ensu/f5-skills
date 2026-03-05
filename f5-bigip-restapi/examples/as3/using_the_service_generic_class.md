# Using the Service_Generic class

## Description

This declaration demonstrates the `Service_Generic` class, which provides a low-level, flexible way to define a virtual server with arbitrary L4/L7 profiles and options. It is useful when you need features not directly exposed by higher-level `Service_HTTP` or `Service_TCP` classes.

## Examples

- Explanation of the example:
  - Tenant named "Sample_generic_01";
  - Application "A1";
    - A `Service_Generic` virtual named "generic_service":
      - Listens on `10.0.1.10:8080`;
      - Uses TCP and HTTP profiles from `/Common`;
      - Enables source address translation using automap;
      - References a pool "generic_pool";
    - Pool "generic_pool":
      - Uses HTTP monitor;
      - Has two pool members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_generic_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "generic_service": {
          "class": "Service_Generic",
          "virtualAddresses": [
            "10.0.1.10"
          ],
          "virtualPort": 8080,
          "profileTCP": {
            "bigip": "/Common/tcp"
          },
          "profileHTTP": {
            "bigip": "/Common/http"
          },
          "snat": "auto",
          "pool": "generic_pool"
        },
        "generic_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 8080,
              "serverAddresses": [
                "192.0.2.20",
                "192.0.2.21"
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

