# bigip_profile_persistence_cookie


## Description

The `bigip_profile_persistence_cookie` module manages cookie persistence profiles on F5 BIG-IP devices. Cookie persistence ensures that subsequent requests from a client are directed to the same back-end server by inserting or reusing a persistence cookie. This module allows administrators to configure cookie attributes such as name, expiration, and security flags, enabling stateful application behavior, improving user experience, and supporting session-based applications behind BIG-IP virtual servers.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **cookie_name** | **Type:** string | Name of the persistence cookie. |
| **description** | **Type:** string | User-defined description of the cookie persistence profile. |
| **expiration** | **Type:** integer | Cookie expiration time in seconds. |
| **httponly** | **Choices:** yes, no | Marks the cookie as HttpOnly to prevent client-side scripts from accessing it. |
| **method** | **Choices:** insert, rewrite, passive | Method used to manage the persistence cookie. |
| **name** | **Type:** string<br>**Required:** yes | Name of the cookie persistence profile. |
| **parent** | **Type:** string | Parent cookie persistence profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **secure** | **Choices:** yes, no | Marks the cookie as Secure (sent only over HTTPS). |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **cookie_name** | Name of the persistence cookie. |
| **description** | Description set on the profile. |
| **expiration** | Cookie expiration time. |
| **httponly** | Indicates if HttpOnly flag is set. |
| **method** | Cookie persistence method used. |
| **name** | Name of the cookie persistence profile managed. |
| **partition** | Partition where the profile is configured. |
| **secure** | Indicates if Secure flag is set. |


## Examples


```yaml
- name: Create cookie persistence profile with secure flags
  bigip_profile_persistence_cookie:
    name: cookie_persist_webapp
    description: Cookie persistence for web app
    parent: cookie
    cookie_name: WEBAPPSESSID
    method: insert
    expiration: 3600
    secure: yes
    httponly: yes
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Change cookie expiration
  bigip_profile_persistence_cookie:
    name: cookie_persist_webapp
    expiration: 7200
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove cookie persistence profile
  bigip_profile_persistence_cookie:
    name: old_cookie_persist
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



