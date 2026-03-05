# Disabling the mode for TLS Server certificates

## Description

This declaration explicitly disables the `mode` (client authentication) for a TLS_Server profile, preventing the BIG-IP from requesting client certificates during the TLS handshake.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_24";
  - Application "A1";
    - HTTPS service "service" on 10.0.24.10:443;
      - Uses TLS_Server "noClientAuthTLS";
      - Pool "web_pool" with HTTP members;
    - TLS_Server "noClientAuthTLS":
      - `mode` = "disabled" (no client certificate authentication);
      - Uses default certificate/key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-24",
    "label": "Sample 24",
    "remark": "Disabling the mode for TLS Server certificates",
    "Sample_tls_24": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.24.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "noClientAuthTLS"
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
                "192.0.24.10",
                "192.0.24.11"
              ]
            }
          ]
        },
        "noClientAuthTLS": {
          "class": "TLS_Server",
          "mode": "disabled",
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


