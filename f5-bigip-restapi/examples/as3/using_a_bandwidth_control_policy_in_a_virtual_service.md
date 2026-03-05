# Using a Bandwidth Control policy in a virtual service

## Description

This AS3 declaration shows how to configure and apply a PEM Bandwidth Control (BWC) policy to a virtual service. It defines a PEM policy that uses a Bandwidth Control action, associates it with a PEM profile, and attaches that profile to a virtual server so subscriber traffic is rate-limited according to the BWC policy.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Example_BWC_01";
  - Folder of the Partition is named "BWC_App";
    - A Bandwidth Control policy object defining rate limits;
    - A PEM policy that references the Bandwidth Control policy via an action;
    - A PEM profile that uses the PEM policy;
    - A service (virtual server) that:
      - Listens on a specified IP/port;
      - Uses the PEM profile so that BWC is enforced on traffic.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.50.0",
    "id": "policy-enforcement-bwc-example",
    "label": "Using a Bandwidth Control policy in a virtual service",
    "remark": "Example of configuring PEM Bandwidth Control with AS3",
    "Example_BWC_01": {
      "class": "Tenant",
      "BWC_App": {
        "class": "Application",
        "template": "generic",
        "bwc_policy_1": {
          "class": "PEM_BandwidthControlPolicy",
          "maximumRate": 1000000,
          "guaranteedRate": 500000,
          "burstSize": 20000
        },
        "pem_policy_bwc": {
          "class": "PEM_Policy",
          "rules": [
            {
              "name": "bwc_rule",
              "conditions": [
                {
                  "type": "ip",
                  "source": true,
                  "address": "0.0.0.0/0"
                }
              ],
              "actions": [
                {
                  "type": "bandwidthControl",
                  "policy": {
                    "use": "bwc_policy_1"
                  }
                }
              ]
            }
          ]
        },
        "pem_profile_bwc": {
          "class": "PEM_Profile",
          "policy": {
            "use": "pem_policy_bwc"
          }
        },
        "service_bwc": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.0.30"
          ],
          "virtualPort": 0,
          "profilePEM": {
            "use": "pem_profile_bwc"
          }
        }
      }
    }
  }
}
```

## Tested json templates
