# Adding a route domain to a static pool member

## Description

This declaration assigns a specific route domain to static pool members by appending the route domain ID to the IP address (for example, `192.0.2.10%2`). It ensures traffic to the member uses the correct routing context.

## Examples

- Explanation of the example:
  - Tenant "Sample_rd_01";
  - Application "A1";
    - Pool "web_pool":
      - Member address `192.0.2.10%2` on port 80;
      - Uses route domain 2;
    - HTTP service "service" uses "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_rd_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.27.10"
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
                "192.0.2.10%2"
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

