"""
get_device.py — Device credential resolver for setup_env.py.

my_utils is importable without conda because PYTHONPATH includes the workspace
root (e.g. export PYTHONPATH="$PYTHONPATH:/home/allen/working" in .bashrc).

Resolution model (called in order by setup_env.py):
  1. get_device(hostname)         → queries the postgres backend via my_utils.
                                    Returns None if my_utils is not importable
                                    or the hostname is not found in the DB.
  2. get_device_default(hostname) → reads credentials from .config.yaml in
                                    this directory. Used when get_device()
                                    returns None.

To integrate a different credential source (Vault, CMDB, etc.), replace the
body of get_device() with your own logic and return a DeviceInfo namedtuple.
"""

import pathlib
import sys
from typing import NamedTuple, Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


class DeviceInfo(NamedTuple):
    management_ip: str
    username: str
    password: str


_CONFIG_FILE = pathlib.Path(__file__).parent / ".config.yaml"


# ---------------------------------------------------------------------------
# Config helpers (used by get_device_default)
# ---------------------------------------------------------------------------

def load_config() -> dict:
    if not _CONFIG_FILE.exists():
        print(f"ERROR: Config file not found: {_CONFIG_FILE}", file=sys.stderr)
        sys.exit(1)
    with _CONFIG_FILE.open() as fh:
        return yaml.safe_load(fh)


def get_available_hosts() -> str:
    return ", ".join(load_config().get("cbip", {}).keys())


# ---------------------------------------------------------------------------
# Primary resolver — postgres backend (my_utils)
# ---------------------------------------------------------------------------

def get_device(hostname: str) -> Optional[DeviceInfo]:
    """
    Look up *hostname* in the postgres devices database via my_utils.

    Returns a DeviceInfo on success, or None if:
      - my_utils is not importable (PYTHONPATH not set correctly), or
      - the hostname is not found in the database.

    setup_env.py will fall back to get_device_default() when None is returned.
    """
    try:
        from my_utils.postgres import postgres
        from my_utils.device import load_devices
    except ImportError:
        return None

    db = postgres(table="devices")
    try:
        rows = db.list_devices(hostname=hostname)
        devices = load_devices(rows, decode_credentials=True)
        if not devices:
            return None
        dev = next(iter(devices.values()))
        return DeviceInfo(
            management_ip=dev.management_ip,
            username=dev.username,
            password=dev.password,
        )
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Fallback resolver — .config.yaml
# ---------------------------------------------------------------------------

def get_device_default(hostname: str) -> DeviceInfo:
    """
    Look up *hostname* in the cbip section of .config.yaml.
    Per-device username/password override default_auth when present.
    """
    cfg = load_config()
    devices = cfg.get("cbip", {})
    defaults = cfg.get("default_auth", {})

    if hostname not in devices:
        print(f"ERROR: '{hostname}' not found in {_CONFIG_FILE.name}.", file=sys.stderr)
        print(f"       Available: {', '.join(devices.keys())}", file=sys.stderr)
        sys.exit(1)

    dev = devices[hostname]
    return DeviceInfo(
        management_ip=dev["address"],
        username=dev.get("username", defaults.get("username", "admin")),
        password=dev.get("password", defaults.get("password", "admin")),
    )
