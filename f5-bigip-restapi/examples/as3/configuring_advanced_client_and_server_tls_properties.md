# Configuring advanced Client and Server TLS properties

## Description

This declaration configures advanced TLS properties such as session tickets, maximum record size, and maximum renegotiations on both client and server TLS profiles.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_28";
  - Application "A1";
    - HTTPS service "service" on 10.0.28.10:443;
      - `serverTLS` "advancedServerTLS";
      - `clientTLS` "advancedClientTLS";
      - Pool "web_pool" with HTTPS members;
    - TLS_Server "advancedServerTLS":
      - Advanced properties (e.g. `sessionTicket`, `maxRecordSize`, `maxRenegotiations`);
    - TLS_Client "advancedClientTLS":
      - Similar advanced properties plus trust/validation settings.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-28",
    "label": "Sample 28",
    "remark": "Configuring advanced Client and Server TLS properties",
    "Sample_tls_28": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.28.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "advancedServerTLS",
          "clientTLS": "advancedClientTLS"
        },
        "web_pool": {
          "class": "Pool",
          "monitors": [
            "https"
          ],
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.28.10",
                "192.0.28.11"
              ]
            }
          ]
        },
        "advancedServerTLS": {
          "class": "TLS_Server",
          "sessionTicket": "enabled",
          "maxRecordSize": 16384,
          "maxRenegotiations": 5,
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/default.crt"
              },
              "privateKey": {
                "bigip": "/Common/default.key"
              }
            }
          ]
        },
        "advancedClientTLS": {
          "class": "TLS_Client",
          "sessionTicket": "enabled",
          "maxRecordSize": 16384,
          "maxRenegotiations": 5,
          "trustCA": {
            "bigip": "/Common/ca-bundle.crt"
          },
          "validateCertificate": true
        }
      }
    }
  }
}
```

## Tested json templates


