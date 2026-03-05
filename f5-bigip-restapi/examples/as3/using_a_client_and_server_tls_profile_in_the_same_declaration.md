# Using a client and server TLS profile in the same declaration

## Description

This declaration configures both client-side (inbound) and server-side (outbound) TLS profiles. The BIG-IP terminates client TLS and re-encrypts traffic to the backend servers using separate TLS_Server and TLS_Client objects.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_07";
  - Application "A1";
    - HTTPS virtual "service" on 10.0.7.10:443;
      - `serverTLS` = "clientFacingTLS";
      - `clientTLS` = "serverFacingTLS";
      - Pool "web_pool" with HTTPS members on port 443;
    - TLS_Server "clientFacingTLS" for client-side termination:
      - Uses /Common/default.crt and /Common/default.key;
    - TLS_Client "serverFacingTLS" for server-side re-encryption:
      - Uses `/Common/ca-bundle.crt` as trust CA;
      - Validates server certificates.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-07",
    "label": "Sample 7",
    "remark": "Using a client and server TLS profile in the same declaration",
    "Sample_tls_07": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.7.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "clientFacingTLS",
          "clientTLS": "serverFacingTLS"
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
                "192.0.7.10",
                "192.0.7.11"
              ]
            }
          ]
        },
        "clientFacingTLS": {
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
        "serverFacingTLS": {
          "class": "TLS_Client",
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


