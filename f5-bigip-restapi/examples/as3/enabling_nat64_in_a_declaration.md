# Enabling NAT64 in a declaration

## Description

This declaration configures an HTTP virtual server with NAT64 translation enabled, allowing IPv6 clients to reach IPv4 backend servers. It uses the `nat64` property and defines an IPv6 virtual address with IPv4 pool members.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_08";
  - Folder of the Partition is named "A1";
    - An HTTP virtual server "service" listening on IPv6 address "2001:db8:10::10", port "80";
      - NAT64 is enabled via `"nat64": true`;
      - Uses a pool "web_pool" with IPv4 pool members;
      - The pool is monitored by "http" and has two members: "192.0.13.10:80" and "192.0.13.11:80".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "wxyzab7890",
    "label": "Sample 8",
    "remark": "Enabling NAT64 in a declaration",
    "Sample_http_08": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "2001:db8:10::10"
          ],
          "virtualPort": 80,
          "nat64": true,
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
                "192.0.13.10",
                "192.0.13.11"
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


