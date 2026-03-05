# Using a DoS profile in a declaration

## Description

Configures and attaches an L7 DoS profile to an HTTP service to protect against denial-of-service attacks. The profile is created as `DoS_Profile` and referenced from the service.

## Examples

- Explanation of the example:
  - Tenant named "Sample_dos";
  - Application named "dosApp";
    - HTTP virtual server "service" on 10.0.8.10:80;
      - Pool "web_pool";
      - DoS profile "dos_profile" of class "DoS_Profile";
      - Attached via `profileDOS`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "dos-01",
    "label": "Using a DoS profile",
    "remark": "Using a DoS profile in a declaration",
    "Sample_dos": {
      "class": "Tenant",
      "dosApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileDOS": {
            "use": "dos_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.8.10"
              ]
            }
          ]
        },
        "dos_profile": {
          "class": "DoS_Profile",
          "application": {
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

