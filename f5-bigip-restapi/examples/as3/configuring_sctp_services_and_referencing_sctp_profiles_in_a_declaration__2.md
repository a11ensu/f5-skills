# Configuring SCTP services and referencing SCTP profiles in a declaration

## Description

Demonstrates how to configure SCTP-based services and reference existing SCTP profiles in AS3. SCTP is commonly used in telecom signaling.

## Examples

- Explanation of the example:
  - Tenant named "Sample_sctp";
  - Application named "sctpApp";
    - L4 service "sctpService" on 10.0.18.10:2905;
      - Pool "sctp_pool";
      - Existing SCTP profile referenced via `profileSCTP`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "sctp-01",
    "label": "Configuring SCTP services and referencing SCTP profiles",
    "remark": "Configuring SCTP services and referencing SCTP profiles in a declaration",
    "Sample_sctp": {
      "class": "Tenant",
      "sctpApp": {
        "class": "Application",
        "sctpService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.18.10"
          ],
          "virtualPort": 2905,
          "pool": "sctp_pool",
          "profileSCTP": {
            "bigip": "/Common/my_sctp_profile"
          }
        },
        "sctp_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 2905,
              "serverAddresses": [
                "192.0.18.10"
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

