# Configuring serviceDownImmediateAction on a virtual

## Description

This declaration configures the `serviceDownImmediateAction` property on a virtual server to control how the BIG-IP responds when the default pool is down (for example, rejecting connections immediately).

## Examples

- Explanation of the example:
  - Tenant "Sample_sdia_01";
  - Application "A1";
    - HTTP service "service":
      - Virtual `10.0.19.10:80`;
      - `serviceDownImmediateAction: "reset"` (or similar);
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_sdia_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.19.10"
          ],
          "virtualPort": 80,
          "serviceDownImmediateAction": "reset",
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
                "192.0.2.210"
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

