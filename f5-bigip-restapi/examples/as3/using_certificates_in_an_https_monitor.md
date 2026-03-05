# Using certificates in an HTTPS monitor

## Description

This AS3 declaration demonstrates an HTTPS health monitor that uses client certificate authentication. It references existing certificate and key objects on the BIG-IP and applies the HTTPS monitor to a pool of HTTPS servers.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_https_cert_01";
  - Folder of the Partition is named "A1";
    - An HTTPS monitor named "https_cert_monitor" with:
      - send/receive strings for HTTP validation;
      - client certificate and key references;
    - A pool named "https_pool" that uses "https_cert_monitor";
      - The pool includes two HTTPS servers on TCP port 443.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "https-cert-monitor-example",
    "label": "Using certificates in an HTTPS monitor",
    "remark": "HTTPS monitor with client certificate example",
    "Sample_https_cert_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "https_cert_monitor": {
          "class": "Monitor",
          "monitorType": "https",
          "interval": 5,
          "timeout": 16,
          "send": "GET /healthcheck HTTP/1.1\r\nHost: www.example.com\r\nConnection: close\r\n\r\n",
          "recv": "200 OK",
          "clientCertificate": {
            "bigip": "/Common/clientcert.crt"
          },
          "clientKey": {
            "bigip": "/Common/clientcert.key"
          }
        },
        "https_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "https_cert_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 443,
              "serverAddresses": [
                "192.0.2.60",
                "192.0.2.61"
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

