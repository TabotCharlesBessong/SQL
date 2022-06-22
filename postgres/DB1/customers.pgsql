
-- CREATE TABLE customers(
--   custId INTEGER ,
--   custname varchar(50),
--   address TEXT,
--   quantity INTEGER);


INSERT INTO customers VALUES (1,'Tabot Charles','Molyko',10000);
INSERT INTO customers VALUES (2,'Yimnai Nerus','Glas Quater',10000);
INSERT INTO customers VALUES (12,'Balemba Junior','Molyko',10000);
INSERT INTO customers VALUES (3,'Balemba Junior','Douala',10000);
INSERT INTO customers VALUES (4,'Atem Randy','Tiko',10000);
INSERT INTO customers VALUES (5,'Ayamba Blaise','Tiko',10000);
INSERT INTO customers VALUES (6,'Leonardo Decaprio','Douala',10000);
INSERT INTO customers VALUES (7,'Acha Raha','Molyko',10000);
INSERT INTO customers VALUES (8,'Yannick Noah','Glas Quater',10000);
INSERT INTO customers VALUES (9,'Stanley Enow','Douala',10000);
INSERT INTO customers VALUES (10,'Tambe Salome','Molyko',10000);
INSERT INTO customers VALUES (11,'Lambiv Gills','Molyko');

DELETE FROM customers WHERE custname = 'Balemeba Junior' ; 

-- alias selection short way
SELECT address  Residence FROM customers ;

-- alias selection long way
SELECT address AS Residence FROM customers ;

--  order by select 
SELECT custname , custid , quantity , length(custname) namesLength FROM customers ORDER BY address ASC , namesLength DESC ;

-- handling NULL Values when selecting and ordering by 

-- The NULLS FIRST option places NULL before other non-null values and the NULL LAST option places NULL after other non-null values.

-- so with the explanation above and with the example below our null value will be placed at the top of all other non null values

SELECT custname , address , quantity  from customers ORDER BY quantity NULLS FIRST;

-- The distinct selection used to remove duplicate from certain selection in a database  

-- if multiple columns are selected then the distinct apply to the 2 in an OR gate approach
SELECT DISTINCT address , custname FROM customers ORDER BY custname ;

-- DISTINCT ON will sort based on the element in the bracket

SELECT DISTINCT ON (custname)  custname , custid FROM customers;

-- WHERE SELECT clause which select base on some conditions 

-- default SELECT 

SELECT custname FROM customers WHERE address = 'Molyko' OR custname = 'Balemba Junior' ORDER BY custname DESC;

-- WHERE clause with the IN OPERATOR
SELECT custname , quantity FROM customers WHERE custname IN ('Tabot Charles','Yimnai Nerus','Yannick Noah');

-- LIKE OPERATOR and the WHERE clause 
-- some more of the LIKE %: any CHARACTER of zero or more matches , ( _ ) matches any single CHARACTER , (f%) : any matches that start with the CHARACTER , (_o_) any matching BETWEEN o (b_) : first CHARACTER bieng b and the rest staying same , (_her%): matches any sting that begins with any single CHARACTER and is followed by her and is ended by any match of CHARACTER

-- NOT LIKE will matche the oposite of LIKE,
-- ILIKE matches values that are case sensitive  

SELECT custname FROM customers WHERE custname LIKE '%nior';

-- BETWEEN OPERATOR in the WHERE clause SELECT

-- some WHERE clause OPERATORS <>: NOT equal or != , IS NULL chooses values that are NULL in value
SELECT custid , custname , length(custname) nameLength FROM customers WHERE length(custname) BETWEEN 12 AND 18;

-- limit clause  , The OFFSET in the LIMIT clause tells where the selection should start from 
SELECT * FROM customers LIMIT 7 OFFSET 4 ;
SELECT  custname,  custid , address from customers WHERE length(custname) > 12 ; 

-- The FETCH clause will give you more flexibility than the LIMIT clause
SELECT custname from customers ORDER BY address FETCH FIRST 5 ROW ONLY;

-- IN OPERATOR 
SELECT custid , custname from customers WHERE custid in(1,4,5,7,2,9);

-- as a parameter to the IN OPERATOR , you can use result of the SELECT to pass in the IN OPERATOR

SELECT * FROM customers WHERE custid IN (
  SELECT custid from customers WHERE address = 'Molyko'
);

SELECT * FROM customers ;