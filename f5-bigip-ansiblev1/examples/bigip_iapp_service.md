# bigip_iapp_service


## Description

The `bigip_iapp_service` module manages TCL iApp services on F5 BIG-IP devices. It allows you to deploy, update, or remove application services based on existing iApp templates. Using this module, you can supply template variables, control traffic group and device group behavior, and ensure consistent, repeatable application provisioning across your BIG-IP environment through Ansible automation.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **name** | **Type:** string<br>**Required:** yes | Name of the iApp service instance to manage. |
| **template** | **Type:** string | Name of the iApp template on which this service is based. Required when creating a new service. |
| **variables** | **Type:** dict | Key/value pairs corresponding to template variables that define the service configuration. |
| **state** | **Choices:** present, absent | Whether the iApp service should exist or be removed. |
| **traffic_group** | **Type:** string | Traffic group to associate with this iApp service, if applicable. |
| **device_group** | **Type:** string | Device group for sync/failover when using BIG-IP device clusters. |
| **partition** | **Default:** Common | Administrative partition in which to manage the iApp service. |
| **description** | **Type:** string | User-defined description for the iApp service instance. |
| **provider** | **Type:** dict | Connection details for the BIG-IP (server, user, password, server_port, validate_certs, etc.). |


## Return Values


| Key | Description |
| --- | --- |
| **name** | Name of the managed iApp service. |
| **template** | Template used to create or update the iApp service. |
| **variables** | Effective template variables applied to the service. |
| **traffic_group** | Traffic group associated with the service, if any. |
| **device_group** | Device group associated with the service, if any. |
| **changed** | Indicates if any change was made by the task. |


## Examples


```yaml
- name: Create an iApp service from an existing template
  bigip_iapp_service:
    name: my_app_service
    template: my_http_iapp
    variables:
      pool__addr: 10.10.10.10
      pool__port: 80
      monitor__interval: 5
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Update variables for an existing iApp service
  bigip_iapp_service:
    name: my_app_service
    variables:
      pool__addr: 10.10.10.20
      pool__port: 8080
    state: present
    provider: "{{ bip }}"
  delegate_to: localhost

- name: Remove an iApp service
  bigip_iapp_service:
    name: my_app_service
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



