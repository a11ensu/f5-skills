# Referencing existing Access and Connectivity profiles

## Description

This AS3 declaration attaches existing APM Access and Connectivity profiles (already created on the BIG‑IP) to an HTTP virtual server. AS3 is used only to deploy the LTM objects (virtual server and pool) and reference the pre‑provisioned APM profiles by name, without managing or modifying the APM configuration itself.

## Examples

- Explanation of the example:
  - Tenant (partition) named "Sample_http_01";
  - Application (folder) named "A1";
    - An HTTP virtual server named "service" listening on 10.0.6.10:80;
      - The virtual server references an existing Access Profile "myAccessProfile";
      - The virtual server references an existing Connectivity Profile "myConnectivityProfile";
      - A pool named "web_pool" with default "http" monitor;
        - Pool members 192.0.6.10:80 and 192.0.6.11:80.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "example-access-connectivity-1",
    "label": "Referencing existing Access and Connectivity profiles",
    "remark": "Attach existing APM Access and Connectivity profiles to a virtual server",
    "Sample_http_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileAccess": {
            "bigip": "/Common/myAccessProfile"
          },
          "profileConnectivity": {
            "bigip": "/Common/myConnectivityProfile"
          }
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

---

