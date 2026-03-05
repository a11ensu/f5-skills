# Using ignoreChanges on resources referenced by URL

## Description

This declaration demonstrates the `ignoreChanges` property for objects whose content is pulled from an external URL. It prevents AS3 from reapplying changes when the remote resource changes, unless explicitly updated in the declaration.

## Examples

- Explanation of the example:
  - Tenant "Sample_ignore_01";
  - Application "A1";
    - iRule "external_rule":
      - `url` points to external source;
      - `ignoreChanges: true` to ignore remote changes;
    - HTTP service uses "external_rule".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_ignore_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "external_rule": {
          "class": "iRule",
          "url": "https://example.com/irules/rule1.tcl",
          "ignoreChanges": true
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.29.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "iRules": [
            {
              "use": "external_rule"
            }
          ]
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.254"
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

