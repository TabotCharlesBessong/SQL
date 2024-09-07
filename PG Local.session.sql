CREATE TABLE
  IF NOT EXISTS users (
    ID SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
  );

INSERT INTO
  users (username, email)
VALUES
  ('John Doe', 'john.doe@gmail.com'),
  ('Charles Tabot', 'charles.tabot@gmail.com'),
  ('Christopher Froome', 'christ.froome@yahoo.com');

CREATE TABLE
  weather (
    city VARCHAR(80),
    temp_lo int,
    temp_hi int,
    date_day date
  );

DROP TABLE weather;

CREATE TABLE cities (
 name varchar(80),
 location point
);

INSERT INTO weather VALUES ('San Francisco', 46, 50,
 '1994-11-27');

INSERT INTO cities VALUES ('San Francisco', '(-194.0, 53.0)');

SELECT * from weather;
