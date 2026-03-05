# bigip_device_connectivity


## Description

The `bigip_device_connectivity` module configures core device connectivity settings on BIG-IP, including management IP, host name, default route, VLAN and self-IP associations, and device trust parameters. It enables you to bootstrap or reconfigure how the BIG-IP is reachable on the network and how it participates in device clusters. Automating these settings streamlines initial deployments and ongoing network topology changes.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **hostname** | **Type:** string | Host name of the BIG-IP device. |
| **management_ip** | **Type:** string | Management IP address in CIDR notation (for example, `192.0.2.10/24`). |
| **management_gateway** | **Type:** string | Default gateway for the management network. |
| **config_sync_ip** | **Type:** string | IP address used for configuration sync in device groups. |
| **unicast_addresses** | **Type:** list | List of unicast addresses used for failover communication. |
| **unicast_addresses/address** | **Type:** string | IP address for failover unicast. |
| **unicast_addresses/port** | **Type:** integer | Port for failover communication. |
| **mirror_primary_address** | **Type:** string | Primary address used for connection mirroring. |
| **mirror_secondary_address** | **Type:** string | Secondary address used for connection mirroring. |
| **state** | **Choices:** present<br>**Default:** present | `present` ensures device connectivity settings match the provided parameters. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server\_port, validate\_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **hostname** | Effective host name of the device. |
| **management_ip** | Configured management IP address. |
| **management_gateway** | Configured management default gateway. |
| **config_sync_ip** | IP address used for config sync. |
| **unicast_addresses** | List of configured failover unicast addresses. |
| **changed** | Indicates whether any changes were made. |


## Examples


```yaml
- name: Configure hostname and management network
  bigip_device_connectivity:
    hostname: bigip1.example.com
    management_ip: 192.0.2.10/24
    management_gateway: 192.0.2.1
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Configure config sync and failover unicast addresses
  bigip_device_connectivity:
    config_sync_ip: 10.0.0.10
    unicast_addresses:
      - address: 10.0.0.10
        port: 1026
      - address: 10.0.1.10
        port: 1026
    mirror_primary_address: 10.0.0.10
    mirror_secondary_address: 10.0.1.10
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
