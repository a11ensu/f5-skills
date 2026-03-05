# Excluding host names from the SSL Forward Proxy Bypass

## Description

This declaration configures SSL forward proxy and explicitly excludes specific hostnames from the bypass list, ensuring those hosts are intercepted and inspected by the proxy.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_22";
  - Application "A1";
    - HTTPS explicit proxy "proxy_service" on 10.0.22.10:3128;
      - Uses TLS_Server "proxyServerTLS" and TLS_Client "proxyClientTLS";
      - Pool "upstream_pool" with upstream servers;
    - TLS_Client "proxyClientTLS":
      - `forwardProxy` enabled;
      - `forwardProxyBypassDefaultAction` = "bypass";
      - `forwardProxyBypassList` excludes specific hostnames (e.g. "sensitive.example.com") from bypass, forcing interception.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-22",
    "label": "Sample 22",
    "remark": "Excluding host names from the SSL Forward Proxy Bypass",
    "Sample_tls_22": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "proxy_service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.22.10"
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
                "192.0.22.10"
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
          "forwardProxyBypassDefaultAction": "bypass",
          "forwardProxyBypassList": [
            "sensitive.example.com"
          ],
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


