# Configuring SCTP services and referencing SCTP profiles in a declaration

## Description

This declaration configures an SCTP-based service and references an SCTP profile. It shows how to use `Service_SCTP` along with a custom or existing SCTP profile and an SCTP pool.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_09";
  - Application "A1";
    - SCTP service "sctp_service" on 10.0.9.10:2905;
      - Uses SCTP profile "custom_sctp";
      - Pool "sctp_pool" with SCTP servers;
    - SCTP_Profile "custom_sctp":
      - `parentProfile` `/Common/sctp`;
      - Optional tuning parameters (e.g., `inboundStreams`, `outboundStreams`);
    - Pool "sctp_pool":
      - Monitored by "sctp";
      - Members: 192.0.9.10:2905 and 192.0.9.11:2905.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-09",
    "label": "Configuring SCTP services and referencing SCTP profiles in a declaration",
    "remark": "SCTP service with SCTP profile",
    "Sample_nonhttp_09": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "sctp_service": {
          "class": "Service_SCTP",
          "virtualAddresses": [
            "10.0.9.10"
          ],
          "virtualPort": 2905,
          "profileSCTP": {
            "use": "custom_sctp"
          },
          "pool": "sctp_pool"
        },
        "custom_sctp": {
          "class": "SCTP_Profile",
          "parentProfile": {
            "bigip": "/Common/sctp"
          },
          "inboundStreams": 10,
          "outboundStreams": 10
        },
        "sctp_pool": {
          "class": "Pool",
          "monitors": [
            "sctp"
          ],
          "members": [
            {
              "servicePort": 2905,
              "serverAddresses": [
                "192.0.9.10",
                "192.0.9.11"
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


