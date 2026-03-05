# Referencing an existing RTSP profile in a declaration

## Description

Shows how to reference an existing RTSP profile from an AS3 declaration and apply it to an RTSP service.

## Examples

- Explanation of the example:
  - Tenant named "Sample_rtsp";
  - Application named "rtspApp";
    - L4 service "rtspService" on 10.0.15.10:554;
      - Pool "rtsp_pool";
      - Existing RTSP profile referenced via `profileRTSP` with `bigip`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.30.0",
    "id": "rtsp-01",
    "label": "Referencing an existing RTSP profile",
    "remark": "Referencing an existing RTSP profile in a declaration",
    "Sample_rtsp": {
      "class": "Tenant",
      "rtspApp": {
        "class": "Application",
        "rtspService": {
          "class": "Service_L4",
          "virtualAddresses": [
            "10.0.15.10"
          ],
          "virtualPort": 554,
          "pool": "rtsp_pool",
          "profileRTSP": {
            "bigip": "/Common/my_rtsp_profile"
          }
        },
        "rtsp_pool": {
          "class": "Pool",
          "members": [
            {
              "servicePort": 554,
              "serverAddresses": [
                "192.0.15.10"
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

