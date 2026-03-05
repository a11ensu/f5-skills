# Referencing a PPTP profile in a declaration

## Description

Shows how to reference an existing PPTP profile in an AS3 declaration and attach it to a PPTP service.

## Examples

- Explanation of the example:
  - Tenant named "Sample_pptp";
  - Application named "pptpApp";
    - L4 service "pptpService" on 10.0.17.10:1723;
      - Pool "pptp_pool";
      - Existing PPTP profile referenced via `profilePPTP`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "pptp-01",
    "label": "Referencing a PPTP profile",
    "remark": "Referencing a PPTP profile in a declaration",
    "Sample_pptp": {
      "class": "Tenant",
      "pptpApp": {
        "class": "Application",
        "pptpService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.17.10"
          ],
          "virtualPort": 1723,
          "pool": "pptp_pool",
          "profilePPTP": {
            "bigip": "/Common/my_pptp_profile"
          }
        },
        "pptp_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 1723,
              "serverAddresses": [
                "192.0.17.10"
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

