# A: Simple example of HTTP Analytics profile with Capture filter

## Description

Provides a minimal HTTP Analytics profile that uses a simple capture filter to record only error responses. It shows the least configuration required to enable filtered capture within HTTP Analytics.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_analytics_capture_simple";
  - Application named "analyticsApp";
    - HTTP virtual server "service" on 10.0.2.20:80;
      - Pool "web_pool" with two HTTP members;
      - HTTP Analytics profile "simple_http_analytics_capture" with basic capture filter:
        - Collect only response codes 500 and 503;
      - Profile attached via `analyticsProfiles`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-analytics-capture-simple",
    "label": "HTTP Analytics simple with capture filter",
    "remark": "A simple example of HTTP Analytics profile with Capture filter",
    "Sample_http_analytics_capture_simple": {
      "class": "Tenant",
      "analyticsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.2.20"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "analyticsProfiles": [
            {
              "use": "simple_http_analytics_capture"
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
                "192.0.2.20",
                "192.0.2.21"
              ]
            }
          ]
        },
        "simple_http_analytics_capture": {
          "class": "Analytics_HTTP_Profile",
          "captureFilter": {
            "collectAll": false,
            "collectByResponseCode": [
              500,
              503
            ]
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

