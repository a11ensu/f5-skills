# NEW in AS3 3.23 – Inline Access Profile with external IAM policy URL

## Description

This AS3 3.23+ declaration defines an APM Access profile inline within the AS3 Application and attaches it to an HTTP virtual server. The Access profile itself includes an external IAM policy reference via URL. This demonstrates the newer capability to manage certain APM objects directly in AS3 while still using an externally hosted IAM policy.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_03";
  - Application named "A1";
    - An inline Access profile object "InlineAccessProfile";
      - The profile specifies an external IAM policy URL;
    - HTTP virtual server "service" on 10.0.8.10:80;
      - Uses the inline Access profile via `"use": "InlineAccessProfile"`;
      - A pool "web_pool" with HTTP monitor and two pool members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.23.0",
    "id": "example-new-3-23-1",
    "label": "NEW in AS3 3.23 – Inline Access Profile with external IAM policy URL",
    "remark": "Demonstrates inline Access profile referencing an external IAM policy URL",
    "Sample_http_03": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "InlineAccessProfile": {
          "class": "Access_Profile",
          "profileType": "iam",
          "iamPolicy": {
            "url": "https://example.com/apm/iam/policies/inline-profile-policy.json"
          }
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileAccess": {
            "use": "InlineAccessProfile"
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
                "192.0.8.10",
                "192.0.8.11"
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

