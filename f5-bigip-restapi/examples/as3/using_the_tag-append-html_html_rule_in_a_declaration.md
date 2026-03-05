# Using the tag-append-html HTML rule in a declaration

## Description

This declaration uses an ASM/Advanced WAF HTML profile with the `tag-append-html` HTML rule, configured via AS3. It appends custom HTML content to responses.

## Examples

- Explanation of the example:
  - Tenant "Sample_tagappend_01";
  - Application "A1";
    - `HTML_Profile` "html_profile" with `tag-append-html` rule;
    - HTTP service "service":
      - Virtual `10.0.26.10:80`;
      - Uses "html_profile";
      - Uses pool "web_pool".

```json
{
  "class": "AS3",
  "action": "deploy",
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "Sample_tagappend_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "html_profile": {
          "class": "HTML_Profile",
          "rules": [
            {
              "name": "tag-append-html",
              "action": "append",
              "content": "<!-- appended by BIG-IP -->"
            }
          ]
        },
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.26.10"
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
                "192.0.2.252"
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

