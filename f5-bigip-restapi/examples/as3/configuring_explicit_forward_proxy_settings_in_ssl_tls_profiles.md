# Configuring explicit forward proxy settings in SSL (TLS) profiles

## Description

This declaration configures explicit SSL forward proxy settings on a TLS_Client profile. It enables outbound interception and re-encryption of client SSL traffic for explicit proxy use cases.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_16";
  - Application "A1";
    - HTTPS explicit proxy service "proxy_service" on 10.0.16.10:3128;
      - `serverTLS` "proxyServerTLS" for client-side interception;
      - `clientTLS` "proxyClientTLS" for outbound connections;
      - Pool "upstream_pool" with upstream proxy or servers;
    - TLS_Server "proxyServerTLS" with interception certificate;
    - TLS_Client "proxyClientTLS":
      - `forwardProxy` enabled;
      - `forwardProxyBypassDefaultAction` etc. set as needed.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-16",
    "label": "Sample 16",
    "remark": "Configuring explicit forward proxy settings in SSL (TLS) profiles",
    "Sample_tls_16": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "proxy_service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.16.10"
          ],
          "virtualPort": 3128,
          "pool": "upstream_pool",
          "serverTLS": "proxyServerTLS",
          "clientTLS": "proxyClientTLS"
        },
        "upstream_pool": {
          "class": "Pool",
          "monitors": [
            "https"
          ],
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.16.10"
              ]
            }
          ]
        },
        "proxyServerTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/proxy.crt"
              },
              "privateKey": {
                "bigip": "/Common/proxy.key"
              }
            }
          ]
        },
        "proxyClientTLS": {
          "class": "TLS_Client",
          "forwardProxy": "enabled",
          "forwardProxyBypassDefaultAction": "intercept",
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


