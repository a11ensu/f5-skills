# Configuring a Security Logging Profile with Bot defense

## Description

This AS3 declaration configures a Security Log Profile that includes Bot Defense logging, suitable for Advanced WAF/Bot Defense deployments. It enables relevant logging options and prepares the profile for attachment to virtual servers with bot protection.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_10";
  - Folder (application) named "bot_defense_logging";
    - Defines a Security Log Profile "bot_log_profile";
    - Enables application, DoS, and Bot Defense logging;
    - Configures a log publisher and categories of bot-related events to log.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_10",
    "label": "Sample 10",
    "remark": "Configuring a Security Logging Profile with Bot defense",
    "Sample_network_security_10": {
      "class": "Tenant",
      "bot_defense_logging": {
        "class": "Application",
        "template": "generic",
        "bot_log_profile": {
          "class": "Security_Log_Profile",
          "application": {
            "localStorage": {
              "enabled": true
            }
          },
          "dosProtection": {
            "enabled": true
          },
          "botDefense": {
            "enabled": true,
            "publisher": {
              "bigip": "/Common/local-db-publisher"
            },
            "logBotSignatures": true,
            "logBrowserChallenges": true,
            "logCaptchaChallenges": true
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

