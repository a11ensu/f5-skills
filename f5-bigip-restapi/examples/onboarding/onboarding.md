# Examples – Declarative Onboarding (DO)

> **Prerequisite:** Run `eval $(python scripts/setup_env.py <hostname>)` before every
> session to set `BIGIP_DEVICE` and `BIGIP_TOKEN`.

---

## GET – Retrieve current onboarding configuration

```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/declarative-onboarding/config | jq .
```

---

## GET – Check onboarding task status

```bash
# List all DO tasks
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/declarative-onboarding/task | jq .

# Get status of a specific task (replace <task-id>)
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X GET \
     https://$BIGIP_DEVICE/mgmt/shared/declarative-onboarding/task/<task-id> | jq .
```

---

## POST – Push onboarding declaration from a JSON file

```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     --data-binary @onboarding.json \
     https://$BIGIP_DEVICE/mgmt/shared/declarative-onboarding/config | jq .
```

---

## POST – Push onboarding declaration inline

```bash
curl -sk \
     -H "X-F5-Auth-Token: $BIGIP_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
       "schemaVersion": "1.0.0",
       "class": "Device",
       "async": true,
       "label": "my-declaration"
     }' \
     https://$BIGIP_DEVICE/mgmt/shared/declarative-onboarding/config | jq .
```
