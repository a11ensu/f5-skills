# Sending multiple declarations in a single request (BIG-IQ)

## Description

This example shows how to send multiple AS3 declarations in a single request to BIG-IQ. The payload is an array of AS3 declarations, each with its own Tenants and Applications, allowing batch deployment and management.

## Examples

- Explanation of the example:
  - Top-level JSON is an array (`[...]`);
  - First declaration:
    - Tenant "TenantA" with Application "App1";
  - Second declaration:
    - Tenant "TenantB" with Application "App2";
  - Intended for BIG-IQ AS3 endpoint which accepts multiple declarations per request.

```json
[
  {
    "class": "AS3",
    "action": "deploy",
    "declaration": {
      "class": "ADC",
      "schemaVersion": "3.0.0",
      "TenantA": {
        "class": "Tenant",
        "App1": {
          "class": "Application",
          "template": "generic",
          "service": {
            "class": "Service_HTTP",
            "virtualAddresses": [
              "10.0.6.10"
            ],
            "virtualPort": 80,
            "pool": "poolA"
          },
          "poolA": {
            "class": "Pool",
            "monitors": [
              "http"
            ],
            "members": [
              {
                "servicePort": 80,
                "serverAddresses": [
                  "192.0.2.70"
                ]
              }
            ]
          }
        }
      }
    }
  },
  {
    "class": "AS3",
    "action": "deploy",
    "declaration": {
      "class": "ADC",
      "schemaVersion": "3.0.0",
      "TenantB": {
        "class": "Tenant",
        "App2": {
          "class": "Application",
          "template": "generic",
          "service": {
            "class": "Service_HTTP",
            "virtualAddresses": [
              "10.0.6.20"
            ],
            "virtualPort": 80,
            "pool": "poolB"
          },
          "poolB": {
            "class": "Pool",
            "monitors": [
              "http"
            ],
            "members": [
              {
                "servicePort": 80,
                "serverAddresses": [
                  "192.0.2.80"
                ]
              }
            ]
          }
        }
      }
    }
  }
]
```

## Tested json templates

---

