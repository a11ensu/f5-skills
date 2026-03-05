# HTTP and HTTPS virtual services in one declaration

## Description

This declaration provisions both HTTP and HTTPS virtual servers within a single application. The HTTPS service uses a client SSL profile and references the same backend pool as the HTTP service, enabling clear HTTP/HTTPS coexistence on the same BIG-IP.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_04";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server "http_service" on address "10.0.9.10", port "80";
    - An HTTPS virtual server "https_service" on address "10.0.9.10", port "443";
      - The HTTPS service uses a client SSL profile named "clientssl" that references the BIG-IP default "/Common/clientssl";
      - Both services use the same pool "web_pool";
      - The pool "web_pool" is monitored by "http";
        - It has two members: "192.0.9.10:80" and "192.0.9.11:80".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "yzabcd1234",
    "label": "Sample 4",
    "remark": "HTTP and HTTPS virtual services in one declaration",
    "Sample_http_04": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "http_service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.9.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "https_service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.9.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "clientssl"
        },
        "clientssl": {
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
                "192.0.9.10",
                "192.0.9.11"
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


