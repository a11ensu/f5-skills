# bigip_snat_translation


## Description

The `bigip_snat_translation` module manages individual SNAT translation addresses on BIG-IP systems. These addresses are used either directly by SNATs or as members of SNAT pools to translate the source IP of outbound connections. The module allows you to create, update, or delete translation addresses, control their traffic group membership, and specify connection limits or other attributes related to SNAT behavior.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the SNAT translation object. Often matches the IP address. |
| **address** | **Type:** string | IP address used for source translation. |
| **traffic_group** | **Type:** string | Traffic group associated with the translation address for HA (for example, `traffic-group-1`). |
| **connection_limit** | **Type:** integer | Maximum number of concurrent connections allowed through this translation address. |
| **partition** | **Default:** Common | Administrative partition where the SNAT translation resides. |
| **state** | **Choices:** present, absent | `present` creates or updates the translation address; `absent` removes it. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP, including server, user, password, server_port, and validate_certs. |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the SNAT translation managed. |
| **address** | IP address used for SNAT translation. |
| **traffic_group** | Traffic group assigned to the translation address. |
| **connection_limit** | Configured connection limit. |
| **changed** | Indicates whether the SNAT translation configuration was altered. |


## Examples


```yaml
- name: Create SNAT translation address for outbound traffic
  bigip_snat_translation:
    name: snat_198_51_100_200
    address: 198.51.100.200
    traffic_group: traffic-group-1
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Set connection limit on SNAT translation
  bigip_snat_translation:
    name: snat_198_51_100_200
    connection_limit: 50000
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove SNAT translation address
  bigip_snat_translation:
    name: old_snat_translation
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks
