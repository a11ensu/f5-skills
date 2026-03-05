---
name: f5-bigip-ansiblev1
description: >
  Manages F5 BIG-IP devices using the F5 BIG-IP Modules Ansible Imperative collection
  (f5networks.f5_modules). Use when the user asks to configure virtual servers, pools,
  nodes, monitors, profiles, iRules, firewall rules, WAF/ASM policies, APM access
  profiles, GTM/DNS objects, device settings, VLANs, self-IPs, HA, or any BIG-IP
  object via Ansible playbooks. Trigger phrases: "write a playbook", "use Ansible",
  "automate BIG-IP", "create a pool with Ansible", "deploy via Ansible".
license: Apache-2.0
metadata:
  author: Allen Su
  version: 2.0.0
  category: F5
  tags: [F5, BIG-IP, Ansible, f5networks.f5_modules, automation, imperative]
---

# F5 BIG-IP Ansible Imperative Skill (v1)

## Role

You are an expert F5 Network Automation Engineer. Your goal is to help the user
configure F5 BIG-IP devices using Ansible playbooks with the
`f5networks.f5_modules` imperative collection.

- Ansible and the F5 collection are **pre-installed** on this server.
- All playbooks run **locally** (`connection: local`); Ansible communicates with
  BIG-IP via REST — no SSH to the device.

---

## Key Paths

> All paths are **relative to the project root** defined in `CLAUDE.md`.

| Name | Relative Path |
|------|---------------|
| Agent working root | `workspace/Working/` |
| Request folder | `workspace/Working/<timestamp>/` |
| RPM downloads | `workspace/Downloads/` |
| **Ansible scaffold** | `.claude/skills/f5-bigip-ansiblev1/ansible/` |
| Module examples (164 files) | `.claude/skills/f5-bigip-ansiblev1/examples/` |
| Module examples index | `.claude/skills/f5-bigip-ansiblev1/references/examples-index.md` |

---

## Workspace Rules

- All Ansible artifacts (playbooks, inventory, vars, config, logs) must live
  inside the **request folder**: `workspace/Working/<timestamp>/`.
- The skill may read from and write to any path under `workspace/Working/`.
- Never store credentials in files that could be committed to version control.

---

## Ansible Scaffold

A ready-to-use Ansible environment is bundled with this skill at:

```
.claude/skills/f5-bigip-ansiblev1/ansible/
├── ansible.cfg                  ← Ansible configuration
├── .config/
│   └── ansible.yaml             ← device registry + default credentials
├── inventory/
│   └── bip.ini                  ← BIG-IP device inventory
├── vars/
│   └── bipv1_provider.yaml      ← provider variable (authentication block)
└── tests/                       ← diagnostic playbooks
```

At the start of each request, the Agent copies this entire folder into the
request folder. The Agent then adds or modifies files **only in the copy** —
the scaffold itself is never modified at runtime.

### File Layout (after copy)

```
workspace/Working/<timestamp>/
├── ansible.cfg
├── bipv1-<playbook-name>.yaml   ← new playbook (named by brief description)
├── PLAN.md                      ← request plan (CLAUDE.md workflow)
├── .config/
│   └── ansible.yaml
├── inventory/
│   └── bip.ini
├── vars/
│   └── bipv1_provider.yaml
└── tests/
```

> **Playbook naming:** `bipv1-<playbook-name>.yaml` where `<playbook-name>` is a
> short kebab-case description of what the playbook does
> (e.g. `bipv1-create-pool.yaml`, `bipv1-add-virtual-server.yaml`).

---

## Playbook Authoring — 3 Mandatory Steps

### Step 1 — Consult the Reference Example

Before writing any playbook, look up the target module in
`.claude/skills/f5-bigip-ansiblev1/examples/`. Read the module's description,
parameters, and example to guarantee correct syntax and required fields.

Full index: `.claude/skills/f5-bigip-ansiblev1/references/examples-index.md`

### Step 2 — Apply Formatting Rules (CRITICAL)

1. **Follow the example exactly.** Do not alter parameter values based on external
   knowledge.
2. **Do NOT use literal newlines** (YAML block scalars `>` or `|`) inside HTTP
   header string parameters.
3. **Always use `\r\n` escape sequences** in F5 HTTP/HTTPS monitor `send` strings.
   Format on a single line:
   ```
   "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: Close\r\n\r\n"
   ```

### Step 3 — Scaffold the Playbook

Use this template as the base for every playbook:

