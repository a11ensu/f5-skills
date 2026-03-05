# Creating a PostgreSQL monitor in a declaration

## Description

This AS3 declaration sets up a PostgreSQL health monitor that connects to a PostgreSQL database using credentials and an optional database name. The monitor is attached to a pool of PostgreSQL servers.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_postgres_01";
  - Folder of the Partition is named "A1";
    - A PostgreSQL monitor named "postgres_monitor" with:
      - Username and password;
      - Optional database name (database);
    - A pool named "postgres_pool" that uses "postgres_monitor";
      - The pool includes two PostgreSQL servers on TCP port 5432.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "postgres-monitor-example",
    "label": "Creating a PostgreSQL monitor in a declaration",
    "remark": "PostgreSQL monitor example",
    "Sample_postgres_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "postgres_monitor": {
          "class": "Monitor",
          "monitorType": "postgresql",
          "interval": 5,
          "timeout": 16,
          "username": "pguser",
          "password": "pgpass",
          "database": "testdb"
        },
        "postgres_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "postgres_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 5432,
              "serverAddresses": [
                "192.0.2.90",
                "192.0.2.91"
              ]
            }
          ]
        }
      }
    }
  }
}
```

## Tested json templates

---

