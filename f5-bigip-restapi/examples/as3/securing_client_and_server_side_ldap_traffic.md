# Securing client and server side LDAP traffic

## Description

This declaration secures both client-side and server-side LDAP traffic using TLS. It configures an LDAPS virtual server and uses TLS profiles to protect inbound and outbound LDAP connections.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_09";
  - Application "A1";
    - Service "ldap_service" using `Service_LDAP` on 10.0.9.10:636;
      - `serverTLS` = "ldapServerTLS";
      - `clientTLS` = "ldapClientTLS";
      - Pool "ldap_pool" with LDAP servers on port 636;
    - TLS_Server "ldapServerTLS" with certificate/key for LDAPS;
    - TLS_Client "ldapClientTLS" validating LDAP server certificates using a CA bundle.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-09",
    "label": "Sample 9",
    "remark": "Securing client and server side LDAP traffic",
    "Sample_tls_09": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "ldap_service": {
          "class": "Service_LDAP",
          "virtualAddresses": [
            "10.0.9.10"
          ],
          "virtualPort": 636,
          "pool": "ldap_pool",
          "serverTLS": "ldapServerTLS",
          "clientTLS": "ldapClientTLS"
        },
        "ldap_pool": {
          "class": "Pool",
          "monitors": [
            "ldap"
          ],
          "members": [
            {
              "servicePort": 636,
              "serverAddresses": [
                "192.0.9.10",
                "192.0.9.11"
              ]
            }
          ]
        },
        "ldapServerTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/ldap.crt"
              },
              "privateKey": {
                "bigip": "/Common/ldap.key"
              }
            }
          ]
        },
        "ldapClientTLS": {
          "class": "TLS_Client",
          "trustCA": {
            "bigip": "/Common/ca-bundle.crt"
          },
          "validateCertificate": true
        }
      }
    }
  }
}
```

## Tested json templates


