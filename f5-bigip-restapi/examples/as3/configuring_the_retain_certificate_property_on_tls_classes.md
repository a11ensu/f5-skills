# Configuring the retain certificate property on TLS classes

## Description

This declaration enables the `retainCertificate` property on a TLS_Server profile so that the BIG-IP retains the full client certificate chain for inspection or logging after handshake completion.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_21";
  - Application "A1";
    - HTTPS service "service" on 10.0.21.10:443;
      - Uses TLS_Server "retainTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "retainTLS":
      - `retainCertificate` = true;
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-21",
    "label": "Sample 21",
    "remark": "Configuring the retain certificate property on TLS classes",
    "Sample_tls_21": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.21.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "retainTLS"
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
                "192.0.21.10",
                "192.0.21.11"
              ]
            }
          ]
        },
        "retainTLS": {
          "class": "TLS_Server",
          "retainCertificate": true,
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


