# Configuring enforcement properties in an HTTP profile

## Description

This declaration configures advanced enforcement properties in a custom HTTP profile and applies it to an HTTP virtual server. It controls HTTP protocol behavior, such as maximum header size, pipeline handling, and whether to enforce RFC compliance.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_10";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server "service" on address "10.0.15.10", port "80";
      - Uses a pool "web_pool" monitored by "http";
      - Uses a custom HTTP profile "http_enforced" via `profileHTTP`;
        - The HTTP profile sets enforcement-related properties such as:
          - `enforcement": "enabled"`;
          - `maxHeaderSize`, `maxRequests`, and pipeline settings;
          - Controls how strictly HTTP behavior is validated.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "ijklmn6789",
    "label": "Sample 10",
    "remark": "Configuring enforcement properties in an HTTP profile",
    "Sample_http_10": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.15.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileHTTP": {
            "use": "http_enforced"
          }
        },
        "http_enforced": {
          "class": "HTTP_Profile",
          "enforcement": "enabled",
          "maxHeaderSize": 32768,
          "maxRequests": 0,
          "pipelineAction": "allow",
          "acceptXff": true
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
                "192.0.15.10",
                "192.0.15.11"
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
