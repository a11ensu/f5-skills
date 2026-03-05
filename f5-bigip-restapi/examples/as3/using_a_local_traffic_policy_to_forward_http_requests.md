# Using a Local Traffic Policy to forward HTTP Requests

## Description

This declaration attaches a Local Traffic Policy to an HTTP virtual server to perform content-based request forwarding. The policy evaluates HTTP host and URI conditions and forwards matching traffic to specific pools.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_07";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server "service" on address "10.0.12.10", port "80";
      - Uses a default pool "default_pool";
      - Attaches a Local Traffic Policy "forward_policy" via the `policyHTTP` property;
        - The policy has rules that:
          - Match HTTP host "app.example.com" and URI path starting with "/images" and send to "images_pool";
          - Match HTTP host "app.example.com" and URI path starting with "/api" and send to "api_pool";
      - Pools "default_pool", "images_pool", and "api_pool" are all monitored by "http" and have their own members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "qrstuv3456",
    "label": "Sample 7",
    "remark": "Using a Local Traffic Policy to forward HTTP Requests",
    "Sample_http_07": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.12.10"
          ],
          "virtualPort": 80,
          "pool": "default_pool",
          "policyHTTP": [
            {
              "use": "forward_policy"
            }
          ]
        },
        "forward_policy": {
          "class": "Traffic_Policy",
          "rules": [
            {
              "name": "images_rule",
              "conditions": [
                {
                  "type": "httpHeader",
                  "name": "Host",
                  "values": [
                    "app.example.com"
                  ]
                },
                {
                  "type": "httpUri",
                  "pathStartsWith": [
                    "/images"
                  ]
                }
              ],
              "actions": [
                {
                  "type": "forward",
                  "pool": {
                    "use": "images_pool"
                  }
                }
              ]
            },
            {
              "name": "api_rule",
              "conditions": [
                {
                  "type": "httpHeader",
                  "name": "Host",
                  "values": [
                    "app.example.com"
                  ]
                },
                {
                  "type": "httpUri",
                  "pathStartsWith": [
                    "/api"
                  ]
                }
              ],
              "actions": [
                {
                  "type": "forward",
                  "pool": {
                    "use": "api_pool"
                  }
                }
              ]
            }
          ]
        },
        "default_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.12.10"
              ]
            }
          ]
        },
        "images_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.12.11"
              ]
            }
          ]
        },
        "api_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.12.12"
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


