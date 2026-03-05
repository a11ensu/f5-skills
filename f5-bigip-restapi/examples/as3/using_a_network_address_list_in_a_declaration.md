# Using a network address list in a declaration

## Description

This AS3 declaration creates a Network Address List and uses it in a firewall rule to match traffic by source or destination networks. The rule is then included in a Firewall Policy for enforcement.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_12";
  - Folder (application) named "network_address_list";
    - Defines "trusted_networks" as a `Network_Address_List` with multiple CIDR ranges;
    - Creates firewall rule "allow_trusted" that uses the address list as source;
    - Adds the rule to firewall policy "fw_policy_trusted".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_12",
    "label": "Sample 12",
    "remark": "Using a network address list in a declaration",
    "Sample_network_security_12": {
      "class": "Tenant",
      "network_address_list": {
        "class": "Application",
        "template": "generic",
        "trusted_networks": {
          "class": "Network_Address_List",
          "addresses": [
            "10.10.0.0/16",
            "10.20.0.0/16",
            "192.168.100.0/24"
          ]
        },
        "allow_trusted": {
          "class": "Firewall_Rule",
          "place-after": "first",
          "action": "accept",
          "source": {
            "addressLists": [
              {
                "use": "trusted_networks"
              }
            ]
          }
        },
        "fw_policy_trusted": {
          "class": "Firewall_Policy",
          "rules": [
            {
              "use": "allow_trusted"
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

