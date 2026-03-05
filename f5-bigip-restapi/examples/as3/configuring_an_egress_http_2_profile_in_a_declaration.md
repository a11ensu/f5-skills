# Configuring an egress HTTP/2 profile in a declaration

## Description

Configures an egress (server-side) HTTP/2 profile to communicate with backend servers using HTTP/2, while clients may use HTTP/1.1 or HTTP/2.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http2_egress";
  - Application named "http2EgressApp";
    - HTTPS virtual server "service" on 10.0.24.10:443;
      - Pool "web_pool";
      - Egress HTTP/2 profile "egress_http2_profile";
      - Attached via `profileHTTP2` (or `profileHTTP2Server` depending on schema).

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http2-egress-01",
    "label": "Configuring an egress HTTP/2 profile",
    "remark": "Configuring an egress HTTP/2 profile in a declaration",
    "Sample_http2_egress": {
      "class": "Tenant",
      "http2EgressApp": {
        "class": "Application",
        "template": "https",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.24.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": {
            "bigip": "/Common/clientssl"
          },
          "profileHTTP2": {
            "use": "egress_http2_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.24.10"
              ]
            }
          ]
        },
        "egress_http2_profile": {
          "class": "HTTP2_Profile",
          "type": "server",
          "concurrentStreamsPerConnection": 100
        }
      }
    }
  }
}
```

## Tested json templates

---

