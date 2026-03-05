# Configuring an HTML profile in a declaration

## Description

Shows how to configure an HTML profile and attach it to an HTTP service. HTML profiles can be used for content rewriting, compression, or other HTML-specific manipulations.

## Examples

- Explanation of the example:
  - Tenant named "Sample_html_profile";
  - Application named "htmlApp";
    - HTTP virtual server "service" on 10.0.25.10:80;
      - Pool "web_pool";
      - HTML profile "html_profile" of class "HTML_Profile";
      - Attached via `profileHTML`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "html-profile-01",
    "label": "Configuring an HTML profile",
    "remark": "Configuring an HTML profile in a declaration",
    "Sample_html_profile": {
      "class": "Tenant",
      "htmlApp": {
        "class": "Application",
        "template": "http",
        "service": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.25.10"
          ],
          "virtualPort": 80,
          "pool": "web_pool",
          "profileHTML": {
            "use": "html_profile"
          }
        },
        "web_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.25.10"
              ]
            }
          ]
        },
        "html_profile": {
          "class": "HTML_Profile",
          "rewriteAbsoluteUrls": "enabled"
        }
      }
    }
  }
}
```

## Tested json templates

</Output>
