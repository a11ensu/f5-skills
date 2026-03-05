# Creating a TCP Analytics profile in a declaration

## Description

Configures a TCP Analytics profile to collect TCP-level statistics such as RTT, retransmissions, and throughput, and attaches it to an L4 or HTTP service.

## Examples

- Explanation of the example:
  - Tenant named "Sample_tcp_analytics";
  - Application named "tcpAnalyticsApp";
    - L4 service "tcpService" on 10.0.16.10:80;
      - Pool "tcp_pool";
      - TCP Analytics profile "tcp_analytics_profile" of class "Analytics_TCP_Profile";
      - Attached via `profileAnalyticsTCP` (or `analyticsProfiles` depending on schema).

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "tcp-analytics-01",
    "label": "Creating a TCP Analytics profile",
    "remark": "Creating a TCP Analytics profile in a declaration",
    "Sample_tcp_analytics": {
      "class": "Tenant",
      "tcpAnalyticsApp": {
        "class": "Application",
        "tcpService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.16.10"
          ],
          "virtualPort": 80,
          "pool": "tcp_pool",
          "profileAnalyticsTCP": {
            "use": "tcp_analytics_profile"
          }
        },
        "tcp_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.16.10"
              ]
            }
          ]
        },
        "tcp_analytics_profile": {
          "class": "Analytics_TCP_Profile",
          "collectClientSideStats": true,
          "collectServerSideStats": true
        }
      }
    }
  }
}
```

## Tested json templates

---

