# Using multiple APM profiles in a declaration

## Description

This AS3 declaration shows how to use multiple APM profiles in a single Application. One HTTP virtual server uses an APM Access profile and a Per‑Request Access profile, while a second virtual server in the same Application uses a different Access profile. This demonstrates referencing multiple APM profiles and sharing them across services in one AS3 declaration.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_06";
  - Application named "A1";
    - Access profile "MainAccessProfile" defined inline;
    - Per‑Request profile "PerRequestProfile" defined inline;
    - Second Access profile "AdminAccessProfile" defined inline;
    - HTTP virtual server "service_main" on 10.0.11.10:80:
      - Uses "MainAccessProfile" and "PerRequestProfile";
      - Uses pool "web_pool";
    - HTTP virtual server "service_admin" on 10.0.11.20:80:
      - Uses "AdminAccessProfile";
      - Uses pool "admin_pool";
    - Two pools: "web_pool" and "admin_pool" each with HTTP monitor and two pool members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.23.0",
    "id": "example-multiple-apm-1",
    "label": "Using multiple APM profiles in a declaration",
    "remark": "Demonstrates multiple APM profiles and their usage across services",
    "Sample_http_06": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "MainAccessProfile": {
          "class": "Access_Profile",
          "profileType": "standard",
          "language": "en"
        },
        "PerRequestProfile": {
          "class": "Access_Profile",
          "profileType": "per-request",
          "perRequestPolicy": {
            "url": "https://example.com/apm/per-request/policies/main-per-request.json"
          }
        },
        "AdminAccessProfile": {
          "class": "Access_Profile",
          "profileType": "standard",
          "language": "en"
        },
        "service_main": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.11.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileAccess": {
            "use": "MainAccessProfile"
          },
          "profileAccessPerRequest": {
            "use": "PerRequestProfile"
          }
        },
        "service_admin": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.11.20"
          ],
          "virtualPort": 80,
          "pool": "admin_pool",
          "profileAccess": {
            "use": "AdminAccessProfile"
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
                "192.0.11.10",
                "192.0.11.11"
              ]
            }
          ]
        },
        "admin_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.11.20",
                "192.0.11.21"
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

</Output>
