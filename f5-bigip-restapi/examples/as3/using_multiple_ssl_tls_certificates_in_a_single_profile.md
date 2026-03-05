# Using multiple SSL/TLS certificates in a single profile

## Description

This declaration configures a single TLS_Server profile with multiple certificates to support SNI-based selection. The HTTPS virtual service can serve different certificates depending on the requested hostname.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_02";
  - Application "A1";
    - HTTPS virtual server "service" on 10.0.2.10:443;
      - Uses TLS_Server profile "multiCertTLS";
      - Pool "web_pool" with two HTTP members 192.0.2.10:80 and 192.0.2.11:80;
    - TLS_Server "multiCertTLS":
      - Contains two certificate entries:
        - First references `/Common/site1.crt` and `/Common/site1.key`;
        - Second references `/Common/site2.crt` and `/Common/site2.key`;
      - BIG-IP selects certificate based on SNI / client hello.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-02",
    "label": "Sample 2",
    "remark": "Using multiple SSL/TLS certificates in a single profile",
    "Sample_tls_02": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.2.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "multiCertTLS"
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
                "192.0.2.10",
                "192.0.2.11"
              ]
            }
          ]
        },
        "multiCertTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/site1.crt"
              },
              "privateKey": {
                "bigip": "/Common/site1.key"
              }
            },
            {
              "certificate": {
                "bigip": "/Common/site2.crt"
              },
              "privateKey": {
                "bigip": "/Common/site2.key"
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


