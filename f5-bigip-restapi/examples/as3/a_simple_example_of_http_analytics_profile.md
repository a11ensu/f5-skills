# A: Simple example of HTTP Analytics profile

## Description

Provides a minimal HTTP Analytics profile configuration where all settings use BIG‑IP defaults. The example shows only the required AS3 structure to enable HTTP Analytics on a virtual server using a simple `Analytics_HTTP_Profile` object.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_analytics_simple";
  - Application named "analyticsApp";
    - A HTTP virtual server named "service" listening on 10.0.1.20:80;
      - A pool "web_pool" with two HTTP members and default "http" monitor;
      - An HTTP Analytics profile "simple_http_analytics" with no additional options;
      - The HTTP Analytics profile is attached via `analyticsProfiles`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-analytics-simple",
    "label": "HTTP Analytics simple",
    "remark": "A simple example of HTTP Analytics profile",
    "Sample_http_analytics_simple": {
      "class": "Tenant",
      "analyticsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.1.20"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "analyticsProfiles": [
            {
              "use": "simple_http_analytics"
            }
          ]
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
                "192.0.1.20",
                "192.0.1.21"
              ]
            }
          ]
        },
        "simple_http_analytics": {
          "class": "Analytics_HTTP_Profile"
        }
      }
    }
  }
}
```

## Tested json templates

---

