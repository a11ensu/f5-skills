# Using Metadata in a declaration

## Description

This declaration shows how to attach arbitrary metadata to AS3 objects using the `metadata` property. Metadata is stored on the BIG-IP but not interpreted by AS3, allowing you to annotate Tenants, Applications, or individual objects with custom key/value information.

## Examples

- Explanation of the example:
  - Tenant "Sample_metadata_01" with tenant-level metadata:
    - Keys like "owner", "environment";
  - Application "A1" with its own metadata:
    - "appId", "team";
  - Pool "web_pool" and its members each have metadata:
    - Metadata used for CMDB references and operational notes.

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_metadata_01": {
      "class": "Tenant",
      "metadata": {
        "owner": "netops@example.com",
        "environment": "production"
      },
      "A1": {
        "class": "Application",
        "template": "generic",
        "metadata": {
          "appId": "APP-12345",
          "team": "WebPlatform"
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.2.10"
          ],
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "metadata": {
            "cmdbId": "CMDB-POOL-001"
          },
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.30",
                "192.0.2.31"
              ],
              "metadata": {
                "role": "primary"
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

