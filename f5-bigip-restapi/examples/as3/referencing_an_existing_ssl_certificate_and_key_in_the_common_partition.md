# Referencing an existing SSL certificate and key in the Common partition

## Description

This declaration shows how to use an existing certificate and key from the Common partition inside an AS3-managed TLS_Server profile. The HTTPS virtual server terminates client-side TLS using the default BIG-IP certificate objects.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_tls_01";
  - Application named "A1";
    - HTTPS virtual server "service" listening on 10.0.1.10:443;
      - Uses server-side TLS profile "webtls";
      - Pool "web_pool" with two HTTP members 192.0.1.10:80 and 192.0.1.11:80, monitored by "http";
    - TLS_Server profile "webtls":
      - Uses existing certificate and key from /Common partition:
        - certificate: `/Common/default.crt`;
        - private key: `/Common/default.key`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-01",
    "label": "Sample 1",
    "remark": "Referencing an existing SSL certificate and key in the Common partition",
    "Sample_tls_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.1.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "webtls"
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
                "192.0.1.10",
                "192.0.1.11"
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


