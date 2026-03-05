# Using Network Vectors in a DoS Profile

## Description

This declaration demonstrates configuring network-layer DoS vectors inside a DoS profile. It enables several common AFM network vectors (such as UDP Flood and ICMP Flood) with thresholds and attaches the profile to an L4 virtual server.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dos_04";
  - Folder of the Partition is named "network_vectors_example";
    - A service address "vs_addr" with IP 10.0.4.10;
    - An L4 virtual server "serviceMain" on 10.0.4.10:0 (all ports):
      - Uses DoS profile "network_dos_profile";
    - A DoS profile "network_dos_profile" with:
      - `network.enabled` set to true;
      - Network vectors configured, for example:
        - UDP Flood: enabled with rate-limit thresholds;
        - ICMP Flood: enabled with rate-limit thresholds;
        - TCP SYN Flood: enabled with thresholds;
    - A Security Log Profile "network_dos_log_profile" to log network DoS events.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "dos_04",
    "label": "Sample 4",
    "remark": "Using Network Vectors in a DoS Profile",
    "Sample_dos_04": {
      "class": "Tenant",
      "network_vectors_example": {
        "class": "Application",
        "template": "generic",
        "vs_addr": {
          "class": "Service_Address",
          "virtualAddress": "10.0.4.10"
        },
        "serviceMain": {
          "class": "Service_L4",
          "virtualAddresses": [
            {
              "use": "vs_addr"
            }
          ],
          "virtualPort": 0,
          "profileDOS": {
            "use": "network_dos_profile"
          },
          "securityLogProfiles": [
            {
              "use": "network_dos_log_profile"
            }
          ]
        },
        "network_dos_profile": {
          "class": "DoS_Profile",
          "network": {
            "enabled": true,
            "vectors": {
              "udpFlood": {
                "state": "enabled",
                "rateLimit": 100000
              },
              "icmpFlood": {
                "state": "enabled",
                "rateLimit": 50000
              },
              "tcpSynFlood": {
                "state": "enabled",
                "rateLimit": 20000
              }
            }
          }
        },
        "network_dos_log_profile": {
          "class": "Security_Log_Profile",
          "dosProtection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logDoSNetwork": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

