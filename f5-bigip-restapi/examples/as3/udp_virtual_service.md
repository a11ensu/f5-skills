# UDP virtual service

## Description

This declaration creates a simple UDP virtual service front-ending a pool of UDP servers. It demonstrates using `Service_UDP` with a basic UDP profile, a health monitor, and two backend pool members.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_nonhttp_01";
  - Application named "A1";
    - A UDP virtual service "udp_service" listening on 10.0.1.10:514;
      - Uses UDP profile `/Common/udp`;
      - Uses pool "udp_pool";
    - Pool "udp_pool":
      - Monitored by built-in "gateway_icmp" monitor;
      - Includes two members: 192.0.1.10:514 and 192.0.1.11:514.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-01",
    "label": "UDP virtual service",
    "remark": "Simple UDP virtual service example",
    "Sample_nonhttp_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "udp_service": {
          "class": "Service_UDP",
          "virtualAddresses": [
            "10.0.1.10"
          ],
          "virtualPort": 514,
          "profileUDP": {
            "bigip": "/Common/udp"
          },
          "pool": "udp_pool"
        },
        "udp_pool": {
          "class": "Pool",
          "monitors": [
            "gateway_icmp"
          ],
          "members": [
            {
              "servicePort": 514,
              "serverAddresses": [
                "192.0.1.10",
                "192.0.1.11"
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


