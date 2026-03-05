---
name: f5-bigip-restapi
description: >
  Manages F5 BIG-IP devices via REST API using curl. Covers three distinct API
  modes: iControl REST (imperative object-by-object), AS3 Application Services 3
  (declarative JSON for app tenants), and Declarative Onboarding DO (device
  platform setup). Use when user asks to configure virtual servers, pools, nodes,
  profiles, iRules, WAF, firewall rules, GSLB, deploy an application with AS3,
  onboard a device with DO, install or upgrade AS3/DO RPM packages, or query any
  BIG-IP REST API endpoint. Trigger phrases: "use curl", "REST API", "send a
  declaration", "AS3", "Declarative Onboarding", "DO", "check BIG-IP via API",
  "install RPM", "deploy with AS3".
license: Apache-2.0
metadata:
  author: Allen Su
  version: 2.0.0
  category: F5
  tags: [F5, BIG-IP, REST, curl, AS3, DO, iControl, automation]
---

# F5 BIG-IP REST API Skill

## Role

You are an expert F5 Network Automation Engineer. You interact with F5 BIG-IP
devices using the REST API and `curl`. You select the correct API mode for each
request, write correct JSON payloads by consulting example files, and verify
results after each operation.

---

## Key Paths

> All paths are **relative to the project root** defined in `CLAUDE.md`.

| Name | Relative Path |
|------|---------------|
| RPM downloads | `workspace/Downloads/` |
| Agent working root | `workspace/Working/` |
| Request folder | `workspace/Working/<timestamp>/` |
| Scripts | `.claude/skills/f5-bigip-restapi/scripts/` |
| AS3 examples (170 files) | `.claude/skills/f5-bigip-restapi/examples/as3/` |
| AS3 examples index | `.claude/skills/f5-bigip-restapi/references/as3-index.md` |
| Onboarding examples | `.claude/skills/f5-bigip-restapi/examples/onboarding/` |
| Package management examples | `.claude/skills/f5-bigip-restapi/examples/package-management.md` |

---

## Workspace Rules

- All files created by this skill (JSON payloads, curl scripts, response logs)
  must be placed in the **request folder**: `workspace/Working/<timestamp>/`.
- RPM packages must be downloaded to `workspace/Downloads/` — never elsewhere.
- Save every JSON declaration sent to the device as a `.json` file in the request
  folder for traceability.

---

## API Modes — Choose Before Acting

BIG-IP exposes three distinct REST API styles. **Choose the correct one first.**

| Mode | When to use | Endpoint base | Examples |
|------|-------------|---------------|---------|
| **iControl REST** | Surgical, object-level changes; read state; anything not covered by AS3/DO | `/mgmt/tm/` | `.claude/skills/f5-bigip-knowledge/` |
| **AS3** | Deploy or update complete application tenants (virtual servers, pools, WAF, profiles) | `/mgmt/shared/appsvcs/declare` | `examples/as3/` |
| **DO** | Initial device setup: hostname, license, NTP, DNS, HA, VLANs, self-IPs | `/mgmt/shared/declarative-onboarding` | `examples/onboarding/` |

> **Rule:** If the request is about an application (virtual server + pool + profiles),
> prefer AS3. If it is about device-level settings, prefer DO. For targeted single-object
> changes or reads, use iControl REST directly.

---

## Environment Setup

Before issuing any `curl` commands, run `setup_env.py` to populate credentials.

> No special Python environment required — stdlib + PyYAML only.
> Device list is read from `scripts/.config.yaml`.

```bash
# Run from the project root
eval $(python .claude/skills/f5-bigip-restapi/scripts/setup_env.py <hostname>)
```

This exports two variables used by every subsequent command:

| Variable | Description |
|----------|-------------|
| `BIGIP_DEVICE` | Management IP of the BIG-IP |
| `BIGIP_TOKEN` | iControl REST auth token |

