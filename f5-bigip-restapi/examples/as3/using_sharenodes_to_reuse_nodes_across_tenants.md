# Using shareNodes to reuse nodes across tenants

## Description

This declaration demonstrates the `shareNodes` ADC-level setting, which allows AS3-created nodes to be shared across Tenants. Nodes with the same IP/route-domain will be reused instead of recreated, reducing duplication.

## Examples

- Explanation of the example:
  - Top-level ADC object sets `"shareNodes": true`;
  - Tenant "Tenant1" with Application "App1":
    - Pool "pool1" with member `192.0.2.100`;
  - Tenant "Tenant2" with Application "App2":
    - Pool "pool2" with member `192.0.2.100`;
  - Because `shareNodes: true`, both pools share the same underlying node object.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "shareNodes": true,
    "Tenant1": {
      "class": "Tenant",
      "App1": {
        "class": "Application",
        "template": "generic",
        "service1": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 80,
          "pool": "pool1"
        },
        "pool1": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.100"
              ]
            }
          ]
        }
      }
    },
    "Tenant2": {
      "class": "Tenant",
      "App2": {
        "class": "Application",
        "template": "generic",
        "service2": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.20"
          ],
          "virtualPort": 80,
          "pool": "pool2"
        },
        "pool2": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.100"
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

