# Creating an Idle Timeout policy in a declaration

## Description

This declaration demonstrates how to define AFM idle timeout policies via AS3. It creates a firewall policy with rules that set specific idle timeouts for different types of traffic and can be attached to virtual servers or route domains.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_07";
  - Folder (application) named "idle_timeout_policy";
    - Creates firewall rules with custom `idleTimeout` values:
      - "tcp_short_idle" for short-lived TCP sessions;
      - "udp_long_idle" for long-lived UDP flows;
    - Combines them into "idle_policy";
    - Policy is ready to be enforced on supported AFM contexts.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_07",
    "label": "Sample 7",
    "remark": "Creating an Idle Timeout policy in a declaration",
    "Sample_network_security_07": {
      "class": "Tenant",
      "idle_timeout_policy": {
        "class": "Application",
        "template": "generic",
        "tcp_short_idle": {
          "class": "Firewall_Rule",
          "place-after": "first",
          "action": "accept",
          "ipProtocol": "tcp",
          "idleTimeout": 60
        },
        "udp_long_idle": {
          "class": "Firewall_Rule",
          "place-after": {
            "use": "tcp_short_idle"
          },
          "action": "accept",
          "ipProtocol": "udp",
          "idleTimeout": 600
        },
        "idle_policy": {
          "class": "Firewall_Policy",
          "rules": [
            {
              "use": "tcp_short_idle"
            },
            {
              "use": "udp_long_idle"
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

