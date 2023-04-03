-- SELECT * FROM world.city;
USE world;
SELECT Name,District,CountryCode,Population FROM world.city WHERE (Population BETWEEN 100000 AND 500000) AND (CountryCode IN ('AFG','NLD','DZA','ANT'));