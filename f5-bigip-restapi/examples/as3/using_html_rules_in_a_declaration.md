# Using HTML rules in a declaration

## Description

This example configures HTML rules (such as search/replace, insert, or remove operations) in an HTML profile and applies it to an HTTP virtual. It demonstrates the general use of the `HTML_Profile` rules array.

## Examples

- Explanation of the example:
  - Tenant "Sample_htmlrules_01";
  - Application "A1";
    - `HTML_Profile` "html_profile":
      - Rule replacing a string in the response body;
    - HTTP service "service":
      - Uses "html_profile";
      - Virtual `10.0.28.10:80`;
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_htmlrules_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "html_profile": {
          "class": "HTML_Profile",
          "rules": [
            {
              "name": "replace-footer",
              "action": "replace",
              "target": "</body>",
              "content": "<footer>New Footer</footer></body>"
            }
          ]
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.28.10"
          ],
          "virtualPort": 80,
          "profileHTML": {
            "use": "html_profile"
          },
          "pool": "web_pool"
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.2.253"
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

