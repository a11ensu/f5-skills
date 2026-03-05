# HTTP with no compression, BIG-IP TCP profile, iRule for pool

## Description

This declaration deploys an HTTP application that disables HTTP compression, uses an existing BIG-IP TCP profile, and attaches an iRule to the pool. It demonstrates referencing BIG-IP-local objects from AS3 and applying an iRule at the pool level.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_02";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server named "service" which listens on address "10.0.7.10", port "80";
      - Uses the built-in BIG-IP TCP profile "/Common/tcp" via the `profileTCP` property;
      - Uses a custom HTTP profile named "http_profile" with compression explicitly disabled;
      - A pool named "web_pool" monitored by the default "http" monitor;
        - The pool includes two pool members "192.0.7.10:80" and "192.0.7.11:80";
        - The pool has an iRule attached by reference to an existing BIG-IP iRule "/Common/pool_select_irule".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "mnopqr12345",
    "label": "Sample 2",
    "remark": "HTTP with no compression, BIG-IP TCP profile, iRule for pool",
    "Sample_http_02": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.7.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileTCP": {
            "bigip": "/Common/tcp"
          },
          "profileHTTP": {
            "use": "http_profile"
          }
        },
        "http_profile": {
          "class": "HTTP_Profile",
          "insertXforwardedFor": true,
          "responseCompression": "none"
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
                "192.0.7.10",
                "192.0.7.11"
              ]
            }
          ],
          "iRules": [
            {
              "bigip": "/Common/pool_select_irule"
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates


