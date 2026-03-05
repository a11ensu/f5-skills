# Using Clone Pools in a declaration

## Description

This declaration configures clone pools on a virtual server. Clone pools allow traffic to be copied to additional pools for out-of-band inspection (such as IDS/IPS) without affecting the main traffic flow.

## Examples

- Explanation of the example:
  - Tenant "Sample_clone_01";
  - Application "A1";
    - HTTP service "service" on `10.0.5.10:80`:
      - Primary pool "web_pool";
      - `clonePools` configured for:
        - `client` side clone pool "client_clone_pool";
        - `server` side clone pool "server_clone_pool";
    - Three pools:
      - "web_pool" for production traffic;
      - "client_clone_pool" for client-side mirroring;
      - "server_clone_pool" for server-side mirroring.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_clone_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.5.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "clonePools": {
            "client": "client_clone_pool",
            "server": "server_clone_pool"
          }
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
                "192.0.2.60"
              ]
            }
          ]
        },
        "client_clone_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "198.51.100.10"
              ]
            }
          ]
        },
        "server_clone_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "198.51.100.20"
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

