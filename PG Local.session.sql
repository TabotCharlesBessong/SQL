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
  weather ()