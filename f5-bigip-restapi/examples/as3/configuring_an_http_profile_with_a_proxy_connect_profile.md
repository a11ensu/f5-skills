# Configuring an HTTP profile with a Proxy Connect profile

## Description

This declaration defines a custom HTTP profile that references a Proxy Connect profile and applies it to an HTTP virtual server. It demonstrates using AS3 to configure explicit proxy capabilities for HTTP traffic.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_09";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server "service" on address "10.0.14.10", port "80";
      - Uses a pool "web_pool" monitored by "http";
      - Uses a custom HTTP profile "http_profile" via `profileHTTP`;
        - The HTTP profile references a Proxy Connect profile "proxy_connect_profile";
    - The Proxy Connect profile "proxy_connect_profile" enables explicit proxy behavior for HTTP CONNECT requests.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "cdefgh2345",
    "label": "Sample 9",
    "remark": "Configuring an HTTP profile with a Proxy Connect profile",
    "Sample_http_09": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.14.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileHTTP": {
            "use": "http_profile"
          }
        },
        "http_profile": {
          "class": "HTTP_Profile",
          "proxyConnectProfile": {
            "use": "proxy_connect_profile"
          }
        },
        "proxy_connect_profile": {
          "class": "Proxy_Connect_Profile",
          "idleTimeout": 300
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
                "192.0.14.10",
                "192.0.14.11"
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


