# HTTP and HTTPS virtual services in one declaration

## Description

This declaration creates both HTTP and HTTPS virtual services for the same application. The HTTPS service terminates TLS using a TLS_Server profile, while both services share the same backend pool.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_06";
  - Application "A1";
    - HTTP virtual "http_service" on 10.0.6.10:80;
    - HTTPS virtual "https_service" on 10.0.6.10:443;
      - Uses TLS_Server "webtls";
      - Both use pool "web_pool";
    - TLS_Server "webtls" with certificate/key from /Common/default.crt and /Common/default.key;
    - Pool "web_pool" with two HTTP members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-06",
    "label": "Sample 6",
    "remark": "HTTP and HTTPS virtual services in one declaration",
    "Sample_tls_06": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "http_service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "https_service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "webtls"
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
                "192.0.6.10",
                "192.0.6.11"
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


