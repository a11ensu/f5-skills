# Sharing IP addresses between virtual servers

## Description

This example demonstrates multiple virtual servers sharing the same IP address but using different ports or protocols. It uses a shared `Service_Address` object referenced by multiple services.

## Examples

- Explanation of the example:
  - Tenant "Sample_shareip_01";
  - Application "A1";
    - `Service_Address` "vipAddress" with IP `10.0.18.10`;
    - Two services:
      - "http_service" on port 80 using "vipAddress";
      - "https_service" on port 443 using "vipAddress";
    - Separate pools for HTTP and HTTPS.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_shareip_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "vipAddress": {
          "class": "Service_Address",
          "virtualAddress": "10.0.18.10"
        },
        "http_service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            {
              "use": "vipAddress"
            }
          ],
          "virtualPort": 80,
          "pool": "pool_http"
        },
        "https_service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            {
              "use": "vipAddress"
            }
          ],
          "virtualPort": 443,
          "serverTLS": {
            "bigip": "/Common/clientssl"
          },
          "pool": "pool_https"
        },
        "pool_http": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.200"
              ]
            }
          ]
        },
        "pool_https": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.2.201"
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

---

