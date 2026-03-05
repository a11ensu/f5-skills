# Using a Stream profile in a declaration

## Description

Shows how to configure and attach a Stream profile that performs on-the-fly content substitution in HTTP responses. The profile is attached to an HTTP virtual server.

## Examples

- Explanation of the example:
  - Tenant named "Sample_stream";
  - Application named "streamApp";
    - HTTP virtual server "service" on 10.0.11.10:80;
      - Pool "web_pool";
      - Stream profile "stream_profile" of class "Stream_Profile";
      - Attached via `profileStream`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "stream-01",
    "label": "Using a Stream profile",
    "remark": "Using a Stream profile in a declaration",
    "Sample_stream": {
      "class": "Tenant",
      "streamApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.11.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileStream": {
            "use": "stream_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.11.10"
              ]
            }
          ]
        },
        "stream_profile": {
          "class": "Stream_Profile",
          "expression": "@http://internal.example.com@https://external.example.com@"
        }
      }
    }
  }
}
```

## Tested json templates

---

