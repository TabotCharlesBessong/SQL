-- explain analyze select id,g from grades where g > 80 and g < 95 order by g;

EXPLAIN ANALYZE SELECT g FROM grades WHERE id = 7;

-- CREATE INDEX id_idx ON grades(id);

-- DROP INDEX id_idx;

-- CREATE INDEX id_idx ON grades(id) include (name);