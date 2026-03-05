# Virtual server listening on multiple ports on the same address

## Description

This declaration configures a single Service_HTTP object that listens on multiple TCP ports on the same virtual address. It uses the `virtualPort` array to expose the same application on several ports while using a single backend pool.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_06";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server named "service" on address "10.0.11.10";
      - Configured to listen on ports 80, 8080, and 8888 via `virtualPort: [80, 8080, 8888]`;
      - Uses a pool named "web_pool" monitored by "http";
        - The pool includes two members: "192.0.11.10:80" and "192.0.11.11:80".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "klmnop9012",
    "label": "Sample 6",
    "remark": "Virtual server listening on multiple ports on the same address",
    "Sample_http_06": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.11.10"
          ],
          "virtualPort": [
            80,
            8080,
            8888
          ],
          "pool": "web_pool"
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
                "192.0.11.10",
                "192.0.11.11"
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


