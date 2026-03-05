# Setting BBR Congestion Control in a TCP profile with AS3

## Description

This declaration configures a custom TCP profile that uses BBR as its congestion-control algorithm, then applies it to a TCP service. It demonstrates how to enable modern congestion control via AS3.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_08";
  - Application "A1";
    - TCP service "bbr_service" on 10.0.8.10:8080;
      - Uses TCP_Profile "bbr_tcp";
      - Pool "bbr_pool" with two members;
    - TCP_Profile "bbr_tcp":
      - `parentProfile` `/Common/tcp`;
      - `congestionControl` set to "bbr";
    - Pool "bbr_pool":
      - Monitored by "tcp";
      - Members: 192.0.8.10:8080 and 192.0.8.11:8080.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-08",
    "label": "Setting BBR Congestion Control in a TCP profile with AS3",
    "remark": "Custom TCP profile using BBR",
    "Sample_nonhttp_08": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "bbr_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 8080,
          "profileTCP": {
            "use": "bbr_tcp"
          },
          "pool": "bbr_pool"
        },
        "bbr_tcp": {
          "class": "TCP_Profile",
          "parentProfile": {
            "bigip": "/Common/tcp"
          },
          "congestionControl": "bbr"
        },
        "bbr_pool": {
          "class": "Pool",
          "monitors": [
            "tcp"
          ],
          "members": [
            {
              "servicePort": 8080,
              "serverAddresses": [
                "192.0.8.10",
                "192.0.8.11"
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


