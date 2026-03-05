# Referencing an IP Intelligence policy in a declaration

## Description

This declaration shows how to reference an existing IP Intelligence policy from AS3 and attach it to a virtual server. It assumes the IP Intelligence policy is pre-created on BIG-IP and uses the `bigip` pointer to bind it.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_11";
  - Folder (application) named "ip_intel_reference";
    - References an existing IP Intelligence policy `/Common/ip-intel-policy`;
    - Applies it to an HTTP virtual server "ipintel_vs" on 10.0.11.10:80 via `policyIpIntelligence`.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_11",
    "label": "Sample 11",
    "remark": "Referencing an IP Intelligence policy in a declaration",
    "Sample_network_security_11": {
      "class": "Tenant",
      "ip_intel_reference": {
        "class": "Application",
        "template": "generic",
        "ipintel_vs": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.11.10"
          ],
          "virtualPort": 80,
          "policyIpIntelligence": {
            "bigip": "/Common/ip-intel-policy"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

