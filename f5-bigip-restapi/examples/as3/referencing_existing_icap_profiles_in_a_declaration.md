# Referencing existing ICAP profiles in a declaration

## Description

This declaration references existing BIG-IP ICAP profiles from AS3 to build an ICAP service. It uses `Service_TCP` with ICAP-specific profiles and a pool of ICAP servers.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_10";
  - Application "A1";
    - TCP service "icap_service" on 10.0.10.10:1344;
      - Uses ICAP profile `/Common/icap` via `profileICAP`;
      - Uses TCP profile `/Common/tcp`;
      - Pool "icap_pool" with ICAP servers;
    - Pool "icap_pool":
      - Monitored by "tcp";
      - Members: 192.0.10.10:1344 and 192.0.10.11:1344.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-10",
    "label": "Referencing existing ICAP profiles in a declaration",
    "remark": "ICAP service using existing ICAP profile",
    "Sample_nonhttp_10": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "icap_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 1344,
          "profileTCP": {
            "bigip": "/Common/tcp"
          },
          "profileICAP": {
            "bigip": "/Common/icap"
          },
          "pool": "icap_pool"
        },
        "icap_pool": {
          "class": "Pool",
          "monitors": [
            "tcp"
          ],
          "members": [
            {
              "servicePort": 1344,
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


