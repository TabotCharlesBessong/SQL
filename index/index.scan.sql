-- EXPLAIN SELECT name FROM grades WHERE id > 100;

-- bitmap scan

-- EXPLAIN select name from grades where g > 95 AND id < 10000 ;

-- CREATE INDEX concurrently g ON grades(g);

-- CREATE INDEX g ON grades(g);

-- INSERT INTO grades (g) VALUES (1);

-- DROP INDEX g;

-- SELECT count(*) from grades;

-- SELECT * FROM grades;