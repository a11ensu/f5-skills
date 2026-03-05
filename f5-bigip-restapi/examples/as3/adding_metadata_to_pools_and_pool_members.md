# Adding metadata to pools and pool members

## Description

This declaration adds metadata at both pool and pool-member levels using the `metadata` property. It can be used for tagging, ownership, or integration with external systems.

## Examples

- Explanation of the example:
  - Tenant "Sample_poolmeta_01";
  - Application "A1";
    - Pool "web_pool" with metadata:
      - `"serviceTier": "gold"`;
    - Member metadata:
      - `"role": "primary"` for the first member;
      - `"role": "secondary"` for the second member;
    - HTTP service "service" uses "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_poolmeta_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.31.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "metadata": {
            "serviceTier": "gold"
          },
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.3.10"
              ],
              "metadata": {
                "role": "primary"
              }
            },
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.3.11"
              ],
              "metadata": {
                "role": "secondary"
              }
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates
