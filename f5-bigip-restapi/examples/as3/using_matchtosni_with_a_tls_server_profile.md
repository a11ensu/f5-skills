# Using matchToSNI with a TLS_Server profile

## Description

This declaration enables `matchToSNI` on a TLS_Server profile so that the BIG-IP chooses the best matching certificate from a multi-certificate profile based on the SNI hostname in the client hello.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_03";
  - Application "A1";
    - HTTPS virtual server "service" on 10.0.3.10:443;
      - Uses TLS_Server profile "sniTLS";
      - Pool "web_pool" with two HTTP members 192.0.3.10:80 and 192.0.3.11:80;
    - TLS_Server "sniTLS":
      - `matchToSNI` set to `true`;
      - Two certificate entries:
        - `/Common/app1.crt` + `/Common/app1.key`;
        - `/Common/app2.crt` + `/Common/app2.key`;
      - SNI hostname determines which certificate is presented.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-03",
    "label": "Sample 3",
    "remark": "Using matchToSNI with a TLS_Server profile",
    "Sample_tls_03": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.3.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "sniTLS"
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
                "192.0.3.10",
                "192.0.3.11"
              ]
            }
          ]
        },
        "sniTLS": {
          "class": "TLS_Server",
          "matchToSNI": true,
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/app1.crt"
              },
              "privateKey": {
                "bigip": "/Common/app1.key"
              }
            },
            {
              "certificate": {
                "bigip": "/Common/app2.crt"
              },
              "privateKey": {
                "bigip": "/Common/app2.key"
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


