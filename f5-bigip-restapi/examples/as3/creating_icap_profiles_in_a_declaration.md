# Creating ICAP profiles in a declaration

## Description

Demonstrates how to create ICAP-based Request and Response Adapt profiles directly in AS3 and attach them to an HTTP service.

## Examples

- Explanation of the example:
  - Tenant named "Sample_icap_create";
  - Application named "icapApp";
    - HTTP virtual server "service" on 10.0.20.20:80;
      - Pool "web_pool";
      - New ICAP-based Request and Response Adapt profiles "req_icap_profile" and "resp_icap_profile";
      - Attached via `profileRequestAdapt` and `profileResponseAdapt`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "icap-create-01",
    "label": "Creating ICAP profiles",
    "remark": "Creating ICAP profiles in a declaration",
    "Sample_icap_create": {
      "class": "Tenant",
      "icapApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.20.20"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileRequestAdapt": {
            "use": "req_icap_profile"
          },
          "profileResponseAdapt": {
            "use": "resp_icap_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.20.20"
              ]
            }
          ]
        },
        "req_icap_profile": {
          "class": "Request_Adapt_Profile",
          "servers": [
            {
              "name": "icap_server",
              "service": {
                "bigip": "/Common/icap-service"
              }
            }
          ]
        },
        "resp_icap_profile": {
          "class": "Response_Adapt_Profile",
          "servers": [
            {
              "name": "icap_server",
              "service": {
                "bigip": "/Common/icap-service"
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

---

