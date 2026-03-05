# Using PKCS 12 in a declaration

## Description

This declaration uses a PKCS#12 bundle (PFX) in a certificate object, letting AS3 load certificate, key, and optional chain from an external URI. The TLS_Server profile then references this certificate by name.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_04";
  - Application "A1";
    - HTTPS virtual server "service" on 10.0.4.10:443 using TLS_Server "p12TLS";
      - Pool "web_pool" with two HTTP members 192.0.4.10:80 and 192.0.4.11:80;
    - Certificate object "myP12Cert":
      - `class` = "Certificate";
      - `certificate` points to a PKCS#12 file via `url`;
      - `passphrase` used to decrypt PKCS#12;
    - TLS_Server "p12TLS":
      - `certificates[0].certificate.use = "myP12Cert"`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-04",
    "label": "Sample 4",
    "remark": "Using PKCS 12 in a declaration",
    "Sample_tls_04": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.4.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "p12TLS"
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
                "192.0.4.10",
                "192.0.4.11"
              ]
            }
          ]
        },
        "myP12Cert": {
          "class": "Certificate",
          "certificate": {
            "url": "https://example.com/certs/app.p12"
          },
          "passphrase": {
            "ciphertext": "ZmFrZS1lbmNyeXB0ZWQtcGFzcw==",
            "protected": "SecureVault",
            "ignoreChanges": true
          }
        },
        "p12TLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "use": "myP12Cert"
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


