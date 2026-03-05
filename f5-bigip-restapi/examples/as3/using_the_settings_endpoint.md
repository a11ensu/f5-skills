# Using the /settings endpoint

## Description

This example configures global AS3 settings via the `/settings` endpoint, such as enabling or disabling `dryRun` or changing default behavior. The JSON is a `Settings` class, not an ADC declaration.

## Examples

- Explanation of the example:
  - Top-level `class: "Settings"`;
  - `id` and `schemaVersion` defined;
  - `dryRun` set to `true`;
  - Affects how subsequent AS3 declarations are processed.

```json
{
  "class": "Settings",
  "schemaVersion": "1.0.0",
  "id": "global-settings",
  "dryRun": true
}
```

## Tested json templates

---

