# Using an Analytics profile with a Capture filter

## Description

Demonstrates how to extend an HTTP Analytics profile with a capture filter so that only traffic matching specific criteria is captured and analyzed. The profile is attached to an HTTP service and uses a `captureFilter` object to limit captured data.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_analytics_capture";
  - Application named "analyticsApp";
    - HTTP virtual server "service" on 10.0.2.10:80;
      - Pool "web_pool" with two members and "http" monitor;
      - HTTP Analytics profile "http_analytics_capture" including a capture filter;
      - Capture filter limits analytics to specific URIs or response codes;
      - Profile attached via `analyticsProfiles`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-analytics-capture",
    "label": "HTTP Analytics with capture filter",
    "remark": "Using an Analytics profile with a Capture filter",
    "Sample_http_analytics_capture": {
      "class": "Tenant",
      "analyticsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.2.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "analyticsProfiles": [
            {
              "use": "http_analytics_capture"
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
                "192.0.2.10",
                "192.0.2.11"
              ]
            }
          ]
        },
        "http_analytics_capture": {
          "class": "Analytics_HTTP_Profile",
          "captureFilter": {
            "collectAll": false,
            "collectErrors": true,
            "collectByResponseCode": [
              500,
              502,
              503
            ],
            "collectByUrl": [
              "/checkout",
              "/login"
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

