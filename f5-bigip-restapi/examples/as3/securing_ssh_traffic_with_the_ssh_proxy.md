# Securing SSH traffic with the SSH Proxy

## Description

This AS3 declaration configures AFM SSH Proxy to inspect and control SSH traffic. It defines an SSH Proxy profile with security settings, a firewall policy referencing the profile, and applies the policy to a virtual server handling SSH connections.

## Examples

- Explanation of the example:
  - Partition (tenant) named "Sample_network_security_03";
  - Folder (application) named "ssh_proxy_example";
    - Creates an AFM SSH Proxy profile "my_ssh_proxy" with key exchange, ciphers, and MACs;
    - Enables SSH command logging and session limits;
    - Builds a firewall rule "ssh_rule" that uses the SSH Proxy profile;
    - Adds a firewall policy "ssh_policy" containing the rule;
    - Applies the policy to a TCP virtual server "ssh_vs" on 10.0.3.10:22.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.36.0",
    "id": "network_security_03",
    "label": "Sample 3",
    "remark": "Securing SSH traffic with the SSH Proxy",
    "Sample_network_security_03": {
      "class": "Tenant",
      "ssh_proxy_example": {
        "class": "Application",
        "template": "generic",
        "my_ssh_proxy": {
          "class": "AFM_SSH_Profile",
          "kexAlgorithms": [
            "diffie-hellman-group-exchange-sha256"
          ],
          "ciphers": [
            "aes256-ctr",
            "aes192-ctr",
            "aes128-ctr"
          ],
          "macAlgorithms": [
            "hmac-sha2-256",
            "hmac-sha2-512"
          ],
          "logCommands": true,
          "maxSessions": 50
        },
        "ssh_rule": {
          "class": "Firewall_Rule",
          "place-after": "first",
          "action": "accept",
          "ipProtocol": "tcp",
          "destination": {
            "ports": [
              22
            ]
          },
          "sshProxyProfile": {
            "use": "my_ssh_proxy"
          }
        },
        "ssh_policy": {
          "class": "Firewall_Policy",
          "rules": [
            {
              "use": "ssh_rule"
            }
          ]
        },
        "ssh_vs": {
          "class": "Service_TCP",
          "virtualAddresses": [
            "10.0.3.10"
          ],
          "virtualPort": 22,
          "policyFirewallEnforced": {
            "use": "ssh_policy"
          }
        }
      }
    }
  }
}
```

## Tested json templates

---

