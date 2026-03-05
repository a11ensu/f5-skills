# Using an existing TFTP profile in a declaration

## Description

This declaration uses an existing BIG-IP TFTP profile for a UDP-based TFTP service. It shows how to attach the `/Common/tftp` profile to a Service_UDP object.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_07";
  - Application "A1";
    - UDP service "tftp_service" on 10.0.7.10:69;
      - Uses `profileTFTP` with `/Common/tftp`;
      - Pool "tftp_pool" with TFTP servers;
    - Pool "tftp_pool":
      - Monitored by "udp";
      - Members: 192.0.7.10:69 and 192.0.7.11:69.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-07",
    "label": "Using an existing TFTP profile in a declaration",
    "remark": "TFTP service using existing TFTP profile",
    "Sample_nonhttp_07": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "tftp_service": {
          "class": "Service_UDP",
          "virtualAddresses": [
            "10.0.7.10"
          ],
          "virtualPort": 69,
          "profileTFTP": {
            "bigip": "/Common/tftp"
          },
          "pool": "tftp_pool"
        },
        "tftp_pool": {
          "class": "Pool",
          "monitors": [
            "udp"
          ],
          "members": [
            {
              "servicePort": 69,
              "serverAddresses": [
                "192.0.7.10",
                "192.0.7.11"
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


