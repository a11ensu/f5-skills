# Using Accelerated Signatures and TLS Signatures in a DoS profile

## Description

This declaration configures a DoS profile with Accelerated Signatures and TLS Signatures enabled for high-performance L7 DoS protection. It attaches the profile to an HTTPS virtual server and configures DoS logging to capture signature-based events.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dos_03";
  - Folder of the Partition is named "accelerated_tls_signatures";
    - A service address "vs_addr" with IP 10.0.3.10;
    - An HTTPS virtual server "serviceMain" on 10.0.3.10:443:
      - Uses TCP, HTTP, and client SSL profiles;
      - References DoS profile "dos_signatures_profile";
      - Uses security log profile "dos_signatures_log_profile";
    - A DoS profile "dos_signatures_profile" with:
      - `application.enabled` set to true;
      - `application.acceleratedSignatures.enabled` set to true;
      - `application.tlsSignatures.enabled` set to true;
    - A Security Log Profile "dos_signatures_log_profile" with:
      - DoS logging enabled for application and TLS signature events.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "dos_03",
    "label": "Sample 3",
    "remark": "Using Accelerated Signatures and TLS Signatures in a DoS profile",
    "Sample_dos_03": {
      "class": "Tenant",
      "accelerated_tls_signatures": {
        "class": "Application",
        "template": "generic",
        "vs_addr": {
          "class": "Service_Address",
          "virtualAddress": "10.0.3.10"
        },
        "serviceMain": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            {
              "use": "vs_addr"
            }
          ],
          "virtualPort": 443,
          "profileTCP": {
            "bigip": "/Common/f5-tcp-progressive"
          },
          "profileHTTP": {
            "bigip": "/Common/http"
          },
          "clientTLS": {
            "bigip": "/Common/clientssl"
          },
          "profileDOS": {
            "use": "dos_signatures_profile"
          },
          "securityLogProfiles": [
            {
              "use": "dos_signatures_log_profile"
            }
          ]
        },
        "dos_signatures_profile": {
          "class": "DoS_Profile",
          "application": {
            "enabled": true,
            "acceleratedSignatures": {
              "enabled": true
            },
            "tlsSignatures": {
              "enabled": true
            }
          }
        },
        "dos_signatures_log_profile": {
          "class": "Security_Log_Profile",
          "dosProtection": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logDoSApplication": true,
            "logDoSTlsSignatures": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

