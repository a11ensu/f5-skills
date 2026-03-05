# Using an external monitor in a declaration

## Description

This AS3 declaration shows how to reference an existing external monitor from an AS3-managed pool. The external monitor script is pre-created on BIG-IP, and the declaration simply attaches that monitor to the pool via a “use” reference.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_external_monitor_01";
  - Folder of the Partition is named "A1";
    - An external monitor object "my_external_monitor" that points to an existing BIG-IP external monitor;
    - A pool named "app_pool" that uses "my_external_monitor";
      - The pool contains two application servers on TCP port 8080.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "external-monitor-example",
    "label": "Using an external monitor in a declaration",
    "remark": "External monitor example",
    "Sample_external_monitor_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "my_external_monitor": {
          "class": "Monitor",
          "monitorType": "external",
          "externalProgram": "/Shared/scripts/check_app.sh",
          "interval": 10,
          "timeout": 30
        },
        "app_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "my_external_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 8080,
              "serverAddresses": [
                "192.0.2.30",
                "192.0.2.31"
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