**Credential resolution order inside `setup_env.py`:**
1. `get_device(hostname)` in `scripts/get_device.py` — custom plug-in (returns `None` by default)
2. `get_device_default(hostname)` — looks up `hostname` in `scripts/.config.yaml → cbip`; per-device `username`/`password` override `default_auth` when present
3. `get_token()` — POSTs to `/mgmt/shared/authn/login` and returns the token

List available hostnames (shown when no argument is given):
```bash
python .claude/skills/f5-bigip-restapi/scripts/setup_env.py
```

Verify after eval (optional):
```bash
echo "Device: $BIGIP_DEVICE"
echo "Token : ${BIGIP_TOKEN:0:10}…"
```

---

## Curl Command Templates

All templates use `BIGIP_TOKEN` for authentication via the `X-F5-Auth-Token`
header. Do **not** use `-u` (Basic Auth) — it is not needed and must not appear.

### iControl REST
```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X <GET|POST|PUT|PATCH|DELETE> \
     https://$BIGIP_DEVICE/mgmt/tm/<module>/<resource> | jq .
```

### AS3 — POST a declaration
```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     --data-binary @workspace/Working/<timestamp>/<declaration>.json \
     https://$BIGIP_DEVICE/mgmt/shared/appsvcs/declare | jq .
```

### DO — POST an onboarding declaration
```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     --data-binary @workspace/Working/<timestamp>/<onboarding>.json \
     https://$BIGIP_DEVICE/mgmt/shared/declarative-onboarding | jq .
```

### RPM upload (requires Content-Range; no JSON header)
```bash
FILE_SIZE=$(stat -c%s "$RPM_PATH")
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/octet-stream" \
     -H "Content-Range: 0-$((FILE_SIZE-1))/$FILE_SIZE" \
     -X POST \
     --data-binary @"$RPM_PATH" \
     "https://$BIGIP_DEVICE/mgmt/shared/file-transfer/uploads/$(basename $RPM_PATH)" | jq .
```

### Curl flag reference

| Flag | Purpose |
|------|---------|
| `-s` | Silent — suppress progress output |
| `-k` | Skip TLS certificate verification (self-signed certs) |
| `-H "X-F5-Auth-Token: $BIGIP_TOKEN"` | Token-based authentication |
| `-H "Content-Type: application/json"` | JSON request body |
| `-X` | HTTP method (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) |
| `--data-binary @file` | Send file body verbatim (preserves JSON formatting) |
| `\| jq .` | Pretty-print JSON response |

---

## AS3 — Authoring Instructions

### Step 1 — Consult an AS3 Example

Before writing any AS3 declaration:
1. Read `.claude/skills/f5-bigip-restapi/references/as3-index.md` to find the
   closest matching example for the request.
2. Open that example file from `examples/as3/` and study its structure,
   class names, and property values.

### Step 2 — AS3 Declaration Structure

Every AS3 declaration follows this skeleton:

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "<unique-id>",
    "<TenantName>": {
      "class": "Tenant",
      "<AppName>": {
        "class": "Application",
        "<ServiceName>": {
          "class": "Service_HTTP",
          "virtualAddresses": ["<vip-ip>"],
          "virtualPort": 80,
          "pool": "<PoolName>"
        },
        "<PoolName>": {
          "class": "Pool",
          "monitors": ["http"],
          "members": [{ "servicePort": 80, "serverAddresses": ["<server-ip>"] }]
        }
      }
    }
  }
}
```

**Key AS3 classes:**

| Class | Purpose |
|-------|---------|
| `Service_HTTP` | HTTP virtual server |
| `Service_HTTPS` | HTTPS virtual server (requires `serverTLS`) |
| `Service_TCP` / `Service_UDP` | TCP/UDP virtual server |
| `Service_Generic` | Generic protocol virtual server |
| `Pool` | Load-balancing pool with members |
| `Monitor_HTTP` / `Monitor_HTTPS` / `Monitor_TCP` | Health monitors |
| `TLS_Server` | Client-side SSL/TLS profile |
| `TLS_Client` | Server-side SSL/TLS re-encryption profile |
| `Certificate` | SSL certificate + key object |
| `Persist_Cookie` / `Persist_Source_Address` | Persistence profiles |
| `iRule` | iRule attached to a service |
| `Firewall_Policy` | AFM firewall policy |
| `WAF_Policy` | ASM/AWAF web application firewall policy |
| `GSLB_Pool` / `GSLB_Domain` | GTM/DNS GSLB objects |

### Step 3 — Check Task Status

AS3 operations are asynchronous. Always poll for completion:

```bash
# Check current AS3 task status
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/appsvcs/task | jq .

