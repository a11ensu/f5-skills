# Referencing pools and iRules in a declaration

## Description

This example shows how to reference existing BIG-IP pools and iRules from AS3 declarations using the `bigip` pointer, alongside AS3-managed objects. It combines AS3-created resources with pre-existing configuration.

## Examples

- Explanation of the example:
  - Tenant "Sample_irule_01";
  - Application "A1";
    - HTTP service "service":
      - Virtual `10.0.14.10:80`;
      - Uses an existing pool `/Common/existing_pool`;
      - Attaches existing iRule `/Common/existing_irule`;
    - No AS3-managed pool in this example.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_irule_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.14.10"
          ],
          "virtualPort": 80,
          "pool": {
            "bigip": "/Common/existing_pool"
          },
          "iRules": [
            {
              "bigip": "/Common/existing_irule"
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

