# Creating a mySQL monitor in a declaration

## Description

This AS3 declaration creates a MySQL health monitor that connects to a MySQL server using credentials and optional database name. The monitor is associated with a pool of MySQL back-end servers.

## Examples

- Explanation of the example:

  - Partition (tenant) named "Sample_mysql_01";
  - Folder of the Partition is named "A1";
    - A MySQL monitor named "mysql_monitor" with:
      - Username and password;
      - Optional database name (database);
    - A pool named "mysql_pool" that uses "mysql_monitor";
      - The pool contains two MySQL servers on TCP port 3306.

```json
{
  "class": "AS3",
  "action": "deploy",
  "persist": true,
  "declaration": {
    "class": "ADC",
    "schemaVersion": "3.0.0",
    "id": "mysql-monitor-example",
    "label": "Creating a mySQL monitor in a declaration",
    "remark": "MySQL monitor example",
    "Sample_mysql_01": {
      "class": "Tenant",
      "A1": {
        "class": "Application",
        "template": "generic",
        "mysql_monitor": {
          "class": "Monitor",
          "monitorType": "mysql",
          "interval": 5,
          "timeout": 16,
          "username": "dbuser",
          "password": "dbpass",
          "database": "testdb"
        },
        "mysql_pool": {
          "class": "Pool",
          "monitors": [
            {
              "use": "mysql_monitor"
            }
          ],
          "members": [
            {
              "servicePort": 3306,
              "serverAddresses": [
                "192.0.2.70",
                "192.0.2.71"
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

