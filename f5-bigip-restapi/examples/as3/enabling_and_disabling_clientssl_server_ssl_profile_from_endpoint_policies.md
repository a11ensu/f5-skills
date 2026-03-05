# Enabling and disabling clientSSL (server SSL profile) from Endpoint policies

## Description

This declaration demonstrates dynamically enabling or disabling server-side TLS (clientSSL) on an HTTPS service via Endpoint Policies. The policy actions toggle SSL based on traffic classification.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_05";
  - Application "A1";
    - HTTPS virtual server "service" on 10.0.5.10:443;
      - Uses endpoint policy "sslTogglePolicy";
      - Default `serverTLS` is "webtls";
      - Pool "web_pool" with two HTTP members;
    - Endpoint_Policy "sslTogglePolicy":
      - Rule "disableSSL" disables SSL for specific traffic;
      - Rule "enableSSL" enables SSL using "webtls";
    - TLS_Server "webtls" with certificate from /Common/default.crt and /Common/default.key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-05",
    "label": "Sample 5",
    "remark": "Enabling and disabling clientSSL (server SSL profile) from Endpoint policies",
    "Sample_tls_05": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.5.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "webtls",
          "policyEndpoint": [
            {
              "use": "sslTogglePolicy"
            }
          ]
        },
        "sslTogglePolicy": {
          "class": "Endpoint_Policy",
          "rules": [
            {
              "name": "disableSSL",
              "conditions": [
                {
                  "type": "httpUri",
                  "pathStartsWith": [
                    "/plaintext"
                  ]
                }
              ],
              "actions": [
                {
                  "type": "ssl",
                  "event": "client",
                  "enable": false
                }
              ]
            },
            {
              "name": "enableSSL",
              "conditions": [
                {
                  "type": "httpUri",
                  "pathStartsWith": [
                    "/secure"
                  ]
                }
              ],
              "actions": [
                {
                  "type": "ssl",
                  "event": "client",
                  "enable": true,
                  "serverTLS": {
                    "use": "webtls"
                  }
                }
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
                "192.0.5.10",
                "192.0.5.11"
              ]
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates


