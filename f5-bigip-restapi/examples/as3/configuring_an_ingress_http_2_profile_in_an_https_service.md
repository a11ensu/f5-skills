# Configuring an ingress HTTP/2 profile in an HTTPS service

## Description

Shows how to configure an ingress (client-side) HTTP/2 profile on an HTTPS service to support HTTP/2 from clients while optionally using HTTP/1.1 to servers.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http2_ingress";
  - Application named "http2IngressApp";
    - HTTPS virtual server "service" on 10.0.21.10:443;
      - Pool "web_pool";
      - Ingress HTTP/2 profile "ingress_http2_profile";
      - Attached via `profileHTTP2`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http2-ingress-01",
    "label": "Configuring an ingress HTTP/2 profile in an HTTPS service",
    "remark": "Configuring an ingress HTTP/2 profile in an HTTPS service",
    "Sample_http2_ingress": {
      "class": "Tenant",
      "http2IngressApp": {
        "class": "Application",
        "template": "https",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.21.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": {
            "bigip": "/Common/clientssl"
          },
          "profileHTTP2": {
            "use": "ingress_http2_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.21.10"
              ]
            }
          ]
        },
        "ingress_http2_profile": {
          "class": "HTTP2_Profile",
          "type": "client",
          "concurrentStreamsPerConnection": 100
        }
      }
    }
  }
}
```

## Tested json templates

---

