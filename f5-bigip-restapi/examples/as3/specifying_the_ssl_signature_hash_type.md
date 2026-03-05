# Specifying the SSL signature hash type

## Description

This declaration sets the preferred SSL signature hash algorithms on a TLS_Server profile, influencing which hash types (such as SHA256) are used when signing handshake messages.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_29";
  - Application "A1";
    - HTTPS service "service" on 10.0.29.10:443;
      - Uses TLS_Server "hashTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "hashTLS":
      - `signatureAlgorithms` or equivalent property set to include specific hash types (e.g. "RSA+SHA256");
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-29",
    "label": "Sample 29",
    "remark": "Specifying the SSL signature hash type",
    "Sample_tls_29": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.29.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "hashTLS"
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
                "192.0.29.10",
                "192.0.29.11"
              ]
            }
          ]
        },
        "hashTLS": {
          "class": "TLS_Server",
          "signatureAlgorithms": [
            "RSA+SHA256",
            "RSA+SHA384"
          ],
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
