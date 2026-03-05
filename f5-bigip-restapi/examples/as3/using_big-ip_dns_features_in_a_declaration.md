# Using BIG-IP DNS features in a declaration

## Description

This AS3 declaration enables and configures BIG-IP DNS (formerly GTM) features such as a DNS listener and a DNS profile within a tenant/application. It shows how to provision DNS services alongside other LTM/ADC objects using AS3, including a DNS listener service that listens on UDP/53 and references a DNS profile.

## Examples

- Explanation of the example:
  - Top-level AS3 declaration with:
    - `class: "AS3"`, `action: "deploy"`, `persist: true`;
  - One tenant named "Sample_dns_01";
  - One application named "A1" in tenant "Sample_dns_01";
    - A DNS listener service named "dns_listener" (`class: Service_UDP`);
      - Listens on `10.0.10.10` port `53`;
      - Uses the built‑in UDP profile `"udp"` and a DNS profile `"dns_profile"`;
    - A DNS profile object named "dns_profile" (`class: DNS_Profile`);
      - Enables DNS functionality for the listener.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "dns-example-01",
    "label": "Using BIG-IP DNS features",
    "remark": "Example of configuring a DNS listener and DNS profile via AS3",
    "Sample_dns_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dns_listener": {
          "class": "Service_UDP",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 53,
          "profileUDP": {
            "bigip": "/Common/udp"
          },
          "profileDNS": {
            "use": "dns_profile"
          }
        },
        "dns_profile": {
          "class": "DNS_Profile",
          "answerDefaultZones": true
        }
      }
    }
  }
}
```

## Tested json templates

---

