# TCP load-balanced to ICAP with custom monitor

## Description

This declaration deploys a TCP virtual service that load-balances traffic to ICAP servers. It uses `Service_TCP`, a custom TCP monitor for ICAP, and a dedicated pool of ICAP services.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_02";
  - Application "A1";
    - TCP virtual service "icap_service" on 10.0.2.10:1344 (ICAP);
      - Uses TCP profile `/Common/tcp`;
      - Uses pool "icap_pool";
    - Custom monitor "icap_tcp_monitor":
      - `class` = "Monitor";
      - Type "tcp";
      - Configured for ICAP port 1344;
    - Pool "icap_pool":
      - Uses monitor "icap_tcp_monitor";
      - Members: 192.0.2.10:1344 and 192.0.2.11:1344.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-02",
    "label": "TCP load-balanced to ICAP with custom monitor",
    "remark": "TCP to ICAP with a custom TCP monitor",
    "Sample_nonhttp_02": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "icap_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.2.10"
          ],
          "virtualPort": 1344,
          "profileTCP": {
            "bigip": "/Common/tcp"
          },
          "pool": "icap_pool"
        },
        "icap_tcp_monitor": {
          "class": "Monitor",
          "monitorType": "tcp",
          "interval": 5,
          "timeout": 16,
          "destination": "0.0.0.0:1344"
        },
        "icap_pool": {
          "class": "Pool",
          "monitors": [
            "icap_tcp_monitor"
          ],
          "members": [
            {
              "servicePort": 1344,
              "serverAddresses": [
                "192.0.2.10",
                "192.0.2.11"
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


