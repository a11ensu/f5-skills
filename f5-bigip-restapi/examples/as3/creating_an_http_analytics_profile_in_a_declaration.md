# Creating an HTTP Analytics profile in a declaration

## Description

Defines how to create and attach an HTTP Analytics profile (`Analytics_HTTP_Profile`) to an HTTP application service in AS3. The profile controls collection of HTTP statistics such as page-load time, latency, and response codes, and is then referenced by the virtual server (Service_HTTP).

## Examples

- Explanation of the example:
  - Tenant named "Sample_http_analytics";
  - Application named "analyticsApp";
    - A HTTP virtual server named "service" that listens on 10.0.1.10:80;
      - A pool named "web_pool" with two members 192.0.1.10:80 and 192.0.1.11:80 monitored by "http";
      - An HTTP Analytics profile "http_analytics" of class "Analytics_HTTP_Profile";
      - The HTTP Analytics profile is attached to the service via the `analyticsProfiles` property.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "http-analytics-01",
    "label": "HTTP Analytics basic",
    "remark": "Creating an HTTP Analytics profile in a declaration",
    "Sample_http_analytics": {
      "class": "Tenant",
      "analyticsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.1.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "analyticsProfiles": [
            {
              "use": "http_analytics"
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
                "192.0.1.10",
                "192.0.1.11"
              ]
            }
          ]
        },
        "http_analytics": {
          "class": "Analytics_HTTP_Profile"
        }
      }
    }
  }
}
```

## Tested json templates

---

