# Using a RADIUS monitor in a declaration

## Description

This AS3 declaration configures a RADIUS health monitor that authenticates against a RADIUS server using a shared secret, username, and password. The monitor is applied to a pool of RADIUS servers.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_radius_01";
  - Folder of the Partition is named "A1";
    - A RADIUS monitor named "radius_monitor" with:
      - Username and password;
      - Shared secret and authentication port;
    - A pool named "radius_pool" that uses "radius_monitor";
      - The pool includes two RADIUS servers on UDP port 1812.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "radius-monitor-example",
    "label": "Using a RADIUS monitor in a declaration",
    "remark": "RADIUS monitor example",
    "Sample_radius_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "radius_monitor": {
          "class": "Monitor",
          "monitorType": "radius",
          "interval": 5,
          "timeout": 16,
          "username": "monitoruser",
          "password": "monitorpass",
          "secret": "sharedsecret",
          "radiusPort": 1812
        },
        "radius_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "radius_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 1812,
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

