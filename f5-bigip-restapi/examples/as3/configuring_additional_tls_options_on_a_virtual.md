# Configuring additional TLS options on a virtual

## Description

This declaration configures advanced TLS options directly on the Service_HTTPS object, such as `insertEmptyFragments`, `allowNonSSL`, and `honorCipherOrder`, while still using a TLS_Server profile for certificates.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_15";
  - Application "A1";
    - HTTPS service "service" on 10.0.15.10:443;
      - `serverTLS` "webtls";
      - Additional TLS options on the service:
        - `insertEmptyFragments`, `allowNonSSL`, `honorCipherOrder`, etc.;
      - Pool "web_pool" with HTTP members;
    - TLS_Server "webtls" with default cert/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-15",
    "label": "Sample 15",
    "remark": "Configuring additional TLS options on a virtual",
    "Sample_tls_15": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.15.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "webtls",
          "insertEmptyFragments": "enabled",
          "allowNonSSL": "disabled",
          "honorCipherOrder": "enabled"
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
                "192.0.15.10",
                "192.0.15.11"
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
        }
      }
    }
  }
}
```

## Tested json templates


