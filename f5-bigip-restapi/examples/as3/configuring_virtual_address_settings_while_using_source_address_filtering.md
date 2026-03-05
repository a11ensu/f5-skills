# Configuring virtual address settings while using Source address filtering

## Description

This declaration shows how to configure detailed `Service_Address` settings (such as `arpEnabled`, `icmpEcho`, etc.) while also applying source address filtering on the virtual service. The virtual references the Service_Address and has a `source` filter.

## Examples

- Explanation of the example:
  - Tenant "Sample_va_src_01";
  - Application "A1";
    - `Service_Address` "vipAddress":
      - IP `10.0.13.10`;
      - `arpEnabled: false`, `icmpEcho: "disabled"`;
    - HTTP service "service":
      - Uses `vipAddress` in `virtualAddresses`;
      - `source: "192.0.2.0/24"`;
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_va_src_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "vipAddress": {
          "class": "Service_Address",
          "virtualAddress": "10.0.13.10",
          "arpEnabled": false,
          "icmpEcho": "disabled"
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            {
              "use": "vipAddress"
            }
          ],
          "virtualPort": 80,
          "source": "192.0.2.0/24",
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.160"
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

