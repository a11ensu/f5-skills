# Apply AFM Policies on the Route Domains

## Description

This AS3 declaration shows how to apply AFM firewall policies to specific route domains. It creates a firewall policy and then attaches it to a route domain using the `Firewall_Route_Domain` class.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_14";
  - Folder (application) named "afm_route_domains";
    - Creates a firewall rule "rd_allow_all" and policy "rd_policy";
    - Defines a `Firewall_Route_Domain` object "rd0_firewall" for route domain 0;
    - Applies the firewall policy to route domain 0 via `enforcedPolicy`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_14",
    "label": "Sample 14",
    "remark": "Apply AFM Policies on the Route Domains",
    "Sample_network_security_14": {
      "class": "Tenant",
      "afm_route_domains": {
        "class": "Application",
        "template": "generic",
        "rd_allow_all": {
          "class": "Firewall_Rule",
          "place-after": "first",
          "action": "accept"
        },
        "rd_policy": {
          "class": "Firewall_Policy",
          "rules": [
            {
              "use": "rd_allow_all"
            }
          ]
        },
        "rd0_firewall": {
          "class": "Firewall_Route_Domain",
          "routeDomain": {
            "bigip": "/Common/0"
          },
          "enforcedPolicy": {
            "use": "rd_policy"
          }
        }
      }
    }
  }
}
```

## Tested json templates
