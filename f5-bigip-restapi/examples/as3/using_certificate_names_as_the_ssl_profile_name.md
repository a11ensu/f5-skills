# Using certificate names as the SSL profile name

## Description

This declaration uses the same name for the Certificate object and the TLS_Server profile, simplifying configuration when you want the SSL profile name to match the certificate name.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_23";
  - Application "A1";
    - HTTPS service "service" on 10.0.23.10:443;
      - `serverTLS` uses "mycert";
      - Pool "web_pool" with HTTP members;
    - Certificate object "mycert" with certificate/key from URI or inline;
    - TLS_Server "mycert" referencing the same Certificate object by `use`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-23",
    "label": "Sample 23",
    "remark": "Using certificate names as the SSL profile name",
    "Sample_tls_23": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.23.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "mycert"
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
                "192.0.23.10",
                "192.0.23.11"
              ]
            }
          ]
        },
        "mycert": {
          "class": "Certificate",
          "certificate": {
            "url": "https://example.com/certs/mycert.crt"
          },
          "privateKey": {
            "url": "https://example.com/certs/mycert.key"
          }
        },
        "mycertTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "use": "mycert"
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


