# Creating an HTTP/2 monitor in a declaration

## Description

This AS3 declaration configures an HTTP/2 health monitor that sends an HTTP/2 request and validates the response. The monitor is applied to a pool of HTTP/2-capable servers.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_http2_01";
  - Folder of the Partition is named "A1";
    - An HTTP/2 monitor named "http2_monitor" with:
      - HTTP method, path, and expected response code;
    - A pool named "http2_pool" that uses "http2_monitor";
      - The pool includes two HTTP/2 servers on TCP port 443.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "http2-monitor-example",
    "label": "Creating an HTTP/2 monitor in a declaration",
    "remark": "HTTP/2 monitor example",
    "Sample_http2_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "http2_monitor": {
          "class": "Monitor",
          "monitorType": "http2",
          "interval": 5,
          "timeout": 16,
          "send": "GET /health HTTP/2\r\nHost: www.example.com\r\n\r\n",
          "recv": "200"
        },
        "http2_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "http2_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.2.80",
                "192.0.2.81"
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

---

