# Original Declaration

## Description

This example shows an original AS3 declaration used to demonstrate a subsequent modification (for example, when showing PATCH behavior). It defines a single Tenant and Application with a basic HTTP service and pool.

## Examples

- Explanation of the example:
  - Tenant "ExampleTenant";
  - Application "App1";
    - HTTP service "service" on `10.0.9.10:80`;
    - Pool "web_pool" with two members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "ExampleTenant": {
      "class": "Tenant",
      "App1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.9.10"
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
                "192.0.2.110",
                "192.0.2.111"
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

