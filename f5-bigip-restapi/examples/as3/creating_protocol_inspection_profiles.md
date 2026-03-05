# Creating Protocol Inspection profiles

## Description

This declaration shows how to create AFM Protocol Inspection profiles and policies using AS3. It defines inspection profiles for specific protocols and a policy that can be attached to a virtual server or firewall rule for deep protocol validation.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_05";
  - Folder (application) named "protocol_inspection_profiles";
    - Creates a Protocol Inspection profile "http_inspection" for HTTP;
    - Creates a Protocol Inspection profile "dns_inspection" for DNS;
    - Builds a Protocol Inspection policy "pi_policy" that references both profiles;
    - The policy is ready for use with AFM firewall rules or virtual servers.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_05",
    "label": "Sample 5",
    "remark": "Creating Protocol Inspection profiles",
    "Sample_network_security_05": {
      "class": "Tenant",
      "protocol_inspection_profiles": {
        "class": "Application",
        "template": "generic",
        "http_inspection": {
          "class": "Protocol_Inspection_Profile",
          "protocol": "http",
          "enforcementMode": "blocking",
          "violations": {
            "bad-header": "alarm",
            "oversized-request": "block"
          }
        },
        "dns_inspection": {
          "class": "Protocol_Inspection_Profile",
          "protocol": "dns",
          "enforcementMode": "blocking",
          "violations": {
            "malformed-query": "block",
            "oversized-response": "alarm"
          }
        },
        "pi_policy": {
          "class": "Protocol_Inspection_Policy",
          "rules": [
            {
              "name": "inspect_http",
              "protocol": "http",
              "profile": {
                "use": "http_inspection"
              }
            },
            {
              "name": "inspect_dns",
              "protocol": "dns",
              "profile": {
                "use": "dns_inspection"
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

