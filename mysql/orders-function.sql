-- SELECT * FROM sql_store.orders;
SELECT * FROM sql_store.orders WHERE shipper_id IS NULL ORDER BY customer_id asc LIMIT 3;