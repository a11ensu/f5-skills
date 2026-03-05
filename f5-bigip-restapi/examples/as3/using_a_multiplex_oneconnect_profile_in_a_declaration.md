# Using a Multiplex (OneConnect) profile in a declaration

## Description

Configures and applies a OneConnect (multiplex) profile in AS3 to reuse server-side connections for multiple client requests. The example shows attaching a OneConnect profile to an HTTP service to improve connection efficiency.

## Examples

- Explanation of the example:
  - Tenant named "Sample_oneconnect";
  - Application named "oneconnectApp";
    - HTTP virtual server "service" on 10.0.3.10:80;
      - Pool "web_pool" with two HTTP members;
      - A OneConnect profile "oneconnect_profile" of class "Multiplex_Profile";
      - The profile is attached via `profileMultiplex`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "oneconnect-01",
    "label": "Using a Multiplex (OneConnect) profile",
    "remark": "Using a Multiplex (OneConnect) profile in a declaration",
    "Sample_oneconnect": {
      "class": "Tenant",
      "oneconnectApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.3.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileMultiplex": {
            "use": "oneconnect_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.3.10",
                "192.0.3.11"
              ]
            }
          ]
        },
        "oneconnect_profile": {
          "class": "Multiplex_Profile",
          "maxSize": 10000,
          "maxAge": 600,
          "maxReuse": 1000,
          "sharePools": true
        }
      }
    }
  }
}
```

## Tested json templates

---

