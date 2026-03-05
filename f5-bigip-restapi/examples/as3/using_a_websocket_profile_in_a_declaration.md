# Using a WebSocket profile in a declaration

## Description

Demonstrates how to configure and attach a WebSocket profile to an HTTP service in AS3. The WebSocket profile enables WebSocket protocol handling on the virtual server.

## Examples

- Explanation of the example:
  - Tenant named "Sample_websocket";
  - Application named "wsApp";
    - HTTP virtual server "service" on 10.0.6.10:80;
      - Pool "web_pool" with HTTP members;
      - WebSocket profile "ws_profile" of class "WebSocket_Profile";
      - Attached via `profileWebSocket`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "websocket-01",
    "label": "Using a WebSocket profile",
    "remark": "Using a WebSocket profile in a declaration",
    "Sample_websocket": {
      "class": "Tenant",
      "wsApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileWebSocket": {
            "use": "ws_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
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
        "ws_profile": {
          "class": "WebSocket_Profile",
          "idleTimeout": 300,
          "masking": "unmask",
          "proxyBufferHigh": 65535,
          "proxyBufferLow": 32768
        }
      }
    }
  }
}
```

## Tested json templates

---

