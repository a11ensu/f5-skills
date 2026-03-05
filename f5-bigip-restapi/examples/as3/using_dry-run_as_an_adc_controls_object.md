# Using dry-run as an ADC Controls object

## Description

This declaration uses `controls` at the ADC level to enable `dryRun`, so the BIG-IP validates the declaration without applying changes. It’s useful for preflight checks.

## Examples

- Explanation of the example:
  - ADC object includes `"controls": { "dryRun": true }`;
  - Tenant "DryRunTenant" with simple Application;
  - No configuration is actually deployed when submitted.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "controls": {
      "class": "Controls",
      "dryRun": true
    },
    "DryRunTenant": {
      "class": "Tenant",
      "App1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.25.10"
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
                "192.0.2.251"
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

