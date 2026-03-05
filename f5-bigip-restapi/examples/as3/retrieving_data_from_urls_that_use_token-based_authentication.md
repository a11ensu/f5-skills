# Retrieving data from URLs that use token-based authentication

## Description

This example shows how to reference external data (such as iRules, data groups, or files) via URL that requires token-based authentication. It uses the `url` property with `authentication` details in the declaration.

## Examples

- Explanation of the example:
  - Tenant "Sample_tokenurl_01";
  - Application "A1";
    - Data group "external_dg" loaded from HTTPS URL;
      - `url` includes HTTP headers with `Authorization: Bearer <token>`;
    - Service uses this data group via iRule or profile (not detailed).

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_tokenurl_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "external_dg": {
          "class": "Data_Group",
          "keyDataType": "string",
          "records": [
            {
              "url": "https://example.com/api/datagroup",
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

