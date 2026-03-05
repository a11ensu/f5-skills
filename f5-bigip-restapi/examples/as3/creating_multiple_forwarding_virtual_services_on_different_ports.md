# Creating multiple forwarding virtual services on different ports

## Description

This declaration creates multiple forwarding virtual services on the same address but different ports. It shows how to build several `Service_Forwarding` objects, each handling a specific port.

## Examples

- Explanation of the example:
  - Tenant "Sample_nonhttp_12";
  - Application "A1";
    - Forwarding service "fwd_80" on 0.0.0.0:80;
      - `forwardingType` "ip";
      - Forwards HTTP traffic between VLANs;
    - Forwarding service "fwd_443" on 0.0.0.0:443;
      - `forwardingType` "ip";
      - Forwards HTTPS traffic;
    - Both services:
      - Use VLANs `/Common/external` and `/Common/internal`;
      - Do not define pools (pure forwarding).

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.40.0",
    "id": "nonhttp-12",
    "label": "Creating multiple forwarding virtual services on different ports",
    "remark": "Multiple IP forwarding virtuals on different ports",
    "Sample_nonhttp_12": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "fwd_80": {
          "class": "Service_Forwarding",
          "virtualAddresses": [
            "0.0.0.0/0"
          ],
          "virtualPort": 80,
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
        "fwd_443": {
          "class": "Service_Forwarding",
          "virtualAddresses": [
            "0.0.0.0/0"
          ],
          "virtualPort": 443,
          "forwardingType": "ip",
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
