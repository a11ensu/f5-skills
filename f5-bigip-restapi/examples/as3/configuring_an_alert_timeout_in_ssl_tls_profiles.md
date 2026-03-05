# Configuring an alert timeout in SSL (TLS) profiles

## Description

This declaration configures the SSL alert timeout on a TLS_Server profile, controlling how long the BIG-IP waits for SSL close/alert messages before timing out.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_18";
  - Application "A1";
    - HTTPS service "service" on 10.0.18.10:443;
      - Uses TLS_Server "alertTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "alertTLS":
      - `alertTimeout` set (for example, 10 seconds);
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-18",
    "label": "Sample 18",
    "remark": "Configuring an alert timeout in SSL (TLS) profiles",
    "Sample_tls_18": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.18.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "alertTLS"
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
                "192.0.18.10",
                "192.0.18.11"
              ]
            }
          ]
        },
        "alertTLS": {
          "class": "TLS_Server",
          "alertTimeout": 10,
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


