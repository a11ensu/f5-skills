# f5-bigip-restapi

Manages F5 BIG-IP devices via REST API using `curl`. Covers three distinct API modes: iControl REST (imperative object-by-object), AS3 Application Services 3 (declarative JSON for app tenants), and Declarative Onboarding DO (device platform setup). Includes 170 AS3 declaration examples, onboarding guides, and Python helper scripts for authentication.

| Field | Value |
|-------|-------|
| **Version** | 2.0.0 |
| **Last Updated** | 2026-03-05 |

## What's Updated (v2.0.0 -- 2026-03-05)

- Initial release with 170 AS3 declaration examples, onboarding guide, package management docs, Python auth scripts, and AS3 index.

## What's Included

- **SKILL.md** -- Agent entry point with API mode selection guide, curl command templates, AS3 authoring instructions, workflow, and troubleshooting.
- **examples/as3/** -- 170 AS3 declaration example files covering virtual services, TLS/SSL, HTTP/2, GSLB/DNS, security (AFM/DoS/firewall), ASM/APM/WAF, SNAT/NAT, transport protocols, monitors, analytics, and more.
- **examples/onboarding/** -- Declarative Onboarding (DO) guide for initial device setup (hostname, license, NTP, DNS, HA, VLANs, self-IPs).
- **examples/package-management.md** -- RPM upload, install, upgrade, and uninstall procedures for AS3 and DO packages.
- **references/** -- Categorised index of all AS3 examples (`as3-index.md`).
- **scripts/** -- Python helper scripts (`setup_env.py`, `get_device.py`) for device credential resolution and auth token management.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-03-05 | Initial release -- 170 AS3 examples, onboarding guide, package management docs, Python auth scripts, AS3 index |
