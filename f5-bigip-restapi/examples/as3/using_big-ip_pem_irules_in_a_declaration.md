# Using BIG-IP PEM iRules in a declaration

## Description

This AS3 declaration illustrates how to attach PEM-related iRules to a virtual service in a PEM-enabled deployment. It shows defining generic iRules in AS3 and applying them to a service that uses a PEM profile, allowing advanced subscriber or policy logic via iRules.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Example_PEM_iRules_01";
  - Folder of the Partition is named "PEM_iRules_App";
    - A PEM policy and PEM profile for subscriber-aware enforcement;
    - One or more iRules (for example, "pem_irule_1") that implement custom PEM logic;
    - A service (virtual server) that:
      - Listens on a specified IP/port;
      - Uses the PEM profile;
      - Has the PEM iRules attached for advanced traffic handling.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.50.0",
    "id": "policy-enforcement-pem-irules-example",
    "label": "Using BIG-IP PEM iRules in a declaration",
    "remark": "Example of attaching PEM iRules with AS3",
    "Example_PEM_iRules_01": {
      "class": "Tenant",
      "PEM_iRules_App": {
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
          }
        },
        "pem_irule_1": {
          "class": "iRule",
          "iRule": "when CLIENT_ACCEPTED {\n    # Example PEM iRule logic\n    PEM::subscriber lookup [IP::client_addr]\n}\n\nwhen PEM_POLICY_INIT {\n    # Modify or inspect PEM policy context\n}"
        },
        "service_pem_irule": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.0.20"
          ],
          "virtualPort": 0,
          "profilePEM": {
            "use": "pem_profile_1"
          },
          "iRules": [
            {
              "use": "pem_irule_1"
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

