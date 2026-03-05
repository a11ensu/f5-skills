# Referencing multiple SSL profiles on a single virtual service

## Description

This declaration assigns multiple TLS_Server profiles to a single HTTPS virtual service. BIG-IP chooses the most appropriate profile based on SNI or other matching criteria.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_14";
  - Application "A1";
    - HTTPS service "service" on 10.0.14.10:443;
      - `serverTLS` is an array: ["defaultTLS", "vipSpecificTLS"];
      - Pool "web_pool" with HTTP members;
    - TLS_Server "defaultTLS" with default certificate;
    - TLS_Server "vipSpecificTLS" with an alternate certificate for specific hostnames/SNI.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-14",
    "label": "Sample 14",
    "remark": "Referencing multiple SSL profiles on a single virtual service",
    "Sample_tls_14": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.14.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": [
            {
              "use": "defaultTLS"
            },
            {
              "use": "vipSpecificTLS"
            }
          ]
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
                "192.0.14.10",
                "192.0.14.11"
              ]
            }
          ]
        },
        "defaultTLS": {
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
        "vipSpecificTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/vip.crt"
              },
              "privateKey": {
                "bigip": "/Common/vip.key"
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


