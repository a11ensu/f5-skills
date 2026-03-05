# Using Splunk as a log destination

## Description

This declaration configures a remote log destination for Splunk using the `Log_Destination` and `Log_Publisher` classes, and attaches it to an HTTP service via an `Application`-level security/logging profile.

## Examples

- Explanation of the example:
  - Tenant "Sample_splunk_01";
  - Application "A1";
    - `logDestination_splunk`:
      - `class: Log_Destination` with remote high-speed logging to a Splunk server at `192.0.2.90:514`;
    - `logPublisher_app`:
      - `class: Log_Publisher` referencing `logDestination_splunk`;
    - HTTP service "service":
      - Virtual `10.0.7.10:80`;
      - Uses pool "web_pool";
      - Logging configured via `securityLogProfiles` referencing `logPublisher_app`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_splunk_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "logDestination_splunk": {
          "class": "Log_Destination",
          "type": "remote-high-speed-log",
          "protocol": "udp",
          "address": "192.0.2.90",
          "port": 514
        },
        "logPublisher_app": {
          "class": "Log_Publisher",
          "destinations": [
            {
              "use": "logDestination_splunk"
            }
          ]
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.7.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "securityLogProfiles": [
            {
              "bigip": "/Common/http"
            }
          ],
          "logPublisher": {
            "use": "logPublisher_app"
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
                "192.0.2.91"
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

