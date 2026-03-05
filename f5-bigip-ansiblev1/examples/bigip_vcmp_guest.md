# bigip_vcmp_guest


## Description

The `bigip_vcmp_guest` module manages Virtual Clustered Multiprocessing (vCMP) guests on F5 BIG-IP hardware platforms that support vCMP. It allows you to create, configure, start, stop, or delete guests, as well as assign CPU cores, memory, and VLANs. This module enables automated provisioning of virtual BIG-IP instances, simplifying multi-tenant deployments and optimizing resource utilization on vCMP-capable devices.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the vCMP guest. |
| **state** | **Choices:** present, absent, deployed, provisioned, configured<br>**Default:** present | Desired state of the vCMP guest, from configuration to full deployment. |
| **partition** | **Default:** Common | Administrative partition where the vCMP guest is defined. |
| **hostname** | **Type:** string | Hostname for the vCMP guest. |
| **cores_per_slot** | **Type:** integer | Number of CPU cores per slot assigned to the guest. |
| **memory** | **Type:** integer | Amount of memory (in MB) allocated to the guest. |
| **vlans** | **Type:** list | VLANs to which the guest is connected. |
| **management_ip** | **Type:** string | Management IP address for the guest. |
| **management_netmask** | **Type:** string | Netmask for the management IP. |
| **management_gateway** | **Type:** string | Default gateway for the management network. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP device. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the vCMP guest. |
| **hostname** | Hostname configured on the guest. |
| **cores_per_slot** | CPU cores per slot assigned. |
| **memory** | Memory allocated to the guest. |
| **vlans** | VLANs attached to the guest. |
| **management_ip** | Management IP address of the guest. |
| **state** | Final state of the guest (for example, `deployed`). |


## Examples


```yaml
- name: Create and provision a vCMP guest
  bigip_vcmp_guest:
    name: guest1
    hostname: guest1.example.com
    cores_per_slot: 2
    memory: 8192
    vlans:
      - /Common/external
      - /Common/internal
    management_ip: 10.1.1.10
    management_netmask: 255.255.255.0
    management_gateway: 10.1.1.1
    state: deployed
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a vCMP guest
  bigip_vcmp_guest:
    name: guest1
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



