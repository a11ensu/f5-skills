# Creating an FTP profile in a declaration

## Description

Demonstrates how to create an FTP profile in AS3 and attach it to an FTP service. The profile controls FTP-specific behavior such as mode and security options.

## Examples

- Explanation of the example:
  - Tenant named "Sample_ftp_profile";
  - Application named "ftpApp";
    - L4 virtual server "ftpService" on 10.0.12.10:21;
      - Pool "ftp_pool";
      - FTP profile "ftp_profile" of class "FTP_Profile";
      - Attached via `profileFTP`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "ftp-profile-01",
    "label": "Creating an FTP profile",
    "remark": "Creating an FTP profile in a declaration",
    "Sample_ftp_profile": {
      "class": "Tenant",
      "ftpApp": {
        "class": "Application",
        "ftpService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.12.10"
          ],
          "virtualPort": 21,
          "pool": "ftp_pool",
          "profileFTP": {
            "use": "ftp_profile"
          }
        },
        "ftp_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 21,
              "serverAddresses": [
                "192.0.12.10"
              ]
            }
          ]
        },
        "ftp_profile": {
          "class": "FTP_Profile",
          "security": "none",
          "mode": "passive"
        }
      }
    }
  }
}
```

## Tested json templates

---

