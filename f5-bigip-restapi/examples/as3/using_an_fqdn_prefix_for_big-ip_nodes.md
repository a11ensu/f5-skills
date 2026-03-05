# Using an FQDN prefix for BIG-IP nodes

## Description

This example uses FQDN-based nodes with a prefix, allowing AS3 to create nodes that resolve via DNS. It leverages the `FQDN_Node` class or FQDN settings on pool members.

## Examples

- Explanation of the example:
  - Tenant "Sample_fqdn_01";
  - Application "A1";
    - Pool "web_pool":
      - Members defined using `fqdn` property with prefix `web` and domain `example.com`;
      - BIG-IP resolves hostnames like `web1.example.com`, `web2.example.com`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_fqdn_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.21.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "fqdn": {
                "name": "web1.example.com"
              }
            },
            {
              "servicePort": 80,
              "fqdn": {
                "name": "web2.example.com"
              }
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