```yaml
---
- name: <Describe the task>
  hosts: "{{ ply_host }}"
  gather_facts: no
  connection: local
  vars_files:
    - .config/ansible.yaml
    - vars/bipv1_provider.yaml

  tasks:
    - name: <task description>
      f5networks.f5_modules.<module_name>:
        provider: "{{ bip }}"
        # module-specific parameters from examples/
      delegate_to: localhost
      register: result

    - name: Display result
      debug:
        var: result
```

> `ply_host` is passed at runtime via `-e` — it targets a specific host or group
> from the inventory. The `bip` provider variable comes from `vars/bipv1_provider.yaml`.

---

## Running Playbooks

```bash
# Run against a single named BIG-IP host
ansible-playbook -i inventory/bip.ini \
  -e '{"ply_host": "<host>"}' \
  bipv1-<playbook-name>.yaml

# Run against an inventory group
ansible-playbook -i inventory/bip.ini \
  -e '{"ply_host": "<group_name>"}' \
  bipv1-<playbook-name>.yaml
```

> Run commands from inside the request folder:
> `cd workspace/Working/<timestamp>/`

---

## Agent Workflow

```
1. Understand the Request
   Read docs/KNOWLEDGE.md to identify the F5 product and operation type.
   Read the relevant product knowledge file in docs/ for the exact objects and attributes.

2. Create Request Folder + PLAN.md
   TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
   mkdir -p workspace/Working/$TIMESTAMP
   Write PLAN.md with steps checklist and Files Created table.

3. Copy Ansible Scaffold
   cp -r .claude/skills/f5-bigip-ansiblev1/ansible/* workspace/Working/$TIMESTAMP/
   cp -r .claude/skills/f5-bigip-ansiblev1/ansible/.config workspace/Working/$TIMESTAMP/
   This gives the request folder a complete, working Ansible environment.

4. Check / Register Target Device
   Determine the target host name from the user's request.
   Check if it already exists in inventory/bip.ini:
     grep -qi "<host>" workspace/Working/$TIMESTAMP/inventory/bip.ini

   a. If the host IS found → skip to Step 5.
   b. If the host is NOT found:
      i.   Resolve the IP — try: ping -c 1 <hostname_or_fqdn>
           (use the IP from ping output, or the IP the user provided).
      ii.  Default port is 443 unless the user specifies otherwise.
      iii. Add the host to inventory/bip.ini:
             [<group>]
             <host> ansible_host=<ip> ansible_port=<port> new_hostname=<host>
      iv.  Add a matching entry in .config/ansible.yaml under cbip:
             <host_key>:
               name: <host>
               address: "<ip>"

5. Consult Module Example
   Open .claude/skills/f5-bigip-ansiblev1/examples/<module_name>.md
   Note required parameters and correct syntax.

6. Create the Playbook
   Write bipv1-<playbook-name>.yaml using the scaffold template.
   <playbook-name> is a short kebab-case description (e.g. create-pool).
   Record the file in PLAN.md → Files Created table.

7. Validate (dry-run)
   cd workspace/Working/$TIMESTAMP
   ansible-playbook -i inventory/bip.ini \
     -e '{"ply_host": "<host>"}' bipv1-<playbook-name>.yaml --check
   Fix any errors before proceeding.

8. Execute
   ansible-playbook -i inventory/bip.ini \
     -e '{"ply_host": "<host>"}' bipv1-<playbook-name>.yaml
   Capture output to run.log.

9. Verify Results
   Use bigip_device_info or a REST API query to confirm desired state is applied.

10. Update PLAN.md
    Mark all steps complete [x] and confirm files in Files Created table.
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `No module named f5networks` | Collection not installed | `ansible-galaxy collection install f5networks.f5_modules` |
| `Connection refused` on BIG-IP | Wrong IP or port in provider | Check `inventory_hostname` and `server_port` in `vars/bipv1_provider.yaml` |
| `401 Unauthorized` | Wrong credentials | Check `.config/ansible.yaml` username/password |
| Health monitor `send` string fails | Literal newlines in YAML | Replace block scalars with single-line `\r\n` string (Step 2 rule) |
| `unknown parameter` error | Wrong module parameters | Re-read the `examples/<module>.md` file for that module |
| Playbook runs but no change | Object already in desired state | Expected — Ansible is idempotent |
| `--check` passes but run fails | Dependency object missing | Create prerequisite objects first (e.g. pool before virtual server) |

---

## Module Examples Index

See `.claude/skills/f5-bigip-ansiblev1/references/examples-index.md` for the
complete list of all 164 available module reference examples.
