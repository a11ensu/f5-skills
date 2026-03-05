# Using TLS 1.3 and Cipher rules and groups in a declaration

## Description

This declaration enables TLS 1.3 and uses Cipher Rules and Cipher Groups to define the cipher suites used by the TLS_Server profile. It shows how to build custom cipher policies via AS3.

## Examples

- Explanation of the example:
  - Tenant "Sample_tls_13";
  - Application "A1";
    - HTTPS service "service" on 10.0.13.10:443;
      - Uses TLS_Server "tls13TLS";
      - Pool "web_pool" with HTTP members;
    - Cipher_Rule "secureCiphers" specifying allowed ciphers (including TLSv1.3 suites);
    - Cipher_Group "secureGroup" referencing "secureCiphers";
    - TLS_Server "tls13TLS":
      - `tls1_3Enabled` = true;
      - `cipherGroup` uses "secureGroup";
      - Uses default certificate from /Common/default.crt and /Common/default.key.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "tls-example-13",
    "label": "Sample 13",
    "remark": "Using TLS 1.3 and Cipher rules and groups in a declaration",
    "Sample_tls_13": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "service": {
          "class": "Service_HTTPS",
          "virtualAddresses": [
            "10.0.13.10"
          ],
          "virtualPort": 443,
          "pool": "web_pool",
          "serverTLS": "tls13TLS"
        },
        "web_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.13.10",
                "192.0.13.11"
              ]
            }
          ]
        },
        "secureCiphers": {
          "class": "Cipher_Rule",
          "cipherSuites": [
            "TLS_AES_256_GCM_SHA384",
            "TLS_AES_128_GCM_SHA256",
            "ECDHE-ECDSA-AES256-GCM-SHA384",
            "ECDHE-RSA-AES256-GCM-SHA384"
          ]
        },
        "secureGroup": {
          "class": "Cipher_Group",
          "rules": [
            {
              "use": "secureCiphers"
            }
          ]
        },
        "tls13TLS": {
          "class": "TLS_Server",
          "tls1_3Enabled": true,
          "cipherGroup": {
            "use": "secureGroup"
          },
          "certificates": [
            {
              "certificate": {
                "bigip": "/Common/default.crt"
              },
              "privateKey": {
                "bigip": "/Common/default.key"
              }
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates


