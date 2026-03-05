# Ignoring validation of certificates when retrieving URI data

## Description

This declaration configures a Certificate object to ignore certificate validation when fetching certificate/key data from a remote URI. It is useful in lab environments where remote endpoints use self-signed or untrusted certificates.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_12";
  - Application "A1";
    - HTTPS service "service" on 10.0.12.10:443;
      - Uses TLS_Server "uriTLS";
      - Pool "web_pool" with HTTP members;
    - Certificate object "remoteCert":
      - `certificate.url` points to remote HTTPS endpoint;
      - `ignoreCertificateWarnings` set to `true`;
    - TLS_Server "uriTLS":
      - Uses "remoteCert" for certificate.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-12",
    "label": "Sample 12",
    "remark": "Ignoring validation of certificates when retrieving URI data",
    "Sample_tls_12": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.12.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "uriTLS"
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
                "192.0.12.10",
                "192.0.12.11"
              ]
            }
          ]
        },
        "remoteCert": {
          "class": "Certificate",
          "certificate": {
            "url": "https://untrusted.example.com/certs/app.crt",
            "ignoreCertificateWarnings": true
          }
        },
        "uriTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "use": "remoteCert"
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


