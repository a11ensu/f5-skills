# New Declaration

## Description

This example shows a modified AS3 declaration based on the "Original Declaration". It typically adds or changes objects (for example, adding another Application, a new service, or modifying pool members) to illustrate how AS3 processes updates.

## Examples

- Explanation of the example:
  - Same Tenant "ExampleTenant";
  - Original Application "App1" unchanged;
  - New Application "App2" added:
    - HTTP service "service2" on `10.0.9.20:80`;
    - Pool "web_pool2" with one member.

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
      },
      "App2": {
        "class": "Application",
        "template": "generic",
        "service2": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.9.20"
          ],
          "virtualPort": 80,
          "pool": "web_pool2"
        },
        "web_pool2": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.120"
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

