# Creating an internal virtual service

## Description

This declaration creates an internal virtual server using the `internal` property. Internal virtuals are only accessible from within the BIG-IP (for example, from other virtuals or iRules), not from external clients.

## Examples

- Explanation of the example:
  - Tenant "Sample_internal_01";
  - Application "A1";
    - HTTP service "internal_service":
      - `internal: true`;
      - Virtual address `10.0.12.10:80`;
      - Uses pool "internal_pool";
    - Pool "internal_pool" with one member.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_internal_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "internal_service": {
          "class": "Service_HTTP",
          "internal": true,
          "virtualAddresses": [
            "10.0.12.10"
          ],
          "virtualPort": 80,
          "pool": "internal_pool"
        },
        "internal_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 8080,
              "serverAddresses": [
                "192.0.2.150"
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

