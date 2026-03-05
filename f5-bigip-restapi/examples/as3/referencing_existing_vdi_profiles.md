# Referencing existing VDI profiles

## Description

This AS3 declaration configures an HTTP virtual server that uses existing APM VDI (Virtual Desktop Infrastructure) profiles on the BIG‑IP. The declaration references pre‑configured VDI profiles by their full BIG‑IP paths, enabling remote desktop or application publishing scenarios while leaving VDI profile creation and maintenance outside AS3.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_05";
  - Application named "A1";
    - HTTP virtual server "service" on 10.0.10.10:443 (HTTPS offload implied);
      - References an existing Access profile "/Common/myVDIAccessProfile";
      - References an existing VDI profile "/Common/myVDIProfile";
      - A pool "rdp_pool" with default TCP monitor;
        - Pool members 192.0.10.10:3389 and 192.0.10.11:3389.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "example-vdi-1",
    "label": "Referencing existing VDI profiles",
    "remark": "Attach existing VDI and Access profiles to a virtual server",
    "Sample_http_05": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 443,
          "pool": "rdp_pool",
          "profileAccess": {
            "bigip": "/Common/myVDIAccessProfile"
          },
          "profileVdi": {
            "bigip": "/Common/myVDIProfile"
          }
        },
        "rdp_pool": {
          "class": "Pool",
          "monitors": [
            "tcp"
          ],
          "members": [
            {
              "servicePort": 3389,
              "serverAddresses": [
                "192.0.10.10",
                "192.0.10.11"
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

