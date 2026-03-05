# Enabling a MQTT profile on a TCP service in a declaration

## Description

This declaration enables a MQTT profile on a TCP-based service using `Service_TCP` and the `profileMQTT` property. It’s used for applications that speak MQTT over TCP.

## Examples

- Explanation of the example:
  - Tenant "Sample_mqtt_01";
  - Application "A1";
    - TCP service "mqtt_service":
      - Virtual `10.0.22.10:1883`;
      - Uses `/Common/mqtt` profile via `profileMQTT`;
      - Pool "mqtt_pool" with two members on port 1883.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_mqtt_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "mqtt_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.22.10"
          ],
          "virtualPort": 1883,
          "profileTCP": {
            "bigip": "/Common/tcp"
          },
          "profileMQTT": {
            "bigip": "/Common/mqtt"
          },
          "pool": "mqtt_pool"
        },
        "mqtt_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 1883,
              "serverAddresses": [
                "192.0.2.230",
                "192.0.2.231"
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

