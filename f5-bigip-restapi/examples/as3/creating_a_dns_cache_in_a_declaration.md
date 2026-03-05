# Creating a DNS cache in a declaration

## Description

This AS3 declaration configures a DNS cache object and associates it with a DNS profile used by a DNS listener. It shows how to define a `DNS_Cache` object and link it to `DNS_Profile` so that all DNS traffic handled by the listener benefits from caching.

## Examples

- Explanation of the example:
  - Tenant named "Sample_dnscache_01";
  - Application named "A1";
    - A DNS cache object named "dns_cache_default" (`class: DNS_Cache`);
      - Type "transparent" cache;
      - Specifies a maximum cache size and enabled options;
    - A DNS profile "dns_profile_cache":
      - Uses the DNS cache "dns_cache_default";
    - A DNS listener service "dns_listener":
      - UDP listener on `10.0.20.10:53`;
      - Uses the DNS profile "dns_profile_cache".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "dns-cache-example-01",
    "label": "Creating a DNS cache",
    "remark": "Example of configuring a DNS cache and associating it with a DNS profile and listener",
    "Sample_dnscache_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "dns_cache_default": {
          "class": "DNS_Cache",
          "cacheType": "transparent",
          "maxSize": 10000,
          "answerDefaultZones": true
        },
        "dns_profile_cache": {
          "class": "DNS_Profile",
          "useCache": true,
          "cache": {
            "use": "dns_cache_default"
          }
        },
        "dns_listener": {
          "class": "Service_UDP",
          "virtualAddresses": [
            "10.0.20.10"
          ],
          "virtualPort": 53,
          "profileUDP": {
            "bigip": "/Common/udp"
          },
          "profileDNS": {
            "use": "dns_profile_cache"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

