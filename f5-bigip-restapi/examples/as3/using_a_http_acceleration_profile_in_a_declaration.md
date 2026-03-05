# Using a HTTP Acceleration profile in a declaration

## Description

Configures a HTTP Acceleration (caching/compression) profile and attaches it to an HTTP service. The profile optimizes web traffic performance by caching or compressing responses.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_accel";
  - Application named "accelApp";
    - HTTP virtual server "service" on 10.0.9.10:80;
      - Pool "web_pool";
      - HTTP Acceleration profile "http_accel_profile" of class "HTTP_Acceleration_Profile";
      - Attached via `profileHTTPAcceleration`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-accel-01",
    "label": "Using a HTTP Acceleration profile",
    "remark": "Using a HTTP Acceleration profile in a declaration",
    "Sample_http_accel": {
      "class": "Tenant",
      "accelApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.9.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileHTTPAcceleration": {
            "use": "http_accel_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.9.10",
                "192.0.9.11"
              ]
            }
          ]
        },
        "http_accel_profile": {
          "class": "HTTP_Acceleration_Profile",
          "cache": true,
          "cacheMaxAge": 3600
        }
      }
    }
  }
}
```

## Tested json templates

---

