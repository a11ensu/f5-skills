# Advertising a route for a Service Address

## Description

This declaration illustrates how to advertise a virtual address into a routing domain (for example, via Route Advertisement) using the `Service_Address` class. It decouples the virtual address object from the virtual server and enables route advertisement properties.

## Examples

- Explanation of the example:
  - Tenant "Sample_route_01";
  - Application "A1";
    - `Service_Address` object "vipAddress":
      - IP `10.0.4.10`;
      - `routeAdvertisement: "selective"`;
    - `Service_HTTP` "service":
      - Uses the `Service_Address` via `virtualAddresses` reference;
      - Listens on port 80;
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_route_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "vipAddress": {
          "class": "Service_Address",
          "virtualAddress": "10.0.4.10",
          "routeAdvertisement": "selective"
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            {
              "use": "vipAddress"
            }
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.50",
                "192.0.2.51"
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

