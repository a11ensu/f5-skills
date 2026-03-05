# Using Client Certificate Constrained Delegation (C3D) features in a declaration

## Description

This declaration enables C3D on a TLS_Server profile, allowing the BIG-IP to extract client certificate information and securely delegate it to backend servers. It configures C3D settings and a corresponding TLS_Client profile to present delegated credentials upstream.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_08";
  - Application "A1";
    - HTTPS virtual "service" on 10.0.8.10:443;
      - Uses `serverTLS` "c3dServerTLS" and `clientTLS` "c3dClientTLS";
      - Pool "web_pool" with HTTPS members;
    - TLS_Server "c3dServerTLS":
      - Standard certificate/key;
      - `c3d` section enabled with a C3D profile name and options;
    - TLS_Client "c3dClientTLS":
      - Uses C3D to delegate client identity to servers;
      - Validates server certificates with a CA bundle.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-08",
    "label": "Sample 8",
    "remark": "Using Client Certificate Constrained Delegation (C3D) features in a declaration",
    "Sample_tls_08": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.8.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "c3dServerTLS",
          "clientTLS": "c3dClientTLS"
        },
        "web_pool": {
          "class": "Pool",
          "monitors": [
            "https"
          ],
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.8.10",
                "192.0.8.11"
              ]
            }
          ]
        },
        "c3dServerTLS": {
          "class": "TLS_Server",
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/default.crt"
              },
              "privateKey": {
                "bigip": "/Common/default.key"
              }
            }
          ],
          "c3d": {
            "enabled": true,
            "profile": {
              "bigip": "/Common/c3d"
            }
          }
        },
        "c3dClientTLS": {
          "class": "TLS_Client",
          "trustCA": {
            "bigip": "/Common/ca-bundle.crt"
          },
          "validateCertificate": true,
          "c3d": {
            "enabled": true
          }
        }
      }
    }
  }
}
```

## Tested json templates


