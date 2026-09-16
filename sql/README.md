# MariaDB / MySQL player database

`spirit_ptcgo.sql` creates the player database tables for MariaDB/MySQL.

Create an empty database, then import the file with a database account allowed
to create tables:

```sql
CREATE DATABASE spirit_ptcgo CHARACTER SET utf8mb4 COLLATE utf8mb4_bin;
```

```sh
mysql -u db_admin -p spirit_ptcgo < sql/spirit_ptcgo.sql
```

Set `DATABASE_URL` in `spirit/config.py` to your connection URL, for example:

```python
DATABASE_URL = "mysql+pymysql://spirit_user:password@db-host/spirit_ptcgo?charset=utf8mb4"
```
