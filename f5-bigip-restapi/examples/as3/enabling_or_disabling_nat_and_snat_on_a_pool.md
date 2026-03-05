# Enabling or disabling NAT and SNAT on a pool

## Description

This example configures per-pool NAT and SNAT settings using the `allowNat` and `allowSnat` properties on a Pool. It controls whether BIG-IP performs NAT/SNAT for traffic to that pool.

## Examples

- Explanation of the example:
  - Tenant "Sample_natpool_01";
  - Application "A1";
    - Pool "web_pool":
      - `allowNat: false`;
      - `allowSnat: false`;
    - HTTP service "service":
      - Virtual `10.0.24.10:80`;
      - Uses "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_natpool_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.24.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "allowNat": false,
          "allowSnat": false,
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.250"
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

