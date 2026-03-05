# Adding logging for protocol inspection events

## Description

This AS3 declaration enables logging for AFM Protocol Inspection events. It defines a security logging profile configured for protocol inspection and attaches it to a virtual server using a Protocol Inspection policy.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_08";
  - Folder (application) named "pi_logging";
    - Creates a Protocol Inspection profile and policy ("pi_profile", "pi_policy");
    - Defines a Security Log Profile "pi_log_profile" with protocol inspection logging enabled;
    - Applies the PI policy and logging profile to an HTTP virtual server "pi_vs" on 10.0.8.10:80.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_08",
    "label": "Sample 8",
    "remark": "Adding logging for protocol inspection events",
    "Sample_network_security_08": {
      "class": "Tenant",
      "pi_logging": {
        "class": "Application",
        "template": "generic",
        "pi_profile": {
          "class": "Protocol_Inspection_Profile",
          "protocol": "http",
          "enforcementMode": "blocking"
        },
        "pi_policy": {
          "class": "Protocol_Inspection_Policy",
          "rules": [
            {
              "name": "inspect_http",
              "protocol": "http",
              "profile": {
                "use": "pi_profile"
              }
            }
          ]
        },
        "pi_log_profile": {
          "class": "Security_Log_Profile",
          "protocolInspection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logAllRequests": true,
            "logIllegalRequests": true
          }
        },
        "pi_vs": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 80,
          "protocolInspectionProfile": {
            "use": "pi_policy"
          },
          "securityLogProfiles": [
            {
              "use": "pi_log_profile"
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

