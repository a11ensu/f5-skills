# bigip_profile_analytics


## Description

The `bigip_profile_analytics` module manages HTTP analytics profiles on F5 BIG-IP systems. It allows administrators to create, modify, or remove analytics profiles that collect statistics about HTTP traffic, such as page load times, user behavior, and application performance. These profiles can be associated with virtual servers to enable detailed visibility and troubleshooting for web applications, helping operations teams monitor SLAs, identify performance bottlenecks, and optimize user experience.


## Parameters


| Parameter | Choices/Defaults | Comments |
| --- | --- | --- |
| **capture_cookies** | **Choices:** yes, no | Enables or disables the collection of HTTP cookie information for analytics. |
| **capture_headers** | **Type:** list | A list of HTTP headers to capture for analysis. |
| **capture_request_uri** | **Choices:** yes, no | Specifies whether to capture the full request URI. |
| **description** | **Type:** string | User-defined description of the analytics profile. |
| **name** | **Type:** string<br>**Required:** yes | Name of the HTTP analytics profile. |
| **parent** | **Type:** string | Name of the parent analytics profile to inherit settings from. |
| **partition** | **Default:** Common | Partition in which the profile resides. |
| **provider** | **Type:** dictionary | Connection details for the BIG-IP. |
| **sampling_mode** | **Choices:** coverage, dedicated, manual | Defines how traffic is sampled for analytics. |
| **sampling_rate** | **Type:** integer | Percentage or absolute rate (depending on mode) of traffic to sample. |
| **state** | **Choices:** present, absent | When `present`, ensures the profile exists; when `absent`, removes it. |


## Return Values


| Key | Description |
| --- | --- |
| **capture_cookies** | Final cookie capture setting of the profile. |
| **capture_headers** | List of headers configured for capture. |
| **capture_request_uri** | Indicates if the request URI is captured. |
| **description** | Description set on the profile. |
| **name** | Name of the analytics profile managed. |
| **partition** | Partition where the profile is configured. |
| **sampling_mode** | Effective sampling mode of the profile. |
| **sampling_rate** | Effective sampling rate used for analytics. |


## Examples


```yaml
- name: Create HTTP analytics profile with URI and cookie capture
  bigip_profile_analytics:
    name: webapp_analytics
    description: Analytics for main web application
    capture_request_uri: yes
    capture_cookies: yes
    capture_headers:
      - User-Agent
      - X-Forwarded-For
    sampling_mode: coverage
    sampling_rate: 10
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Adjust sampling on existing analytics profile
  bigip_profile_analytics:
    name: webapp_analytics
    sampling_mode: manual
    sampling_rate: 1000
    provider: "{{ bip }}"
  delegate_to: localhost


- name: Remove HTTP analytics profile
  bigip_profile_analytics:
    name: old_analytics
    state: absent
    provider: "{{ bip }}"
  delegate_to: localhost
```


## Tested Playbooks



