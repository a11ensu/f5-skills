# Using traceResponse to enable traces in AS3 responses

## Description

This example shows how to use the `trace` or `traceResponse` property in an AS3 declaration to request detailed trace information in the deployment response. This is useful for debugging and understanding how AS3 interprets your declaration.

## Examples

- Explanation of the example:
  - Top-level `class: "AS3"` includes `"trace": true`;
  - Simple Tenant "TraceTenant" with Application "App1";
  - HTTP service and pool defined as usual;
  - Response from AS3 will include trace details.

```json
{
  "class": "AS3",
  "action": "deploy",
  "trace": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "TraceTenant": {
      "class": "Tenant",
      "App1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.16.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.180"
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