# Retrieve current declared state (all tenants)
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/appsvcs/declare | jq .
```

---

## Examples Index

### AS3 Examples (170 files)
Full categorised index: `.claude/skills/f5-bigip-restapi/references/as3-index.md`

Categories covered:
- Virtual Services & LTM · TLS/SSL · HTTP/2 · Profiles & Logging
- GSLB / DNS · Security – AFM/DoS/Firewall · Security – ASM/APM/WAF
- SNAT / NAT / Forwarding · Transport Protocols · Monitors
- Analytics · Data Sources & References · Declaration Controls · Network

### Onboarding Examples (DO)
See: `examples/onboarding/onboarding.md`

### Package Management Examples
See: `examples/package-management.md`
(RPM resolution, upload, AS3/DO install/upgrade/uninstall)

---

## Agent Workflow

```
1. Understand & Classify
   Read KNOWLEDGE.md. Identify: product module, operation type, API mode
   (iControl REST / AS3 / DO).

2. Create Request Folder + PLAN.md
   TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
   mkdir -p workspace/Working/$TIMESTAMP
   Write PLAN.md with steps checklist and Files Created table.

3. Environment Setup
   eval $(python .claude/skills/f5-bigip-restapi/scripts/setup_env.py <hostname>)

4. Query Current State
   GET relevant objects from the device to understand what already exists.
   Save the response to workspace/Working/$TIMESTAMP/current-state.json.

5. Check Extension Requirements (if using AS3 or DO)
   Verify AS3 / DO is installed at the required version:
     GET /mgmt/shared/iapp/installed-packages
   If not installed or outdated → follow the RPM Package Resolution Rule in
   examples/package-management.md to download, verify, and install.

6. Consult Examples
   For AS3: read references/as3-index.md and open the closest example file.
   For DO:  read examples/onboarding/onboarding.md.
   For iControl REST: read the knowledge base for the correct endpoint.

7. Write JSON Payload
   Save to workspace/Working/$TIMESTAMP/<declaration>.json.
   Record the file in PLAN.md → Files Created table.

8. Execute
   POST / PATCH / GET as required. Save response to run.log.

9. Verify
   Poll task status (AS3/DO) or GET the object (iControl REST) to confirm
   the desired state is applied. Report results to the user.

10. Save Config (iControl REST changes only)
    POST /mgmt/tm/sys/config  {"command":"save"}
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `401 Unauthorized` | Expired or missing token | Re-run `setup_env.py` to get a fresh token; default token lifetime is 1200 s |
| `404 Not Found` | Wrong endpoint path or object not in partition | Check URL; add `~Common~` encoding for `/Common/` |
| AS3 returns `422` | Schema validation error | Read the `errors` array in the response; check class names and required fields against the example |
| AS3/DO task stuck `in progress` | Long-running change | Poll `/task` endpoint; wait up to 5 min for provisioning tasks |
| `Missing 'Content-Range' header` | RPM upload without Content-Range | Use the upload template in `examples/package-management.md` |
| Object exists but wrong state | Prior declaration not cleaned up | GET current state; DELETE tenant (AS3) or PATCH specific object (iControl) |
| `iControl REST PATCH 400` | Attempting to PATCH read-only field | Use PUT to replace, or check field mutability in knowledge base |
