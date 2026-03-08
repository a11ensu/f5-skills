# F5 Skills Repository

This repository contains skills and examples for managing and automating F5 BIG-IP devices.

## Skills Summary

| Skill | Version | Last Updated | Description |
|-------|---------|--------------|-------------|
| [f5-bigip-ansiblev1](f5-bigip-ansiblev1/) | 2.0.0 | 2026-03-05 | Ansible automation for BIG-IP (imperative collection) |
| [f5-bigip-restapi](f5-bigip-restapi/) | 2.0.0 | 2026-03-05 | REST API automation for BIG-IP (curl, AS3, DO) |
| [f5-cis-k8s](f5-cis-k8s/) | 3.0.0 | 2026-03-07 | F5 Container Ingress Services on Kubernetes |

---

## f5-bigip-ansiblev1 (v2.0.0)

Manages F5 BIG-IP devices using the F5 BIG-IP Modules Ansible Imperative collection (`f5networks.f5_modules`). Provides an environment and templates to configure virtual servers, pools, nodes, monitors, profiles, iRules, firewall rules, WAF/ASM policies, APM access profiles, GTM/DNS objects, device settings, VLANs, self-IPs, HA, and other BIG-IP objects via Ansible playbooks. All playbooks are executed locally and communicate with the BIG-IP via REST.

**What's Updated (v2.0.0 -- 2026-03-05):** Initial release with Ansible scaffold, 164 module reference files, examples index, device registry, and diagnostic playbooks.

## f5-bigip-restapi (v2.0.0)

Manages F5 BIG-IP devices via REST API using `curl`. Covers three distinct API modes: iControl REST (imperative object-by-object), AS3 Application Services 3 (declarative JSON for app tenants), and Declarative Onboarding DO (device platform setup). This skill selects the correct API mode to configure components, deploy applications with AS3, onboard devices with DO, manage RPM packages, and query any BIG-IP REST API endpoint.

**What's Updated (v2.0.0 -- 2026-03-05):** Initial release with 170 AS3 declaration examples, onboarding guide, package management docs, Python auth scripts, and AS3 index.

## f5-cis-k8s (v3.0.0)

Installs and operates F5 BIG-IP Container Ingress Services (CIS) on Kubernetes clusters. Provides templates, CRD examples, and reference documents for deploying CIS, creating VirtualServer/TransportServer/ExternalDNS custom resources, exposing Kubernetes services through BIG-IP, and troubleshooting CIS.

**What's Updated (v3.0.0 -- 2026-03-07):** Added NodePort templates, BIG-IP Node template, Calico Tigera operator docs, ArgoCD TransportServer, worked example in install-steps, F5 Helm chart reference, and expanded CRD field docs.
