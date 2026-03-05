# Referencing an existing NTLM profile in a declaration

## Description

Shows how to reference an existing NTLM authentication profile in AS3 and attach it to an HTTP service for NTLM-based authentication.

## Examples

- Explanation of the example:
  - Tenant named "Sample_ntlm";
  - Application named "ntlmApp";
    - HTTP virtual server "service" on 10.0.23.10:80;
      - Pool "web_pool";
      - Existing NTLM profile referenced via `profileNTLM`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "ntlm-01",
    "label": "Referencing an existing NTLM profile",
    "remark": "Referencing an existing NTLM profile in a declaration",
    "Sample_ntlm": {
      "class": "Tenant",
      "ntlmApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.23.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileNTLM": {
            "bigip": "/Common/my_ntlm_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.23.10"
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

