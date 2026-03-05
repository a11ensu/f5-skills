# Using BIG-IP PEM in a declaration

## Description

This AS3 declaration demonstrates how to configure BIG-IP PEM objects—such as a PEM profile, PEM policy, and subscriber management—within an AS3 tenant. It shows how to define a PEM policy with rules and actions, associate it with a PEM profile, and enable subscriber awareness for a service.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Example_PEM_01";
  - Folder of the Partition is named "PEM_App";
    - A PEM policy named "pem_policy_1" with rules that match traffic and apply PEM actions;
    - A PEM profile named "pem_profile_1" that references the PEM policy;
    - A subscriber management configuration that enables subscriber awareness;
    - A service (typically a virtual server) that uses the PEM profile to enforce policy on subscriber traffic.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.50.0",
    "id": "policy-enforcement-pem-example",
    "label": "Using BIG-IP PEM in a declaration",
    "remark": "Example of configuring PEM objects in AS3",
    "Example_PEM_01": {
      "class": "Tenant",
      "PEM_App": {
        "class": "Application",
        "template": "generic",
        "pem_policy_1": {
          "class": "PEM_Policy",
          "rules": [
            {
              "name": "rule1",
              "conditions": [
                {
                  "type": "ip",
                  "source": true,
                  "address": "0.0.0.0/0"
                }
              ],
              "actions": [
                {
                  "type": "classification",
                  "application": "web-browsing"
                }
              ]
            }
          ]
        },
        "pem_profile_1": {
          "class": "PEM_Profile",
          "policy": {
            "use": "pem_policy_1"
          },
          "subscriberManagement": {
            "enabled": true,
            "type": "Gx"
          }
        },
        "subscriber_management_1": {
          "class": "PEM_SubscriberManagement",
          "type": "Gx",
          "servers": [
            {
              "address": "198.51.100.10",
              "port": 3868
            }
          ]
        },
        "service_pem": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.0.10"
          ],
          "virtualPort": 0,
          "profilePEM": {
            "use": "pem_profile_1"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

