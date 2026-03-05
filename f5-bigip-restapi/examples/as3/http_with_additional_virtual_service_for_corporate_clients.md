# HTTP with additional virtual service for corporate clients

## Description

This declaration defines an HTTP application with two virtual servers: one for general clients and an additional one dedicated to corporate clients, each listening on different destination addresses but sharing the same backend pool.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_03";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server named "public_service" on address "10.0.8.10", port "80";
    - A second HTTP virtual server named "corp_service" on address "10.0.8.20", port "80" for corporate users;
      - Both virtual servers use the same pool "web_pool";
      - The pool "web_pool" is monitored by the default "http" monitor;
        - The pool contains two members: "192.0.8.10:80" and "192.0.8.11:80".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "stuvwx67890",
    "label": "Sample 3",
    "remark": "HTTP with additional virtual service for corporate clients",
    "Sample_http_03": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "public_service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "corp_service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.20"
          ],
          "virtualPort": 80,
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
                "192.0.8.10",
                "192.0.8.11"
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


