# Referencing a data group from an external URL with token authentication

## Description

This declaration pulls a data group from an external URL that requires an authentication token, similar to the earlier token URL example but specifically for data groups.

## Examples

- Explanation of the example:
  - Tenant "Sample_dgtoken_01";
  - Application "A1";
    - Data group "external_dg":
      - `url` with `authentication`:
        - `method: "bearer-token"`;
        - `token` value.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_dgtoken_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "external_dg": {
          "class": "Data_Group",
          "keyDataType": "string",
          "records": [
            {
              "url": "https://example.com/api/datagroups/app1",
              "authentication": {
                "method": "bearer-token",
                "token": "REPLACE_WITH_TOKEN"
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

---

