# B: Detailed example of HTTP Analytics profile with Capture filter

## Description

Shows a fully customized HTTP Analytics profile combined with an advanced capture filter. The filter is configured to capture specific URLs, methods, response codes, and client subnets, while general analytics options are also explicitly defined.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_analytics_capture_detailed";
  - Application named "analyticsApp";
    - HTTP virtual server "service" on 10.0.2.30:80;
      - Pool "web_pool" with two HTTP members and "http" monitor;
      - Detailed HTTP Analytics profile "detailed_http_analytics_capture" that:
        - Enables detailed collection (IP, URL, user agent, geo, latency);
        - Uses a capture filter with:
          - Selected URLs and methods;
          - Specific response codes;
          - Subnet filters and thresholds;
      - Attached via `analyticsProfiles`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-analytics-capture-detailed",
    "label": "HTTP Analytics detailed with capture filter",
    "remark": "Detailed example of HTTP Analytics profile with Capture filter",
    "Sample_http_analytics_capture_detailed": {
      "class": "Tenant",
      "analyticsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.2.30"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "analyticsProfiles": [
            {
              "use": "detailed_http_analytics_capture"
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
                "192.0.2.30",
                "192.0.2.31"
              ]
            }
          ]
        },
        "detailed_http_analytics_capture": {
          "class": "Analytics_HTTP_Profile",
          "collectIp": true,
          "collectUrl": true,
          "collectUserAgent": true,
          "collectGeo": true,
          "collectLatency": true,
          "samplingRate": 1,
          "maxTPS": 2000,
          "captureFilter": {
            "collectAll": false,
            "collectErrors": true,
            "collectByResponseCode": [
              400,
              401,
              403,
              404,
              500,
              502,
              503
            ],
            "collectByUrl": [
              "/api",
              "/checkout",
              "/login"
            ],
            "collectByMethod": [
              "POST",
              "PUT",
              "DELETE"
            ],
            "collectBySubnet": [
              "10.0.0.0/8",
              "192.168.0.0/16"
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

