# Using Firewall Rules, Policies, and logging

## Description

This AS3 declaration demonstrates how to create and apply AFM firewall rules and policies, and how to enable logging of firewall events. It defines firewall address lists, a firewall rule, a firewall policy referencing that rule, and a security log profile, then attaches the policy and logging profile to a virtual server.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_01";
  - Folder (application) named "firewall_policy_logging";
    - Creates two firewall address lists for source and destination addresses;
    - Defines a firewall rule that references the address lists and allows traffic;
    - Creates a firewall policy that uses the rule;
    - Configures a security log profile for firewall logging;
    - Applies the firewall policy and log profile to a virtual server "serviceMain" listening on 10.0.1.10:80.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_01",
    "label": "Sample 1",
    "remark": "Using Firewall Rules, Policies, and logging",
    "Sample_network_security_01": {
      "class": "Tenant",
      "firewall_policy_logging": {
        "class": "Application",
        "template": "generic",
        "vs_addr": {
          "class": "Service_Address",
          "virtualAddress": "10.0.1.10"
        },
        "serviceMain": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            {
              "use": "vs_addr"
            }
          ],
          "virtualPort": 80,
          "policyFirewallEnforced": {
            "use": "my_firewall_policy"
          },
          "profileTCP": {
            "bigip": "/Common/f5-tcp-progressive"
          },
          "securityLogProfiles": [
            {
              "use": "my_firewall_log_profile"
            }
          ]
        },
        "my_src_address_list": {
          "class": "Firewall_Address_List",
          "addresses": [
            {
              "addr": "10.0.0.0/8"
            }
          ]
        },
        "my_dest_address_list": {
          "class": "Firewall_Address_List",
          "addresses": [
            {
              "addr": "192.168.0.0/16"
            }
          ]
        },
        "my_firewall_rule": {
          "class": "Firewall_Rule",
          "place-after": "first",
          "action": "accept",
          "log": "yes",
          "source": {
            "addressLists": [
              {
                "use": "my_src_address_list"
              }
            ]
          },
          "destination": {
            "addressLists": [
              {
                "use": "my_dest_address_list"
              }
            ]
          }
        },
        "my_firewall_policy": {
          "class": "Firewall_Policy",
          "rules": [
            {
              "use": "my_firewall_rule"
            }
          ]
        },
        "my_firewall_log_profile": {
          "class": "Security_Log_Profile",
          "application": {
            "localStorage": {
              "enabled": true
            }
          },
          "network": {
            "logFirewallEvents": true,
            "logIpErrors": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            }
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

