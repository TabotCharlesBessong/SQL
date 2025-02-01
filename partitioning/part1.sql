-- CREATE TABLE IF NOT EXISTS grades_org (id serial NOT NULL, g int NOT NULL);

-- CREATE TABLE IF NOT EXISTS grades_parts (id serial NOT NULL, g int NOT NULL) PARTITION BY RANGE(g);

-- CREATE TABLE g70100 (LIKE grades_parts including indexes);

-- ALTER TABLE grades_parts ATTACH PARTITION g0035 for VALUES FROM (0) to (35); 
-- ALTER TABLE grades_parts ATTACH PARTITION g3570 for VALUES FROM (35) to (70); 
-- ALTER TABLE grades_parts ATTACH PARTITION g70100 for VALUES FROM (70) to (100); 

-- INSERT INTO grades_org(g) SELECT floor(random() * 101) FROM generate_series(0,10000000);

-- INSERT INTO grades_parts SELECT * FROM grades_org;

-- SELECT * FROM grades_org;

-- DROP TABLE grades_org;

-- CREATE INDEX grades_org_index on grades_org(g);

-- \d grades_org;

-- EXPLAIN ANALYZE SELECT count(*) FROM grades_org WHERE g = 30;