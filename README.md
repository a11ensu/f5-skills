# F5 Skills Repository

This repository contains skills and examples for managing and automating F5 BIG-IP devices.

## f5-bigip-ansiblev1

The `f5-bigip-ansiblev1` skill manages F5 BIG-IP devices using the F5 BIG-IP Modules Ansible Imperative collection (`f5networks.f5_modules`). It provides an environment and templates to configure virtual servers, pools, nodes, monitors, profiles, iRules, firewall rules, WAF/ASM policies, APM access profiles, GTM/DNS objects, device settings, VLANs, self-IPs, HA, and other BIG-IP objects via Ansible playbooks. All playbooks are executed locally and communicate with the BIG-IP via REST.


## f5-bigip-restapi

The `f5-bigip-restapi` skill manages F5 BIG-IP devices via REST API using `curl`. It covers three distinct API modes: iControl REST (imperative object-by-object), AS3 Application Services 3 (declarative JSON for app tenants), and Declarative Onboarding DO (device platform setup). This skill selects the correct API mode to configure components, deploy applications with AS3, onboard devices with DO, manage RPM packages, and query any BIG-IP REST API endpoint.
