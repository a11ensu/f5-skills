# Using a Rewrite profile in a declaration

## Description

Shows how to configure and apply a Rewrite profile to modify URLs or headers in HTTP traffic. The profile is attached to an HTTP service and can perform URI translation or header rewriting.

## Examples

- Explanation of the example:
  - Tenant named "Sample_rewrite";
  - Application named "rewriteApp";
    - HTTP virtual server "service" on 10.0.7.10:80;
      - Pool "web_pool";
      - Rewrite profile "rewrite_profile" of class "Rewrite_Profile";
      - Attached via `profileRewrite`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "rewrite-01",
    "label": "Using a Rewrite profile",
    "remark": "Using a Rewrite profile in a declaration",
    "Sample_rewrite": {
      "class": "Tenant",
      "rewriteApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.7.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileRewrite": {
            "use": "rewrite_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.7.10"
              ]
            }
          ]
        },
        "rewrite_profile": {
          "class": "Rewrite_Profile",
          "uriRules": [
            {
              "name": "rewriteToApp",
              "client": {
                "pattern": "/app",
                "string": "/app1"
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

