# Two applications sharing a pool

## Description

This declaration creates two separate applications (folders) under the same tenant, both referencing a common shared pool. It demonstrates how AS3 can centralize shared resources while allowing distinct application services.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_http_05";
  - Two Application folders named "App1" and "App2";
    - Each application defines an HTTP virtual server ("service1" and "service2") with different virtual addresses;
    - Both applications use the same pool "shared_pool" defined in a shared application "Shared";
      - The shared pool is monitored by "http";
        - It contains two pool members "192.0.10.10:80" and "192.0.10.11:80".

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "efghij5678",
    "label": "Sample 5",
    "remark": "Two applications sharing a pool",
    "Sample_http_05": {
      "class": "Tenant",
      "Shared": {
        "class": "Application",
        "shared_pool": {
          "class": "Pool",
          "monitors": [
            "http"
          ],
          "members": [
            {
              "servicePort": 80,
              "serverAddresses": [
                "192.0.10.10",
                "192.0.10.11"
              ]
            }
          ]
        }
      },
      "App1": {
        "class": "Application",
        "service1": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.10.10"
          ],
          "virtualPort": 80,
          "pool": {
            "use": "/Sample_http_05/Shared/shared_pool"
          }
        }
      },
      "App2": {
        "class": "Application",
        "service2": {
          "class": "Service_HTTP",
          "virtualAddresses": [
            "10.0.10.20"
          ],
          "virtualPort": 80,
          "pool": {
            "use": "/Sample_http_05/Shared/shared_pool"
          }
        }
      }
    }
  }
}
```

## Tested json templates


