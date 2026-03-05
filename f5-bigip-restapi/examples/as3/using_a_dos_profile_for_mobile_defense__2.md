# Using a DoS profile for Mobile Defense

## Description

Shows how to configure a DoS profile specifically for Mobile Defense, protecting mobile applications from automated attacks. The DoS profile is attached to an HTTP service that serves mobile clients.

## Examples

- Explanation of the example:
  - Tenant named "Sample_dos_mobile";
  - Application named "mobileApp";
    - HTTP virtual server "service" on 10.0.8.20:80;
      - Pool "web_pool";
      - DoS profile "dos_mobile_profile" with Mobile Defense enabled;
      - Attached via `profileDOS`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "dos-mobile-01",
    "label": "Using a DoS profile for Mobile Defense",
    "remark": "Using a DoS profile for Mobile Defense",
    "Sample_dos_mobile": {
      "class": "Tenant",
      "mobileApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.20"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileDOS": {
            "use": "dos_mobile_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.8.20"
              ]
            }
          ]
        },
        "dos_mobile_profile": {
          "class": "DoS_Profile",
          "mobileDefense": {
            "enabled": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

