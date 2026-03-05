# Using the include property to reference one section of a declaration in another section

## Description

This declaration demonstrates the `include` property, which allows you to reuse a section of JSON (for example, a base Application or object fragment) in multiple places in the declaration. This promotes reuse and consistency across services.

## Examples

- Explanation of the example:
  - Tenant "Sample_include_01";
  - Defines a reusable application fragment "BaseApp" under a special `Shared` tenant;
  - Tenant "Customer1" uses `include` to pull in "BaseApp":
    - Resulting Application "App1" inherits the service and pool defined in "BaseApp".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Shared": {
      "class": "Tenant",
      "BaseApp": {
        "class": "Application",
        "template": "generic",
        "baseService": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 80,
          "pool": "base_pool"
        },
        "base_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.130"
              ]
            }
          ]
        }
      }
    },
    "Customer1": {
      "class": "Tenant",
      "App1": {
        "include": {
          "tenant": "Shared",
          "application": "BaseApp"
        }
      }
    }
  }
}
```

## Tested json templates

---

