# Configuring the renegotiation property on TLS classes

## Description

This declaration configures SSL renegotiation behavior on TLS_Server and/or TLS_Client profiles, including whether renegotiation is allowed and if secure renegotiation is enforced.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_20";
  - Application "A1";
    - HTTPS service "service" on 10.0.20.10:443;
      - Uses TLS_Server "renegTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "renegTLS":
      - `renegotiation` = "secure";
      - `renegotiateMaxRecordDelay` set to limit renegotiation frequency;
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-20",
    "label": "Sample 20",
    "remark": "Configuring the renegotiation property on TLS classes",
    "Sample_tls_20": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.20.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "renegTLS"
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
                "192.0.20.10",
                "192.0.20.11"
              ]
            }
          ]
        },
        "renegTLS": {
          "class": "TLS_Server",
          "renegotiation": "secure",
          "renegotiateMaxRecordDelay": 10,
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


