# Referencing an external IAM policy using a URL (UPDATED)

## Description

This AS3 declaration configures an HTTP virtual server that uses an APM Access profile with an external IAM policy referenced by URL. The IAM policy is not stored on BIG‑IP; instead, APM fetches it from the specified URL at runtime. AS3 only wires the Access profile to the virtual server and points to the external IAM policy location.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_02";
  - Application named "A1";
    - HTTP virtual server "service" on 10.0.7.10:80;
      - Uses Access profile "myIAMAccessProfile" which references an external IAM policy by URL;
      - The IAM policy URL is defined in the Access profile’s configuration;
      - A pool "web_pool" with HTTP health monitor and two pool members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "example-iam-url-1",
    "label": "Referencing an external IAM policy using a URL (UPDATED)",
    "remark": "Attach an Access profile that uses an external IAM policy referenced by URL",
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
          "profileAccess": {
            "class": "Access_Profile",
            "name": "myIAMAccessProfile",
            "iamPolicy": {
              "url": "https://example.com/apm/iam/policies/my-policy.json"
            }
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
                "192.0.7.10",
                "192.0.7.11"
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

