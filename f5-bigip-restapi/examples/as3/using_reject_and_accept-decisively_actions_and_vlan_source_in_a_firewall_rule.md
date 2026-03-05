# Using reject and accept-decisively actions and VLAN source in a firewall rule

## Description

This declaration illustrates advanced AFM firewall rule actions (`reject` and `accept-decisively`) and how to match traffic based on source VLANs. It defines multiple rules with different actions and applies them via a firewall policy to a virtual server.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_04";
  - Folder (application) named "firewall_actions_vlans";
    - Creates three firewall rules:
      - "rule_reject": rejects traffic from specified VLANs;
      - "rule_accept_decisively": accepts traffic decisively on specific VLANs;
      - "rule_default": generic accept rule;
    - Uses VLAN names in the rule `source.vlans` match criteria;
    - Combines rules in "fw_policy_vlans";
    - Applies the policy to "vs_fw_vlans" virtual server on 10.0.4.10:80.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_04",
    "label": "Sample 4",
    "remark": "Using reject and accept-decisively actions and VLAN source in a firewall rule",
    "Sample_network_security_04": {
      "class": "Tenant",
      "firewall_actions_vlans": {
        "class": "Application",
        "template": "generic",
        "rule_reject": {
          "class": "Firewall_Rule",
          "place-after": "first",
          "action": "reject",
          "log": "yes",
          "source": {
            "vlans": [
              {
                "bigip": "/Common/external"
              }
            ]
          }
        },
        "rule_accept_decisively": {
          "class": "Firewall_Rule",
          "place-after": {
            "use": "rule_reject"
          },
          "action": "accept-decisively",
          "source": {
            "vlans": [
              {
                "bigip": "/Common/internal"
              }
            ]
          }
        },
        "rule_default": {
          "class": "Firewall_Rule",
          "place-after": {
            "use": "rule_accept_decisively"
          },
          "action": "accept"
        },
        "fw_policy_vlans": {
          "class": "Firewall_Policy",
          "rules": [
            {
              "use": "rule_reject"
            },
            {
              "use": "rule_accept_decisively"
            },
            {
              "use": "rule_default"
            }
          ]
        },
        "vs_fw_vlans": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.4.10"
          ],
          "virtualPort": 80,
          "policyFirewallEnforced": {
            "use": "fw_policy_vlans"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

