# Skipping a certificate check when referencing data groups from external URLs

## Description

This example shows how to skip TLS certificate validation when pulling data groups from an HTTPS URL by setting `skipCertificateCheck: true`. It’s useful in lab or self-signed environments (not recommended for production).

## Examples

- Explanation of the example:
  - Tenant "Sample_skipcert_01";
  - Application "A1";
    - Data group "external_dg":
      - `url: "https://..."`;
      - `skipCertificateCheck: true`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_skipcert_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "external_dg": {
          "class": "Data_Group",
          "keyDataType": "string",
          "records": [
            {
              "url": "https://example.local/datagroups/dg1",
              "skipCertificateCheck": true
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

