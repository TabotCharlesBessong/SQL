
CREATE TABLE contacts(
    id INT GENERATED BY DEFAULT AS IDENTITY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    PRIMARY KEY (id)
);

INSERT INTO contacts(first_name, last_name, email, phone)
VALUES ('John','Doe','johndoe@gmail.com',NULL),
    ('Lily','Bush','lily.bush@gmail.com','(408-231-2764)'),
    ('Tabot','Charles','tabotcharles@gmail.com','(408-232-2764)'),
    ('Yimnai','Nerus','yimnainerus@gmail.com','(408-233-2764)'),
    ('Atem','Randy','atemrandy@gmail.com','(408-234-2764)'),
    ('Ayamba','Blaise','ayambablaise@gmail.com','(408-235-2764)'),
    ('Leonardo','Dicaprio','leonardodecaprio@gmail.com','(408-234-2761)'),
    ('Acha','Raha','acharaha@gmail.com','(408-234-2762)'),
    ('Yannick','Noah','yannicknoah@gmail.com','(408-234-2763)'),
    ('Stanley','Enow','stanleyenow@gmail.com','(408-234-2764)'),
    ('Tambe','Salome','tambesalome@gmail.com','(408-234-2765)'),
    ('Lambiv','Gills','lambivgills@gmail.com','(408-734-2764)');
    

SELECT * FROM contacts;

CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR (100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

SELECT * FROM basket_a;

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR (100) NOT NULL
);

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');

SELECT * FROM basket_b;

-- INNER JOIN , joins the first table with the second table by matching values in the first and second table

SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
INNER JOIN basket_b
    ON fruit_a = fruit_b;


SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b 
   ON fruit_a = fruit_b;

SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
RIGHT JOIN basket_b ON fruit_a = fruit_b;

SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
FULL OUTER JOIN basket_b 
    ON fruit_a = fruit_b;