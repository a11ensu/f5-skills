# Using OCSP Certificate Validation in a declaration

## Description

This declaration enables OCSP-based certificate validation for outbound TLS connections. The TLS_Client profile is configured to query an OCSP responder to verify server certificates.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_10";
  - Application "A1";
    - HTTPS service "service" on 10.0.10.10:443;
      - `serverTLS` "webtls" for client-side termination;
      - `clientTLS` "ocspTLS" for outbound TLS with OCSP validation;
      - Pool "web_pool" with HTTPS members;
    - TLS_Client "ocspTLS":
      - `ocsp` section:
        - Enabled;
        - Specifies OCSP responder URL and timeout;
      - Uses a CA bundle and validates certificates.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-10",
    "label": "Sample 10",
    "remark": "Using OCSP Certificate Validation in a declaration",
    "Sample_tls_10": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "webtls",
          "clientTLS": "ocspTLS"
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
                "192.0.10.10",
                "192.0.10.11"
              ]
            }
          ]
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
        },
        "ocspTLS": {
          "class": "TLS_Client",
          "trustCA": {
            "bigip": "/Common/ca-bundle.crt"
          },
          "validateCertificate": true,
          "ocsp": {
            "enabled": true,
            "url": "http://ocsp.example.com",
            "timeout": 5
          }
        }
      }
    }
  }
}
```

## Tested json templates


