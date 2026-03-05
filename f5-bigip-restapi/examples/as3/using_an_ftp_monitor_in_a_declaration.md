# Using an FTP monitor in a declaration

## Description

This AS3 declaration shows how to configure an FTP health monitor that logs in with a username and password and issues an FTP command. The monitor is applied to a pool of FTP servers to verify service health.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_ftp_01";
  - Folder of the Partition is named "A1";
    - An FTP monitor named "ftp_monitor" with:
      - Username and password for login;
      - Optional FTP type and mode;
    - A pool named "ftp_pool" that uses "ftp_monitor";
      - The pool has two FTP servers on TCP port 21.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "ftp-monitor-example",
    "label": "Using an FTP monitor in a declaration",
    "remark": "FTP monitor example",
    "Sample_ftp_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "ftp_monitor": {
          "class": "Monitor",
          "monitorType": "ftp",
          "interval": 5,
          "timeout": 16,
          "username": "ftpuser",
          "password": "ftppass",
          "mode": "passive"
        },
        "ftp_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "ftp_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 21,
              "serverAddresses": [
                "192.0.2.50",
                "192.0.2.51"
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

