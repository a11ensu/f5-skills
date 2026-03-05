# Using adminState to disable a virtual, but leave the configuration

## Description

This example uses the `adminState` property on a Service to disable a virtual server without deleting it. The configuration remains on the BIG-IP but the virtual is not processing traffic.

## Examples

- Explanation of the example:
  - Tenant "Sample_adminstate_01";
  - Application "A1";
    - HTTP service "service":
      - `adminState: "disable"`;
      - Virtual `10.0.30.10:80`;
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_adminstate_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "service": {
          "class": "Service_HTTP",
          "adminState": "disable",
          "virtualAddresses": [
            "10.0.30.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.255"
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

