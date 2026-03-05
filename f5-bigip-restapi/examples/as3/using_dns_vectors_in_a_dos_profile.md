# Using DNS Vectors in a DoS Profile

## Description

This declaration configures DNS-specific DoS vectors in a DoS profile and protects a DNS virtual server. It enables DNS query/response-based protections and logs DNS DoS events for analysis.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dos_05";
  - Folder of the Partition is named "dns_vectors_example";
    - A DNS virtual server "dns_vs" on 10.0.5.10:53 (UDP);
    - A DoS profile "dns_dos_profile" with:
      - `dns.enabled` set to true;
      - DNS vectors such as:
        - dnsQueryFlood;
        - dnsResponseFlood;
        - dnsMalformedQuery;
    - A Security Log Profile "dns_dos_log_profile" with DNS DoS logging enabled.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "dos_05",
    "label": "Sample 5",
    "remark": "Using DNS Vectors in a DoS Profile",
    "Sample_dos_05": {
      "class": "Tenant",
      "dns_vectors_example": {
        "class": "Application",
        "template": "generic",
        "dns_vs": {
          "class": "Service_UDP",
          "virtualAddresses": [
            "10.0.5.10"
          ],
          "virtualPort": 53,
          "profileDOS": {
            "use": "dns_dos_profile"
          },
          "securityLogProfiles": [
            {
              "use": "dns_dos_log_profile"
            }
          ]
        },
        "dns_dos_profile": {
          "class": "DoS_Profile",
          "dns": {
            "enabled": true,
            "vectors": {
              "dnsQueryFlood": {
                "state": "enabled",
                "rateLimit": 10000
              },
              "dnsResponseFlood": {
                "state": "enabled",
                "rateLimit": 10000
              },
              "dnsMalformedQuery": {
                "state": "enabled"
              }
            }
          }
        },
        "dns_dos_log_profile": {
          "class": "Security_Log_Profile",
          "dosProtection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logDoSDns": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

