# Using IP or L2 Forwarding in a declaration

## Description

This declaration configures IP and/or L2 forwarding virtual services using `Service_L2` or `Service_Forwarding`. It demonstrates how to build a forwarding VIP for routing or switching traffic without terminating L4–L7 protocols.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_11";
  - Application "A1";
    - IP forwarding service "ip_forward" using `Service_Forwarding`;
      - `virtualAddresses` 0.0.0.0/0, `virtualPort` 0 (all ports);
      - `forwardingType` "ip";
      - Uses VLANs `/Common/external` and `/Common/internal`;
    - L2 forwarding service "l2_forward" using `Service_L2`;
      - `virtualAddresses` 0.0.0.0/0, `virtualPort` 0;
      - `forwardingType` "l2";
      - Same VLANs or others as needed.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-11",
    "label": "Using IP or L2 Forwarding in a declaration",
    "remark": "IP and L2 forwarding examples",
    "Sample_nonhttp_11": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "ip_forward": {
          "class": "Service_Forwarding",
          "virtualAddresses": [
            "0.0.0.0/0"
          ],
          "virtualPort": 0,
          "forwardingType": "ip",
          "vlans": [
            {
              "bigip": "/Common/external"
            },
            {
              "bigip": "/Common/internal"
            }
          ]
        },
        "l2_forward": {
          "class": "Service_L2",
          "virtualAddresses": [
            "0.0.0.0/0"
          ],
          "virtualPort": 0,
          "forwardingType": "l2",
          "vlans": [
            {
              "bigip": "/Common/external"
            },
            {
              "bigip": "/Common/internal"
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates


