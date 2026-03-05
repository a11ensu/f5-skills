# Referencing an external Per Request Access policy using a URL

## Description

This AS3 declaration attaches an APM Per‑Request Access policy to an HTTP virtual server by referencing the policy via URL. The per‑request policy is not stored locally on BIG‑IP; it is retrieved from the specified external location. AS3 configures the Service_HTTP with an Access profile that contains the external per‑request policy reference.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_04";
  - Application named "A1";
    - Access profile "PerRequestProfile" defined inline;
      - Contains a `perRequestPolicy` property referencing a URL;
    - HTTP virtual server "service" on 10.0.9.10:80;
      - Uses the "PerRequestProfile" via `"use": "PerRequestProfile"`;
      - A pool "web_pool" with HTTP monitor and two pool members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.23.0",
    "id": "example-per-request-url-1",
    "label": "Referencing an external Per Request Access policy using a URL",
    "remark": "Attach a Per-Request Access policy referenced by external URL",
    "Sample_http_04": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "PerRequestProfile": {
          "class": "Access_Profile",
          "profileType": "per-request",
          "perRequestPolicy": {
            "url": "https://example.com/apm/per-request/policies/my-per-request-policy.json"
          }
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.9.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileAccess": {
            "use": "PerRequestProfile"
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

---

