\d TABLE_NAME /* show table definition including indexes, constraints & triggers (psql)*/
\d+ TABLE_NAME /* More detailed table definition including description and physical disk size (psql) */
\dt /*List tables from current schema (psql) */
\dt *.* /* List tables from all schemas (psql)*/
\dt <name-of-schema>.* /* List the tables in a specific schema (psql) */
\copy (SELECT * FROM __table_name__) TO 'file_path_and_name.csv' WITH CSV /*Export a table as CSV (psql)*/


/*Show table indexes (SQL)*/
SELECT * FROM pg_indexes WHERE tablename='__table_name__' AND
schemaname='__schema_name__';

ANALYZE [__table__] /*Analyze a table and store the results in the pg_statistic system catalog (SQL)*/

/*Adding comment on table/column*/
Comment on table employee is 'Stores employee records'; 

Comment on column employee.ssn is 'Employee Social Security Number';

FULL CHEAT SHEET -> https://postgrescheatsheet.com/#/tables
