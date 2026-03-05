# Creating TCP and UDP monitors in a declaration

## Description

This AS3 declaration defines simple TCP and UDP health monitors and applies them to separate pools. The TCP monitor checks for a successful TCP handshake, while the UDP monitor validates UDP responses from back-end servers.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_tcp_udp_01";
  - Folder of the Partition is named "A1";
    - A TCP monitor named "tcp_monitor";
    - A UDP monitor named "udp_monitor";
    - A pool named "tcp_pool" that uses "tcp_monitor";
      - The pool includes two TCP application servers on port 80;
    - A pool named "udp_pool" that uses "udp_monitor";
      - The pool includes two UDP servers on port 514.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tcp-udp-monitor-example",
    "label": "Creating TCP and UDP monitors in a declaration",
    "remark": "TCP and UDP monitor example",
    "Sample_tcp_udp_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "tcp_monitor": {
          "class": "Monitor",
          "monitorType": "tcp",
          "interval": 5,
          "timeout": 16
        },
        "udp_monitor": {
          "class": "Monitor",
          "monitorType": "udp",
          "interval": 5,
          "timeout": 16,
          "send": "ping",
          "recv": "pong"
        },
        "tcp_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "tcp_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.100",
                "192.0.2.101"
              ]
            }
          ]
        },
        "udp_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "udp_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 514,
              "serverAddresses": [
                "192.0.2.110",
                "192.0.2.111"
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
