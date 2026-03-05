# bigip_apm_acl

## Description

The `bigip_apm_acl` module facilitates the management of user-defined Access Policy Manager (APM) Access Control Lists (ACLs) on F5 BIG-IP systems. It enables administrators to create, update, or remove ACLs, specifying them as either static or dynamic types. The module supports defining granular access control entries (ACEs) that filter traffic based on Layer 4 properties (such as IP addresses, ports, and protocols) and Layer 7 attributes (including host names, URI paths, and schemes), enforcing actions like allow, reject, or discard on matching traffic.

## Parameters

| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **acl\_order** | **Type:** integer | Specifies the order of the ACL relative to others. If unset, it is placed after the last created ACL. Lower numbers (0-65535) indicate higher priority. |
| **description** | **Type:** string | User-defined description for the ACL. |
| **entries** | **Type:** list | A list of access control entries defining matching criteria and behavior. Order matters; changing order changes the device configuration. |
| **entries/action** | **Choices:** allow, reject, discard, continue<br>**Required:** yes | Specifies the action taken when an entry matches. |
| **entries/dst\_addr** | **Type:** string | Destination IP address. Set to `any` to match any address (ignores `dst_mask`). |
| **entries/dst\_mask** | **Type:** string | Destination network mask. If omitted and `dst_addr` is not `any`, `dst_addr` is treated as a host. |
| **entries/dst\_port** | **Type:** string | Destination port. Use `*` for all ports. Mutually exclusive with `dst_port_range`. |
| **entries/dst\_port\_range** | **Type:** string | Destination port range. Mutually exclusive with `dst_port`. |
| **entries/host\_name** | **Type:** string | Layer 7 only. Specifies the host the entry applies to. |
| **entries/log** | **Choices:** none, packet | Log level for the action. `none` (default) logs nothing; `packet` logs the matched packet. |
| **entries/paths** | **Type:** string | Layer 7 only. Path or paths the entry applies to. |
| **entries/protocol** | **Choices:** tcp, icmp, udp, all | Layer 4 only. Protocol the entry applies to. |
| **entries/scheme** | **Choices:** http, https, any | Layer 7 only. URI scheme the entry operates on. |
| **entries/src\_addr** | **Type:** string | Source IP address. Set to `any` to match any address (ignores `src_mask`). |
| **entries/src\_mask** | **Type:** string | Source network mask. If omitted and `src_addr` is not `any`, `src_addr` is treated as a host. |
| **entries/src\_port** | **Type:** string | Source port. Use `*` for all ports. Mutually exclusive with `src_port_range`. |
| **entries/src\_port\_range** | **Type:** string | Source port range. Mutually exclusive with `src_port`. |
| **name** | **Type:** string<br>**Required:** yes | The name of the ACL to manage. |
| **partition** | **Default:** Common | Device partition to manage resources on. |
| **path\_match\_case** | **Choices:** no, yes | Specifies if alphabetic case is considered when matching paths. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **state** | **Choices:** present, absent | `present` ensures the ACL exists; `absent` removes it. |
| **type** | **Choices:** static, dynamic | The type of ACL to create. Cannot be changed once set. |

## Return Values

| Key | Description |
| --- | --- |
| **acl\_order** | The order of this ACL relative to other ACLs. |
| **description** | The new description of the ACL. |
| **entries** | Access control entries defining the ACL matching and behavior. |
| **path\_match\_case** | Boolean indicating if case sensitivity is enabled for path matching. |
| **type** | The type of ACL created (e.g., static). |

## Examples

```yaml
- name: Create a static ACL with L4 entries
  bigip_apm_acl:
    name: L4foo
    acl_order: 0
    type: static
    entries:
      - action: allow
        dst_port: '80'
        dst_addr: '192.168.1.1'
        src_port: '443'
        src_addr: '10.10.10.0'
        src_mask: '255.255.255.128'
        protocol: tcp
      - action: reject
        dst_port: '*'
        dst_addr: '192.168.1.1'
        src_port: '*'
        src_addr: '10.10.10.0'
        src_mask: '255.255.255.128'
        protocol: tcp
        log: packet
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a static ACL with L7 entries
  bigip_apm_acl:
    name: L7foo
    acl_order: 1
    type: static
    path_match_case: false
    entries:
      - action: allow
        host_name: 'foobar.com'
        paths: '/shopfront'
        scheme: https
      - action: reject
        host_name: 'internal_foobar.com'
        paths: '/admin'
        scheme: any
        log: packet
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Create a static ACL with L7/L4 entries
  bigip_apm_acl:
    name: L7L4foo
    acl_order: 2
    type: static
    path_match_case: false
    entries:
      - action: allow
        host_name: 'foobar.com'
        paths: '/shopfront'
        scheme: https
        dst_port: '8181'
        dst_addr: '192.168.1.1'
        protocol: tcp
      - action: reject
        dst_addr: '192.168.1.1'
        host_name: 'internal_foobar.com'
        paths: '/admin'
        scheme: any
        protocol: all
        log: packet
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Modify a static ACL entries
  bigip_apm_acl:
    name: L4foo
    entries:
      - action: allow
        dst_port: '80'
        dst_addr: '192.168.1.1'
        src_port: '443'
        src_addr: '10.10.10.0'
        src_mask: '255.255.255.128'
        protocol: tcp
      - action: discard
        dst_port: '*'
        dst_addr: 192.168.1.1
        src_port: '*'
        src_addr: '10.10.10.0'
        src_mask: '255.2155.255.128'
        protocol: all
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove static ACL
  bigip_apm_acl:
    name: L4foo
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```

## Tested Playbooks