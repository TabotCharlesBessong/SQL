-- create table students (
-- id serial primary key, 
--  g int,
--  firstname text, 
-- lastname text, 
-- middlename text,
-- address text,
--  bio text,
-- dob date,
-- id1 int,
-- id2 int,
-- id3 int,
-- id4 int,
-- id5 int,
-- id6 int,
-- id7 int,
-- id8 int,
-- id9 int
-- ); 

SELECT * FROM students limit 100000;

-- explain analyze select id, g from students where g > 80 and g < 95 order by g desc;

-- create index g_idx on students(g);

-- drop index g_idx;

-- create index g_idx1 on students(g) include (id);

-- DROP TABLE students;

-- SELECT count(*) FROM students;

-- insert into students (g,
-- firstname, 
-- lastname, 
-- middlename,
-- address ,
--  bio,
-- dob,
-- id1 ,
-- id2,
-- id3,
-- id4,
-- id5,
-- id6,
-- id7,
-- id8,
-- id9) 
-- select 
-- random()*100,
-- substring(md5(random()::text ),0,floor(random()*31)::int),
-- substring(md5(random()::text ),0,floor(random()*31)::int),
-- substring(md5(random()::text ),0,floor(random()*31)::int),
-- substring(md5(random()::text ),0,floor(random()*31)::int),
-- substring(md5(random()::text ),0,floor(random()*31)::int),
-- now(),
-- random()*100000,
-- random()*100000,
-- random()*100000,
-- random()*100000,
-- random()*100000,
-- random()*100000,
-- random()*100000,
-- random()*100000,
-- random()*100000
--  from generate_series(0, 500000);