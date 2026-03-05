# Adding ports to a protocol inspection profile

## Description

This declaration shows how to associate specific ports with a Protocol Inspection profile so that AFM applies inspection only to traffic on those ports. It updates the profile to include a list of ports and uses it in a PI policy.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_09";
  - Folder (application) named "pi_ports";
    - Creates a Protocol Inspection profile "http_pi_ports" with protocol http;
    - Adds ports 80 and 8080 to the profile;
    - Builds a PI policy "pi_policy_ports" using the profile;
    - The policy can be referenced by AFM rules or virtual servers.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_09",
    "label": "Sample 9",
    "remark": "Adding ports to a protocol inspection profile",
    "Sample_network_security_09": {
      "class": "Tenant",
      "pi_ports": {
        "class": "Application",
        "template": "generic",
        "http_pi_ports": {
          "class": "Protocol_Inspection_Profile",
          "protocol": "http",
          "ports": [
            80,
            8080
          ]
        },
        "pi_policy_ports": {
          "class": "Protocol_Inspection_Policy",
          "rules": [
            {
              "name": "inspect_http_ports",
              "protocol": "http",
              "profile": {
                "use": "http_pi_ports"
              }
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

