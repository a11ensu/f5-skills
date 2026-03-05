# Using a DNS monitor in a declaration

## Description

This AS3 declaration demonstrates configuring a DNS health monitor that sends a specific DNS query and validates the response. The monitor is applied to a pool so that pool members are checked via DNS lookups for a particular name, type, and expected response.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_dns_01";
  - Folder of the Partition is named "A1";
    - A DNS monitor named "dns_monitor" with:
      - Query name (qname);
      - Query type (qtype), such as "A";
      - Expected response (acceptRcode, answerContains);
    - A pool named "dns_pool" that uses "dns_monitor";
      - The pool includes two DNS servers on UDP port 53.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "dns-monitor-example",
    "label": "Using a DNS monitor in a declaration",
    "remark": "DNS monitor example",
    "Sample_dns_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dns_monitor": {
          "class": "Monitor",
          "monitorType": "dns",
          "interval": 5,
          "timeout": 16,
          "qname": "www.example.com",
          "qtype": "A",
          "acceptRcode": "noerror",
          "answerContains": "192.0.2.100"
        },
        "dns_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "dns_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 53,
              "serverAddresses": [
                "192.0.2.20",
                "192.0.2.21"
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

