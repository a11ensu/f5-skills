#!/usr/bin/env python3
"""
setup_env.py — Authenticate to a F5 BIG-IP and export shell variables.

Usage:
    eval $(python .claude/skills/f5-bigip-restapi/scripts/setup_env.py <hostname>)

No conda/base environment requirement.

Exports:
    BIGIP_DEVICE   — Management IP of the BIG-IP
    BIGIP_TOKEN    — iControl REST auth token

Token-based curl usage:
    curl -sk -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
         -H "Content-Type: application/json" \
         -X GET https://$BIGIP_DEVICE/mgmt/tm/ltm/virtual | jq .

Credential resolution order:
    1. get_device(hostname)         — queries postgres via my_utils (get_device.py);
                                      returns None if my_utils unavailable or host not found
    2. get_device_default(hostname) — reads from scripts/.config.yaml (cbip section)
"""

import json
import ssl
import sys
import urllib.request

from get_device import get_available_hosts, get_device, get_device_default


# ---------------------------------------------------------------------------
# Token generation
# ---------------------------------------------------------------------------
def get_token(device_ip: str, username: str, password: str) -> str:
    """
    POST to /mgmt/shared/authn/login and return the auth token string.
    TLS certificate verification is disabled (BIG-IP uses self-signed certs).
    """
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    payload = json.dumps({
        "username": username,
        "password": password,
        "loginProviderName": "tmos",
    }).encode()

    req = urllib.request.Request(
        f"https://{device_ip}/mgmt/shared/authn/login",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        print(f"ERROR: Token request failed ({exc.code}): {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as exc:
        print(f"ERROR: Cannot reach {device_ip}: {exc.reason}", file=sys.stderr)
        sys.exit(1)

    try:
        return data["token"]["token"]
    except (KeyError, TypeError):
        print(
            f"ERROR: Unexpected auth response:\n{json.dumps(data, indent=2)}",
            file=sys.stderr,
        )
        sys.exit(1)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: eval $(python setup_env.py <hostname>)", file=sys.stderr)
        print(f"       Available hosts: {get_available_hosts()}", file=sys.stderr)
        sys.exit(1)

    hostname = sys.argv[1]

    # Step 1 — try custom plug-in first
    device = get_device(hostname)

    # Step 2 — explicit fallback message + config lookup
    if device is None:
        print(
            f"INFO: get_device('{hostname}') returned None; using get_device_default() from .config.yaml",
            file=sys.stderr,
        )
        device = get_device_default(hostname)
    else:
        print(f"INFO: get_device('{hostname}') returned {device.management_ip}", file=sys.stderr)

    # Step 3 — obtain a token
    token = get_token(device.management_ip, device.username, device.password)

    # Step 4 — emit export statements for eval in the caller's shell
    print(f"export BIGIP_DEVICE={device.management_ip}")
    print(f"export BIGIP_TOKEN={token}")
