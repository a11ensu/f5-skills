# Using existing FTP and SIP profiles in a declaration

## Description

Illustrates how to reference pre-existing LTM FTP and SIP profiles from an AS3 declaration. The example configures FTP and SIP services that leverage those existing profiles instead of defining new ones.

## Examples

- Explanation of the example:
  - Tenant named "Sample_ftp_sip";
  - Application named "profileApp";
    - FTP virtual server "ftpService" on 10.0.4.10:21 referencing an existing FTP profile;
    - SIP virtual server "sipService" on 10.0.4.20:5060 referencing an existing SIP profile;
    - Both profiles are referenced via `use` and `bigip` pointers.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "ftp-sip-profiles",
    "label": "Using existing FTP and SIP profiles",
    "remark": "Using existing FTP and SIP profiles in a declaration",
    "Sample_ftp_sip": {
      "class": "Tenant",
      "profileApp": {
        "class": "Application",
        "ftpService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.4.10"
          ],
          "virtualPort": 21,
          "pool": "ftp_pool",
          "profileFTP": {
            "bigip": "/Common/my_ftp_profile"
          }
        },
        "ftp_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 21,
              "serverAddresses": [
                "192.0.4.10"
              ]
            }
          ]
        },
        "sipService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.4.20"
          ],
          "virtualPort": 5060,
          "pool": "sip_pool",
          "profileSIP": {
            "bigip": "/Common/my_sip_profile"
          }
        },
        "sip_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 5060,
              "serverAddresses": [
                "192.0.4.20"
              ]
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

