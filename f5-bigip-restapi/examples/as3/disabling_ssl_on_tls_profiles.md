# Disabling SSL on TLS profiles

## Description

This declaration shows how to disable SSL/TLS processing on a TLS profile while still attaching the profile to a service, effectively passing traffic in clear text.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_26";
  - Application "A1";
    - Service_HTTPS "service" on 10.0.26.10:443;
      - Uses TLS_Server "disabledTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "disabledTLS":
      - `sslEnabled` = false (or equivalent property);
      - Certificates defined but not used for encryption when disabled.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-26",
    "label": "Sample 26",
    "remark": "Disabling SSL on TLS profiles",
    "Sample_tls_26": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.26.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "disabledTLS"
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
                "192.0.26.10",
                "192.0.26.11"
              ]
            }
          ]
        },
        "disabledTLS": {
          "class": "TLS_Server",
          "sslEnabled": false,
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


