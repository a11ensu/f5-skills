# Using PATCH to add a new Application to a Tenant

## Description

This example shows how to use HTTP PATCH with AS3 to add a new Application to an existing Tenant without redeploying the entire declaration. It demonstrates the `patchBody` format where only the new Application object is included under an existing Tenant.

## Examples

- Explanation of the example:
  - Existing tenant named "Tenant1" already deployed on the BIG-IP;
  - PATCH request targets `/mgmt/shared/appsvcs/declare/Tenant1`;
  - Adds a new Application named "App2" to Tenant1;
    - `App2` is a generic application containing:
      - A Service_HTTP virtual named "web";
      - A Pool named "web_pool" with two members.

```json
{
  "class": "AS3",
  "patchBody": {
    "Tenant1": {
      "class": "Tenant",
      "App2": {
        "class": "Application",
        "template": "generic",
        "web": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.0.20"
          ],
          "pool": "web_pool"
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
                "192.0.2.10",
                "192.0.2.11"
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

