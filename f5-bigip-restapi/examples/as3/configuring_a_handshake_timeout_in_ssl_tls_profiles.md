# Configuring a handshake timeout in SSL (TLS) profiles

## Description

This declaration sets the SSL/TLS handshake timeout on a TLS_Server profile, defining the maximum time allowed to complete a TLS handshake.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_19";
  - Application "A1";
    - HTTPS service "service" on 10.0.19.10:443;
      - Uses TLS_Server "handshakeTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "handshakeTLS":
      - `handshakeTimeout` set (for example, 15 seconds);
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-19",
    "label": "Sample 19",
    "remark": "Configuring a handshake timeout in SSL (TLS) profiles",
    "Sample_tls_19": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.19.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "handshakeTLS"
        },
        "web_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.19.10",
                "192.0.19.11"
              ]
            }
          ]
        },
        "handshakeTLS": {
          "class": "TLS_Server",
          "handshakeTimeout": 15,
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
        }
      }
    }
  }
}
```

## Tested json templates


