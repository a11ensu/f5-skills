# Using tcpOptions in a TCP Profile

## Description

This declaration customizes TCP behavior using the `tcpOptions` property in a TCP_Profile object, then applies that profile to a TCP service. It demonstrates setting low-level TCP flags/options via AS3.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_04";
  - Application "A1";
    - Service_TCP "tcp_service" on 10.0.4.10:8080;
      - Uses custom TCP_Profile "custom_tcp";
      - Pool "tcp_pool" with two members;
    - TCP_Profile "custom_tcp":
      - Inherits from `/Common/tcp` via `parentProfile`;
      - `tcpOptions` array includes options like "mss", "wscale", "sack";
    - Pool "tcp_pool":
      - Monitored by "tcp";
      - Members: 192.0.4.10:8080 and 192.0.4.11:8080.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-04",
    "label": "Using tcpOptions in a TCP Profile",
    "remark": "Custom TCP profile with tcpOptions",
    "Sample_nonhttp_04": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "tcp_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.4.10"
          ],
          "virtualPort": 8080,
          "profileTCP": {
            "use": "custom_tcp"
          },
          "pool": "tcp_pool"
        },
        "custom_tcp": {
          "class": "TCP_Profile",
          "parentProfile": {
            "bigip": "/Common/tcp"
          },
          "tcpOptions": [
            "mss",
            "wscale",
            "sack"
          ]
        },
        "tcp_pool": {
          "class": "Pool",
          "monitors": [
            "tcp"
          ],
          "members": [
            {
              "servicePort": 8080,
              "serverAddresses": [
                "192.0.4.10",
                "192.0.4.11"
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


