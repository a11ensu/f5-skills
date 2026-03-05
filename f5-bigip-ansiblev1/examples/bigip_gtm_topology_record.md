# bigip_gtm_topology_record


## Description

The `bigip_gtm_topology_record` module manages GTM topology records on F5 BIG-IP systems. Topology records define matching rules between client and server attributes—such as geographic region, IP subnet, or ISP—to influence DNS load-balancing decisions. Use this module to create, adjust, or remove topology records, set match conditions, and assign order or score, enabling location-aware traffic steering and policy-based DNS routing across distributed infrastructures.


## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **description** | **Type:** string | Description of the topology record. |
| **ldns** | **Type:** string | Expression describing the LDNS (client) side of the topology (for example, `continent NA`, `subnet 203.0.113.0/24`). |
| **server** | **Type:** string | Expression describing the server side of the topology (for example, `datacenter dc-seattle`, `region europe`). |
| **score** | **Type:** integer | Score for the topology record; lower scores typically have higher preference. |
| **order** | **Type:** integer | Explicit order of the topology record in the list. |
| **name** | **Type:** string<br>**Required:** yes | Name of the topology record. |
| **partition** | **Default:** Common | Partition in which the topology record is managed. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc). |
| **state** | **Choices:** present, absent<br>**Default:** present | When `present`, ensures the topology record exists; when `absent`, removes it. |


## Return Values

| Key | Description |
| --- | --- |
| **name** | Name of the topology record. |
| **ldns** | LDNS side expression in the record. |
| **server** | Server side expression in the record. |
| **score** | Score associated with the topology record. |
| **order** | Effective order of the record in the topology list. |


## Examples

```yaml
- name: Prefer North America clients to Seattle datacenter
  bigip_gtm_topology_record:
    name: na_to_seattle
    ldns: "continent NA"
    server: "datacenter dc-seattle"
    score: 10
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Add subnet-based topology record
  bigip_gtm_topology_record:
    name: corp_subnet_to_dc1
    ldns: "subnet 203.0.113.0/24"
    server: "datacenter dc1"
    score: 5
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove a topology record
  bigip_gtm_topology_record:
    name: old_topology_rule
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



