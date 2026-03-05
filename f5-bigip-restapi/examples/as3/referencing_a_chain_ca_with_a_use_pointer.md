# Referencing a Chain CA with a 'use' pointer

## Description

This declaration references a chain CA certificate object from a TLS_Client profile using a `use` pointer, allowing you to manage intermediate CA chains as separate AS3 objects.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_25";
  - Application "A1";
    - HTTPS service "service" on 10.0.25.10:443;
      - `serverTLS` "webtls";
      - `clientTLS` "chainedTLS";
      - Pool "web_pool" with HTTPS members;
    - Certificate object "chainCA" representing the intermediate CA chain;
    - TLS_Client "chainedTLS":
      - `trustCA` uses "chainCA" via `use`;
    - TLS_Server "webtls" with default cert/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-25",
    "label": "Sample 25",
    "remark": "Referencing a Chain CA with a 'use' pointer",
    "Sample_tls_25": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.25.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "webtls",
          "clientTLS": "chainedTLS"
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
                "192.0.25.10",
                "192.0.25.11"
              ]
            }
          ]
        },
        "chainCA": {
          "class": "Certificate",
          "certificate": {
            "url": "https://example.com/certs/chain-ca.crt"
          }
        },
        "chainedTLS": {
          "class": "TLS_Client",
          "trustCA": {
            "use": "chainCA"
          },
          "validateCertificate": true
        },
        "webtls": {
          "class": "TLS_Server",
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


