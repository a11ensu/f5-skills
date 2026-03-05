# Using the HTTP/2 profile in a declaration

## Description

Configures an HTTP/2 profile and attaches it to an HTTPS service so that the virtual server can handle HTTP/2 connections on the client side.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http2";
  - Application named "http2App";
    - HTTPS virtual server "service" on 10.0.14.10:443;
      - Pool "web_pool";
      - HTTP/2 profile "http2_profile" of class "HTTP2_Profile";
      - Attached via `profileHTTP2`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http2-01",
    "label": "Using the HTTP/2 profile",
    "remark": "Using the HTTP/2 profile in a declaration",
    "Sample_http2": {
      "class": "Tenant",
      "http2App": {
        "class": "Application",
        "template": "https",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.14.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": {
            "bigip": "/Common/clientssl"
          },
          "profileHTTP2": {
            "use": "http2_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.14.10"
              ]
            }
          ]
        },
        "http2_profile": {
          "class": "HTTP2_Profile",
          "concurrentStreamsPerConnection": 100
        }
      }
    }
  }
}
```

## Tested json templates

---

