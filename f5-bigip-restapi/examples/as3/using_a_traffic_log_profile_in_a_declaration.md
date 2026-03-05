# Using a Traffic Log profile in a declaration

## Description

Shows how to configure and apply a Traffic Log profile to an application service in AS3. The profile controls what traffic is logged and how, typically for troubleshooting or compliance.

## Examples

- Explanation of the example:
  - Tenant named "Sample_traffic_log";
  - Application named "logApp";
    - HTTP virtual server "service" on 10.0.5.10:80;
      - Pool "web_pool" with HTTP members;
      - Traffic Log profile "traffic_log_profile" of class "Traffic_Log_Profile";
      - Attached to the service via `profileTrafficLog`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "traffic-log-01",
    "label": "Using a Traffic Log profile",
    "remark": "Using a Traffic Log profile in a declaration",
    "Sample_traffic_log": {
      "class": "Tenant",
      "logApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.5.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileTrafficLog": {
            "use": "traffic_log_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.5.10",
                "192.0.5.11"
              ]
            }
          ]
        },
        "traffic_log_profile": {
          "class": "Traffic_Log_Profile",
          "logPublisher": {
            "bigip": "/Common/local-db-publisher"
          },
          "logProfile": {
            "bigip": "/Common/http"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

