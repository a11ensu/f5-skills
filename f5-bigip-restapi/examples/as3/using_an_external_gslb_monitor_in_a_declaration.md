# Using an external GSLB monitor in a declaration

## Description

This AS3 declaration demonstrates how to reference an existing external GSLB (DNS/GTM) monitor from an AS3-managed GSLB pool. The external monitor script is pre-created, and the declaration attaches that monitor to the GSLB pool.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_gslb_extmon_01";
  - Folder of the Partition is named "A1";
    - An external GSLB monitor named "gslb_ext_monitor" that references an existing GTM external monitor;
    - A GSLB pool named "gslb_pool" that uses "gslb_ext_monitor";
      - The pool contains two GSLB members (LDNS or server IPs) on UDP port 53.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "gslb-external-monitor-example",
    "label": "Using an external GSLB monitor in a declaration",
    "remark": "External GSLB monitor example",
    "Sample_gslb_extmon_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "gslb_ext_monitor": {
          "class": "GSLB_Monitor",
          "monitorType": "external",
          "externalProgram": "/Shared/scripts/gslb_check.sh",
          "interval": 10,
          "timeout": 30
        },
        "gslb_pool": {
          "class": "GSLB_Pool",
          "monitors": [
            {
              "use": "gslb_ext_monitor"
            }
          ],
          "members": [
            {
              "server": "gslb_server_1",
              "virtualServer": "vs_1"
            },
            {
              "server": "gslb_server_2",
              "virtualServer": "vs_2"
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

