# Configuring a cache timeout in SSL (TLS) profiles

## Description

This declaration sets the SSL session cache timeout on a TLS_Server profile, controlling how long session parameters are cached for session resumption.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_17";
  - Application "A1";
    - HTTPS service "service" on 10.0.17.10:443;
      - Uses TLS_Server "cacheTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "cacheTLS":
      - `cacheTimeout` set (for example, 600 seconds);
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-17",
    "label": "Sample 17",
    "remark": "Configuring a cache timeout in SSL (TLS) profiles",
    "Sample_tls_17": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.17.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "cacheTLS"
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
                "192.0.17.10",
                "192.0.17.11"
              ]
            }
          ]
        },
        "cacheTLS": {
          "class": "TLS_Server",
          "cacheTimeout": 600,
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


