# Creating Request and Response Adapt profiles in a declaration

## Description

Demonstrates how to create new Request Adapt and Response Adapt profiles directly in AS3 and apply them to an HTTP service.

## Examples

- Explanation of the example:
  - Tenant named "Sample_adapt_create";
  - Application named "adaptApp";
    - HTTP virtual server "service" on 10.0.19.20:80;
      - Pool "web_pool";
      - Request Adapt profile "req_adapt_profile" and Response Adapt profile "resp_adapt_profile";
      - Attached via `profileRequestAdapt` and `profileResponseAdapt`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "adapt-create-01",
    "label": "Creating Request and Response Adapt profiles",
    "remark": "Creating Request and Response Adapt profiles in a declaration",
    "Sample_adapt_create": {
      "class": "Tenant",
      "adaptApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.19.20"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileRequestAdapt": {
            "use": "req_adapt_profile"
          },
          "profileResponseAdapt": {
            "use": "resp_adapt_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.19.20"
              ]
            }
          ]
        },
        "req_adapt_profile": {
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
        "resp_adapt_profile": {
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

