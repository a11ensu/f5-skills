# Using the userAgent Controls property

## Description

This declaration uses the `userAgent` controls property within an HTTP profile to enable or configure user-agent based features. It shows how to set `userAgent` options via AS3.

## Examples

- Explanation of the example:
  - Tenant "Sample_useragent_01";
  - Application "A1";
    - `HTTP_Profile` object "http_profile":
      - `userAgent` controls configured (for example, `enable: true`);
    - Service_HTTP "service":
      - Virtual `10.0.15.10:80`;
      - Uses "http_profile";
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_useragent_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "http_profile": {
          "class": "HTTP_Profile",
          "userAgent": {
            "enabled": true
          }
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.15.10"
          ],
          "virtualPort": 80,
          "profileHTTP": {
            "use": "http_profile"
          },
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.170"
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

