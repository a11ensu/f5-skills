# Using existing FTP and SIP profiles in a declaration

## Description

This declaration shows how to reference existing BIG-IP FTP and SIP profiles from AS3. It creates FTP and SIP services that use the built-in profiles in the Common partition.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_05";
  - Application "A1";
    - FTP service "ftp_service" on 10.0.5.10:21:
      - Uses `profileFTP` with `bigip: "/Common/ftp"`;
      - Pool "ftp_pool" with FTP servers;
    - SIP service "sip_service" on 10.0.5.20:5060:
      - Uses `profileSIP` with `bigip: "/Common/sip"` (or `sip-udp`);
      - Pool "sip_pool" with SIP servers;
    - Both pools use appropriate monitors and members.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-05",
    "label": "Using existing FTP and SIP profiles in a declaration",
    "remark": "Reference existing FTP and SIP profiles",
    "Sample_nonhttp_05": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "ftp_service": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.5.10"
          ],
          "virtualPort": 21,
          "profileFTP": {
            "bigip": "/Common/ftp"
          },
          "pool": "ftp_pool"
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
                "192.0.5.10",
                "192.0.5.11"
              ]
            }
          ]
        },
        "sip_service": {
          "class": "Service_UDP",
          "virtualAddresses": [
            "10.0.5.20"
          ],
          "virtualPort": 5060,
          "profileSIP": {
            "bigip": "/Common/sip"
          },
          "pool": "sip_pool"
        },
        "sip_pool": {
          "class": "Pool",
          "monitors": [
            "udp"
          ],
          "members": [
            {
              "servicePort": 5060,
              "serverAddresses": [
                "192.0.5.20",
                "192.0.5.21"
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


