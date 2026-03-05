# Examples – iApp Package Management

> **Prerequisite:** Run `eval $(python scripts/setup_env.py <hostname>)` before every
> session to set `BIGIP_DEVICE` and `BIGIP_TOKEN`.
>
> **RPM version:** If not specified by the user, always use the **latest** release.
> Follow the *RPM Package Resolution Rule* below to locate, download, verify, and
> install the correct RPM before issuing any management requests.

**Set the downloads directory variable first — used in every command below:**

```bash
# Set to the project-root-relative Downloads path (run from project root)
DOWNLOADS_DIR="workspace/Downloads"
```

---

## RPM Package Resolution Rule

> **Rule:** When the user does not specify an RPM version, the Agent **must** always
> use the **latest release** available. Follow these steps in order:
>
> 1. **Check `$DOWNLOADS_DIR`** — if a matching RPM exists, pick the highest version.
> 2. **Download if missing** — if no matching RPM is found, download the latest release
>    from GitHub **together with its `.sha256` checksum file**.
> 3. **Verify integrity** — verify the sha256 checksum before uploading to the device;
>    abort if the hashes do not match.

---

### Step 1 – Check the `Downloads/` folder

```bash
# Resolve latest locally available RPM (empty output = not present)
ls "$DOWNLOADS_DIR" | grep "^f5-appsvcs" | sort -V | tail -1
ls "$DOWNLOADS_DIR" | grep "^f5-declarative-onboarding" | sort -V | tail -1
```

Use the resulting filename as `packageFilePath` on the device:
`/var/config/rest/downloads/<filename>`

---

### Step 2 – Download from GitHub (if not found locally)

Release pages:
- **AS3:** <https://github.com/F5Networks/f5-appsvcs-extension/releases>
- **DO:**  <https://github.com/F5Networks/f5-declarative-onboarding/releases>

Always download the RPM **and** its `.sha256` checksum file together:

```bash
# AS3 example – download RPM and checksum together
wget -P "$DOWNLOADS_DIR" \
  https://github.com/F5Networks/f5-appsvcs-extension/releases/download/v<VERSION>/f5-appsvcs-<VERSION>-<BUILD>.noarch.rpm
wget -P "$DOWNLOADS_DIR" \
  https://github.com/F5Networks/f5-appsvcs-extension/releases/download/v<VERSION>/f5-appsvcs-<VERSION>-<BUILD>.noarch.rpm.sha256

# DO example – download RPM and checksum together
wget -P "$DOWNLOADS_DIR" \
  https://github.com/F5Networks/f5-declarative-onboarding/releases/download/v<VERSION>/f5-declarative-onboarding-<VERSION>-<BUILD>.noarch.rpm
wget -P "$DOWNLOADS_DIR" \
  https://github.com/F5Networks/f5-declarative-onboarding/releases/download/v<VERSION>/f5-declarative-onboarding-<VERSION>-<BUILD>.noarch.rpm.sha256
```

> **Tip:** Check the GitHub releases page to obtain the exact tag and filename for the
> latest version before constructing the URL.

---

### Step 3 – Verify RPM integrity

**Always verify the checksum before uploading to the device.**
If the hashes do not match, discard the RPM and re-download.

```bash
# Verify against the downloaded .sha256 file
sha256sum -c "$DOWNLOADS_DIR/<filename>.noarch.rpm.sha256"
```

---

## List installed packages

```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/iapp/global-installed-packages | jq .
```

---

## Query package management tasks

Check the status of a previously submitted install/uninstall task.

```bash
# List all tasks
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/iapp/package-management-tasks | jq .

# Get status of a specific task (replace <task-id>)
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/iapp/package-management-tasks/<task-id> | jq .
```

---

## Upload RPM to BIG-IP

> **IMPORTANT:** The BIG-IP REST API requires the `Content-Range` header when uploading
> files. Without this header, the upload will fail with a 400 error:
> `"Missing 'Content-Range' header"`.

```bash
# Set the RPM filename
RPM_FILE="<rpm-filename>"

# Get file size and calculate Content-Range header
FILE_SIZE=$(stat -c%s "$DOWNLOADS_DIR/$RPM_FILE")

# Upload with Content-Range header (required)
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/octet-stream" \
     -H "Content-Range: 0-$((FILE_SIZE-1))/$FILE_SIZE" \
     -X POST \
     --data-binary @"$DOWNLOADS_DIR/$RPM_FILE" \
     "https://$BIGIP_DEVICE/mgmt/shared/file-transfer/uploads/$RPM_FILE" | jq .
```

---

## Install AS3 (Application Services 3)

Resolve the latest RPM first, verify integrity, upload to device, then install:

```bash
# Step 1 – resolve latest RPM filename
AS3_RPM=$(ls "$DOWNLOADS_DIR" | grep "^f5-appsvcs" | sort -V | tail -1)
echo "Installing: $AS3_RPM"

# Step 2 – verify RPM integrity before uploading
sha256sum -c "$DOWNLOADS_DIR/${AS3_RPM}.sha256"

# Step 3 – upload RPM to device (Content-Range header required)
FILE_SIZE=$(stat -c%s "$DOWNLOADS_DIR/$AS3_RPM")
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/octet-stream" \
     -H "Content-Range: 0-$((FILE_SIZE-1))/$FILE_SIZE" \
     -X POST \
     --data-binary @"$DOWNLOADS_DIR/$AS3_RPM" \
     "https://$BIGIP_DEVICE/mgmt/shared/file-transfer/uploads/$AS3_RPM" | jq .

# Step 4 – install on device
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d "{\"operation\":\"INSTALL\",\"packageFilePath\":\"/var/config/rest/downloads/$AS3_RPM\"}" \
     https://$BIGIP_DEVICE/mgmt/shared/iapp/package-management-tasks | jq .
```

---

## Install Declarative Onboarding (DO)

```bash
# Step 1 – resolve latest RPM filename
DO_RPM=$(ls "$DOWNLOADS_DIR" | grep "^f5-declarative-onboarding" | sort -V | tail -1)
echo "Installing: $DO_RPM"

# Step 2 – verify RPM integrity before uploading
sha256sum -c "$DOWNLOADS_DIR/${DO_RPM}.sha256"

# Step 3 – upload RPM to device (Content-Range header required)
FILE_SIZE=$(stat -c%s "$DOWNLOADS_DIR/$DO_RPM")
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/octet-stream" \
     -H "Content-Range: 0-$((FILE_SIZE-1))/$FILE_SIZE" \
     -X POST \
     --data-binary @"$DOWNLOADS_DIR/$DO_RPM" \
     "https://$BIGIP_DEVICE/mgmt/shared/file-transfer/uploads/$DO_RPM" | jq .

# Step 4 – install on device
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d "{\"operation\":\"INSTALL\",\"packageFilePath\":\"/var/config/rest/downloads/$DO_RPM\"}" \
     https://$BIGIP_DEVICE/mgmt/shared/iapp/package-management-tasks | jq .
```

---

## Uninstall a package

```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{"operation":"UNINSTALL","packageName":"<package-name>"}' \
     https://$BIGIP_DEVICE/mgmt/shared/iapp/package-management-tasks | jq .
```
