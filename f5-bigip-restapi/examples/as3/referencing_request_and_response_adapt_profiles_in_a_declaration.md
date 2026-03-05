# Referencing Request and Response Adapt profiles in a declaration

## Description

Shows how to reference existing Request Adapt and Response Adapt profiles in an AS3 declaration. These profiles integrate with external ICAP or other adaptation services.

## Examples

- Explanation of the example:
  - Tenant named "Sample_adapt_ref";
  - Application named "adaptApp";
    - HTTP virtual server "service" on 10.0.19.10:80;
      - Pool "web_pool";
      - Existing Request Adapt and Response Adapt profiles referenced via `profileRequestAdapt` and `profileResponseAdapt`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "adapt-ref-01",
    "label": "Referencing Request and Response Adapt profiles",
    "remark": "Referencing Request and Response Adapt profiles in a declaration",
    "Sample_adapt_ref": {
      "class": "Tenant",
      "adaptApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.19.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileRequestAdapt": {
            "bigip": "/Common/my_request_adapt"
          },
          "profileResponseAdapt": {
            "bigip": "/Common/my_response_adapt"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.19.10"
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

