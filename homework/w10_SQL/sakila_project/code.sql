-- 0 --
/* retrive information from table */
USE sakila; 
SELECT count(*) FROM actor;

USE sakila;
SELECT count(*) FROM information_schema.columns WHERE table_name = 'actor';

-- 1a --
/* Display the first and last names of all actors from the table actor */
USE sakila;
SELECT first_name, last_name FROM actor;

-- 1b --
/* Display the first and last name of each actor in a single column 
 in upper case letters. Name the column Actor Name. */
USE sakila;
SELECT Concat(first_name, ' ', last_name) AS 'Actor Name' FROM actor;

-- 2a --
/* You need to find the ID number, first name, and last name of an actor, 
of whom you know only the first name, "Joe." What is one query would you use 
to obtain this information? */
USE sakila;
SELECT Concat(first_name, ' ', last_name) AS 'Actor Name' FROM actor
WHERE first_name = 'JOE';

-- 2b --
/* Find all actors whose last name contain the letters GEN */
USE sakila;
SELECT Concat(first_name, ' ', last_name) AS 'Actor Name' FROM actor
WHERE last_name LIKE '%GEN%';

-- 2c --
/* Find all actors whose last names contain the letters LI. This time, 
order the rows by last name and first name, in that order: */
USE sakila;
SELECT Concat(first_name, ' ', last_name) AS 'Actor Name' FROM actor
WHERE last_name LIKE '%LI%'
ORDER BY last_name, first_name;

-- 2d --
/* Using IN, display the country_id and country columns of the following 
countries: Afghanistan, Bangladesh, and China:*/
USE sakila;
SELECT country_id, country FROM country
WHERE country IN ('Afghanistan', 'Bangladesh', 'China');

-- 3a --
/* You want to keep a description of each actor. You don't think you 
will be performing queries on a description, so create a column in the table 
actor named description and use the data type BLOB (Make sure to research 
the type BLOB, as the difference between it and VARCHAR are significant). */
USE sakila;
ALTER TABLE actor
    ADD COLUMN description BLOB;

-- 3d --
/* Very quickly you realize that entering descriptions for each actor is too 
much effort. Delete the description column.*/
USE sakila;
ALTER TABLE actor
    DROP COLUMN description;

-- 4a --
/* List the last names of actors, as well as how many actors have that last 
name.*/
USE sakila;
SELECT last_name, count(*) AS number_lastname FROM actor  
GROUP BY last_name; 

-- 4b --
/* List last names of actors and the number of actors who have that last name, 
but only for names that are shared by at least two actors */
USE sakila;
SELECT last_name, count(*) AS number_lastname FROM actor  
GROUP BY last_name
HAVING number_lastname >= 2;

-- 4c --
/* The actor HARPO WILLIAMS was accidentally entered in the actor table as 
GROUCHO WILLIAMS. Write a query to fix the record.*/
USE sakila;

UPDATE actor
SET first_name = 'HARPO'
WHERE first_name = 'GROUCHO' AND last_name = 'WILLIAMS';

USE sakila;
SELECT * FROM actor
WHERE last_name = 'WILLIAMS';

-- 4d --
/* Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that 
GROUCHO was the correct name after all! In a single query, if the first name 
of the actor is currently HARPO, change it to GROUCHO. */

/*
USE sakila;
SELECT * FROM actor
WHERE first_name = 'HARPO';
*/

USE sakila;
UPDATE actor
SET first_name = 'GROUCHO'
WHERE first_name = 'HARPO';

/*
USE sakila;
SELECT * FROM actor
WHERE first_name = 'GROUCHO';
*/

-- 5a --
/* You cannot locate the schema of the address table. Which query would you use 
to re-create it? */

