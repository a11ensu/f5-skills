# Using an LDAP monitor in a declaration

## Description

This AS3 declaration shows how to define and use a custom LDAP health monitor for a pool. The monitor is configured with an LDAP filter, base DN, and required attributes, and is then attached to a pool whose members are monitored via LDAP queries.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_ldap_01";
  - Folder of the Partition is named "A1";
    - An LDAP monitor named "ldap_monitor" with:
      - A base distinguished name (baseDn);
      - An LDAP filter string (filter);
      - Requested attributes for the query (attributes);
    - A pool named "ldap_pool" that uses the "ldap_monitor";
      - The pool has two LDAP servers as members on TCP port 389.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "ldap-monitor-example",
    "label": "Using an LDAP monitor in a declaration",
    "remark": "LDAP monitor example",
    "Sample_ldap_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "ldap_monitor": {
          "class": "Monitor",
          "monitorType": "ldap",
          "interval": 5,
          "timeout": 16,
          "baseDn": "dc=example,dc=com",
          "filter": "(objectClass=person)",
          "attributes": [
            "cn",
            "sn"
          ]
        },
        "ldap_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "ldap_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 389,
              "serverAddresses": [
                "192.0.2.10",
                "192.0.2.11"
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

