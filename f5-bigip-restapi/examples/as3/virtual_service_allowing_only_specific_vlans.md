# Virtual service allowing only specific VLANs

## Description

This declaration configures a virtual server that only accepts traffic from specified VLANs. It uses the `vlans` and `vlansEnabled` properties on a Service class to restrict which VLANs can access the virtual service.

## Examples

- Explanation of the example:
  - Tenant "Sample_vlan_01";
  - Application "A1";
    - HTTP service "service":
      - Virtual address `10.0.3.10:80`;
      - `vlansEnabled: true`;
      - `vlans` list includes `/Common/external` and `/Common/partners`;
      - Uses pool "web_pool";
    - Pool "web_pool" with two members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_vlan_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.3.10"
          ],
          "virtualPort": 80,
          "vlansEnabled": true,
          "vlans": [
            {
              "bigip": "/Common/external"
            },
            {
              "bigip": "/Common/partners"
            }
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
                "192.0.2.40",
                "192.0.2.41"
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

