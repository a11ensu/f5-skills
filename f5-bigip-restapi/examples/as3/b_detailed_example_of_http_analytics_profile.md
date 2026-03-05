# B: Detailed example of HTTP Analytics profile

## Description

Shows a fully customized HTTP Analytics profile with explicit settings for statistics collection, sampling, latency thresholds, and what to include in reports. This profile is then attached to an HTTP service to provide fine‑grained analytics behavior.

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_analytics_detailed";
  - Application named "analyticsApp";
    - A HTTP virtual server named "service" on 10.0.1.30:80;
      - A pool "web_pool" with two HTTP members and "http" monitor;
      - A detailed HTTP Analytics profile "detailed_http_analytics" that:
        - Enables collection of page-load time, latency, and response-code statistics;
        - Configures sampling rate, maximum TPS, and latency thresholds;
        - Enables collection of client IP, user agent, URI, and other dimensions;
      - The profile is attached via `analyticsProfiles`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-analytics-detailed",
    "label": "HTTP Analytics detailed",
    "remark": "Detailed example of HTTP Analytics profile",
    "Sample_http_analytics_detailed": {
      "class": "Tenant",
      "analyticsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.1.30"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "analyticsProfiles": [
            {
              "use": "detailed_http_analytics"
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
                "192.0.1.30",
                "192.0.1.31"
              ]
            }
          ]
        },
        "detailed_http_analytics": {
          "class": "Analytics_HTTP_Profile",
          "collectGeo": true,
          "collectIp": true,
          "collectUserAgent": true,
          "collectUrl": true,
          "collectResponseCode": true,
          "collectLatency": true,
          "collectClientSideStats": true,
          "collectServerSideStats": true,
          "samplingRate": 1,
          "maxTPS": 1000,
          "latencyThresholdMs": 500,
          "pageLoadTimeThresholdMs": 2000,
          "requestType": "all",
          "collectMethod": true,
          "collectSubnets": [
            "0.0.0.0/0"
          ]
        }
      }
    }
  }
}
```

## Tested json templates

---

