# Referencing existing iRules LX Profiles

## Description

Shows how to reference existing iRules LX profiles in an AS3 declaration, attaching them to an HTTP service to extend functionality using Node.js-based iRules LX.

## Examples

- Explanation of the example:
  - Tenant named "Sample_iruleslx";
  - Application named "lxApp";
    - HTTP virtual server "service" on 10.0.13.10:80;
      - Pool "web_pool";
      - Existing iRules LX profile referenced via `profileILX` with a BIG‑IP path.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "iruleslx-01",
    "label": "Referencing existing iRules LX Profiles",
    "remark": "Referencing existing iRules LX Profiles",
    "Sample_iruleslx": {
      "class": "Tenant",
      "lxApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.13.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileILX": {
            "bigip": "/Common/my_ilx_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.13.10"
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

