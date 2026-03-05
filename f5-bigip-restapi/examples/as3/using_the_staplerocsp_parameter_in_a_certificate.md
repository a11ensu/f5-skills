# Using the staplerOCSP parameter in a certificate

## Description

This declaration configures OCSP stapling for a TLS_Server profile. The certificate object has `staplerOCSP` enabled, allowing BIG-IP to staple OCSP responses during the TLS handshake.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_11";
  - Application "A1";
    - HTTPS service "service" on 10.0.11.10:443;
      - Uses TLS_Server "stapleTLS";
      - Pool "web_pool" with HTTP members;
    - Certificate object "stapledCert":
      - Certificate from URI;
      - `staplerOCSP` set to `"enabled"`;
    - TLS_Server "stapleTLS":
      - Uses `"stapledCert"` via `certificates[0].certificate.use`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-11",
    "label": "Sample 11",
    "remark": "Using the staplerOCSP parameter in a certificate",
    "Sample_tls_11": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.11.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "stapleTLS"
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
                "192.0.11.10",
                "192.0.11.11"
              ]
            }
          ]
        },
        "stapledCert": {
          "class": "Certificate",
          "certificate": {
            "url": "https://example.com/certs/stapled.crt"
          },
          "staplerOCSP": "enabled"
        },
        "stapleTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "use": "stapledCert"
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


