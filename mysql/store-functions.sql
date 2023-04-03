-- SELECT * FROM sql_store.customers;
-- SELECT * FROM sql_store.customers WHERE last_name REGEXP '^field'; -- start with field
-- regexp 'field$' the last name must end with field 
-- SELECT * FROM sql_store.customers WHERE last_name REGEXP '^field|mac|rose'; 
-- SELECT * FROM sql_store.customers WHERE first_name REGEXP 'elka|ambur';
-- SELECT * FROM sql_store.customers WHERE last_name REGEXP 'ey$|on$';
-- SELECT * FROM sql_store.customers WHERE last_name REGEXP '^my|se';
-- SELECT * FROM sql_store.customers WHERE last_name REGEXP 'b[ru]';
-- SELECT * FROM sql_store.customers WHERE phone IS NULL;
SELECT * FROM sql_store.customers ORDER BY points desc LIMIT 3;