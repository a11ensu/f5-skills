# Referencing an iFile in an iRule declaration

## Description

This declaration references an iFile from within an iRule created by AS3. The iRule uses the iFile to serve or process content, and AS3 links to the existing iFile using the `bigip` pointer.

## Examples

- Explanation of the example:
  - Tenant "Sample_ifile_01";
  - Application "A1";
    - iRule "serve_ifile" referencing `/Common/my_ifile`;
    - HTTP service "service":
      - Attaches the "serve_ifile" iRule.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_ifile_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "serve_ifile": {
          "class": "iRule",
          "iRule": "when HTTP_REQUEST { HTTP::respond 200 content [ifile get /Common/my_ifile] }"
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.23.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "iRules": [
            {
              "use": "serve_ifile"
            }
          ]
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.240"
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

