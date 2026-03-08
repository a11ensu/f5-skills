# f5-bigip-ansiblev1

Manages F5 BIG-IP devices using the F5 BIG-IP Modules Ansible Imperative collection (`f5networks.f5_modules`). Provides an environment, scaffold, and 164 module reference files to configure virtual servers, pools, nodes, monitors, profiles, iRules, firewall rules, WAF/ASM policies, APM access profiles, GTM/DNS objects, device settings, VLANs, self-IPs, HA, and other BIG-IP objects via Ansible playbooks.

| Field | Value |
|-------|-------|
| **Version** | 2.0.0 |
| **Last Updated** | 2026-03-05 |

## What's Updated (v2.0.0 -- 2026-03-05)

- Initial release with Ansible scaffold, 164 module reference files, examples index, device registry, and diagnostic playbooks.

## What's Included

- **SKILL.md** -- Agent entry point with role definition, playbook authoring guide, workflow, and troubleshooting.
- **ansible/** -- Ready-to-use Ansible scaffold (ansible.cfg, inventory, provider vars, device registry, diagnostic playbooks).
- **examples/** -- 164 module reference files (one per `bigip_*` module) covering parameters, return values, and usage examples.
- **references/** -- Categorised index of all example modules (`examples-index.md`).

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-03-05 | Initial release -- Ansible scaffold, 164 module reference files, examples index, device registry, diagnostic playbooks |
