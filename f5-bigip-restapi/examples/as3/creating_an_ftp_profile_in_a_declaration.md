# Creating an FTP profile in a declaration

## Description

This declaration creates a custom FTP profile using AS3 and assigns it to an FTP virtual service. It demonstrates configuring FTP-specific options such as mode and security settings.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_06";
  - Application "A1";
    - FTP service "ftp_service" on 10.0.6.10:21;
      - Uses custom `FTP_Profile` "custom_ftp";
      - Pool "ftp_pool" with FTP servers;
    - FTP_Profile "custom_ftp":
      - `parentProfile` `/Common/ftp`;
      - Options like `security`, `dataPort`, or `port` mode configured;
    - Pool "ftp_pool":
      - Monitored by "tcp";
      - Members: 192.0.6.10:21 and 192.0.6.11:21.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-06",
    "label": "Creating an FTP profile in a declaration",
    "remark": "Custom FTP profile and FTP service",
    "Sample_nonhttp_06": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "ftp_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "virtualPort": 21,
          "profileFTP": {
            "use": "custom_ftp"
          },
          "pool": "ftp_pool"
        },
        "custom_ftp": {
          "class": "FTP_Profile",
          "parentProfile": {
            "bigip": "/Common/ftp"
          },
          "security": "enabled",
          "dataPort": 20
        },
        "ftp_pool": {
          "class": "Pool",
          "monitors": [
            "tcp"
          ],
          "members": [
            {
              "servicePort": 21,
              "serverAddresses": [
                "192.0.6.10",
                "192.0.6.11"
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


