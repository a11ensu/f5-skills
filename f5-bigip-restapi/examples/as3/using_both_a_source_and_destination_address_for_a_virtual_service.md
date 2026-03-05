# Using both a source and destination address for a virtual service

## Description

This declaration configures a virtual server with both destination and source address filters. The `source` property restricts which client IP ranges may access the virtual, while `virtualAddresses` controls the destination address.

## Examples

- Explanation of the example:
  - Tenant "Sample_srcdst_01";
  - Application "A1";
    - HTTP service "service":
      - Virtual address `10.0.11.10:80`;
      - `source` set to `192.0.2.0/24`;
      - Only clients from that subnet can access the VIP;
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_srcdst_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.11.10"
          ],
          "virtualPort": 80,
          "source": "192.0.2.0/24",
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
                "192.0.2.140"
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

