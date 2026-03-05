# HTTP with custom persistence

## Description

This declaration deploys an HTTP application with a custom cookie persistence profile. It defines a single HTTP virtual server, a backend pool with two members, and a dedicated persistence object that tracks sessions using the JSESSIONID cookie.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_01";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server named "service" which listens on address "10.0.6.10", default HTTP port "80";
      - A pool named "web_pool" monitored by the default "http" health monitor;
        - The pool includes 2 pool members: "192.0.6.10:80" and "192.0.6.11:80";
      - A persistence profile named "jsessionid", which uses cookie-based persistence with hash method and cookie name "JSESSIONID", applied to the virtual server via `persistenceMethods`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "fghijkl7890",
    "label": "Sample 1",
    "remark": "HTTP with custom persistence",
    "Sample_http_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "pool": "web_pool",
          "persistenceMethods": [
            {
              "use": "jsessionid"
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
                "192.0.6.10",
                "192.0.6.11"
              ]
            }
          ]
        },
        "jsessionid": {
          "class": "Persist",
          "persistenceMethod": "cookie",
          "cookieMethod": "hash",
          "cookieName": "JSESSIONID"
        }
      }
    }
  }
}
```

## Tested json templates


