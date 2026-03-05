# Setting Maximum Bandwidth on a virtual with AFM

## Description

This AS3 declaration configures AFM DoS or firewall bandwidth control on a virtual server. It sets a maximum bandwidth limit using a DoS profile or rate-shaping attributes and attaches it to a Service_HTTP virtual server.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_06";
  - Folder (application) named "afm_bandwidth_limit";
    - Defines a DoS profile "dos_profile_bw" with max bandwidth 100 Mbps;
    - Associates the DoS profile with the HTTP virtual server "bw_vs";
    - Virtual server listens on 10.0.6.10:80 and enforces AFM bandwidth control.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_06",
    "label": "Sample 6",
    "remark": "Setting Maximum Bandwidth on a virtual with AFM",
    "Sample_network_security_06": {
      "class": "Tenant",
      "afm_bandwidth_limit": {
        "class": "Application",
        "template": "generic",
        "dos_profile_bw": {
          "class": "DoS_Profile",
          "application": {
            "enabled": true,
            "maxBandwidth": 100000
          }
        },
        "bw_vs": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.6.10"
          ],
          "virtualPort": 80,
          "profileDOS": {
            "use": "dos_profile_bw"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

