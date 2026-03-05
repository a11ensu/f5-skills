# Configuring management port log destinations

## Description

This declaration configures log destinations that send logs out the management port, using `Log_Destination` with the appropriate transport and referencing it from a `Log_Publisher` used by services.

## Examples

- Explanation of the example:
  - Tenant "Sample_mgmtlog_01";
  - Application "A1";
    - `logDestination_mgmt`:
      - `class: Log_Destination` with management transport to `192.0.2.190:514`;
    - `logPublisher_app` referencing this destination;
    - HTTP service "service" uses `logPublisher_app`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_mgmtlog_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "logDestination_mgmt": {
          "class": "Log_Destination",
          "type": "remote-syslog",
          "protocol": "udp",
          "useManagementPort": true,
          "address": "192.0.2.190",
          "port": 514
        },
        "logPublisher_app": {
          "class": "Log_Publisher",
          "destinations": [
            {
              "use": "logDestination_mgmt"
            }
          ]
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.17.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "logPublisher": {
            "use": "logPublisher_app"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.191"
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

