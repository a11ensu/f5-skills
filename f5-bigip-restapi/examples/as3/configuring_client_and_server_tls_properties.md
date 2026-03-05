# Configuring Client and Server TLS properties

## Description

This declaration configures basic properties on both TLS_Server and TLS_Client profiles, such as protocol versions and cipher strings, and attaches them to a single HTTPS service.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_27";
  - Application "A1";
    - HTTPS service "service" on 10.0.27.10:443;
      - `serverTLS` "basicServerTLS";
      - `clientTLS` "basicClientTLS";
      - Pool "web_pool" with HTTPS members;
    - TLS_Server "basicServerTLS":
      - `tls1_0Enabled`, `tls1_1Enabled`, `tls1_2Enabled` set;
      - `ciphers` string defined;
    - TLS_Client "basicClientTLS":
      - Similar protocol and cipher properties;
      - `trustCA` and `validateCertificate` configured.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-27",
    "label": "Sample 27",
    "remark": "Configuring Client and Server TLS properties",
    "Sample_tls_27": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.27.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "basicServerTLS",
          "clientTLS": "basicClientTLS"
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
                "192.0.27.10",
                "192.0.27.11"
              ]
            }
          ]
        },
        "basicServerTLS": {
          "class": "TLS_Server",
          "tls1_0Enabled": false,
          "tls1_1Enabled": false,
          "tls1_2Enabled": true,
          "ciphers": "DEFAULT",
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
        "basicClientTLS": {
          "class": "TLS_Client",
          "tls1_0Enabled": false,
          "tls1_1Enabled": false,
          "tls1_2Enabled": true,
          "ciphers": "DEFAULT",
          "trustCA": {
            "bigip": "/Common/ca-bundle.crt"
          },
          "validateCertificate": true
        }
      }
    }
  }
}
```

## Tested json templates


