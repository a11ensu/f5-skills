# Creating an ALG log profile in a declaration

## Description

This declaration demonstrates how to configure an ALG (Application Layer Gateway) logging profile using AS3. It defines a Security Log Profile that logs ALG events (such as SIP or FTP) using a specified publisher.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_13";
  - Folder (application) named "alg_logging";
    - Creates "alg_log_profile" as a Security Log Profile;
    - Enables ALG logging and sets the log publisher to `/Common/local-db-publisher`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_13",
    "label": "Sample 13",
    "remark": "Creating an ALG log profile in a declaration",
    "Sample_network_security_13": {
      "class": "Tenant",
      "alg_logging": {
        "class": "Application",
        "template": "generic",
        "alg_log_profile": {
          "class": "Security_Log_Profile",
          "algLog": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            }
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

