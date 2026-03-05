# Referencing existing ICAP profiles in a declaration

## Description

Shows how to reference existing ICAP profiles for request and response adaptation in AS3, typically used for antivirus or DLP scanning.

## Examples

- Explanation of the example:
  - Tenant named "Sample_icap_ref";
  - Application named "icapApp";
    - HTTP virtual server "service" on 10.0.20.10:80;
      - Pool "web_pool";
      - Existing ICAP profiles referenced via `profileRequestAdapt` and `profileResponseAdapt`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "icap-ref-01",
    "label": "Referencing existing ICAP profiles",
    "remark": "Referencing existing ICAP profiles in a declaration",
    "Sample_icap_ref": {
      "class": "Tenant",
      "icapApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.20.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileRequestAdapt": {
            "bigip": "/Common/my_icap_request"
          },
          "profileResponseAdapt": {
            "bigip": "/Common/my_icap_response"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.20.10"
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

