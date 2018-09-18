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
USE sakila;
DESCRIBE sakila.address;

-- 6a --
/* Use JOIN to display the first and last names, as well as the address, of 
each staff member. Use the tables staff and address: */
USE sakila;
SELECT staff.first_name, staff.last_name, address.address 
FROM staff INNER JOIN address 
ON staff.address_id = address.address_id;

-- 6b --
/* Use JOIN to display the total amount rung up by each staff member in 
August of 2005. Use tables staff and payment. */

USE sakila;
SELECT merge_table.first_name, merge_table.last_name, SUM(merge_table.amount) AS 'Total' 

FROM (
    SELECT staff.first_name, staff.last_name, payment.payment_date, payment.amount
    FROM staff INNER JOIN payment 
    ON staff.staff_id = payment.staff_id
    WHERE MONTH(payment_date) = 08 AND YEAR(payment_date) = 2005
    ) AS merge_table

GROUP BY merge_table.first_name, merge_table.last_name;

-- 6c --
/* List each film and the number of actors who are listed for that film. 
Use tables film_actor and film. Use inner join. */

USE sakila;
SELECT merge_table.film_id, merge_table.title, count(merge_table.actor_id) AS 'actor_count'
FROM (
    SELECT film_actor.film_id, film_actor.actor_id, film.title
    FROM film_actor INNER JOIN film
    ON film_actor.film_id = film.film_id
    ) AS merge_table

GROUP BY merge_table.title, merge_table.film_id;

-- 6d --
/* How many copies of the film Hunchback Impossible exist in the inventory 
system? */

USE sakila;
SELECT f.film_id, f.title, count(i.inventory_id) AS 'inventory_count'
FROM inventory i INNER JOIN film f
ON i.film_id = f.film_id
GROUP BY film_id;

-- 6e --
/* Using the tables payment and customer and the JOIN command, list the total 
paid by each customer. List the customers alphabetically by last name:*/

USE sakila;
SELECT c.customer_id, c.first_name, c.last_name, SUM(p.amount) AS 'total_payment'
FROM payment p INNER JOIN customer c
ON p.customer_id = c.customer_id
GROUP BY customer_id
ORDER BY last_name;

-- 7a --
/* The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
As an unintended consequence, films starting with the letters K and Q have also 
soared in popularity. Use subqueries to display the titles of movies starting 
with the letters K and Q whose language is English. */
USE sakila;
SELECT * FROM film;

USE sakila;
SELECT * FROM language;

USE sakila;
SELECT title FROM film
WHERE (title LIKE 'K%' OR title LIKE 'Q%') 
AND language_id = (SELECT language_id FROM language WHERE name = 'English')

-- 7b --
/* Use subqueries to display all actors who appear in the film Alone Trip. */
USE sakila;
SELECT * FROM actor;

USE sakila;
SELECT * FROM film;

USE sakila;
SELECT * FROM film_actor;

USE sakila;
SELECT first_name, last_name FROM actor
WHERE actor_id IN (SELECT actor_id FROM film_actor WHERE film_id = 
    (SELECT film_id FROM film WHERE title = 'ALONE TRIP')
)

USE sakila;
SHOW CREATE TABLE address;

-- 7c --
/* You want to run an email marketing campaign in Canada, for which you will 
need the names and email addresses of all Canadian customers. Use joins to retrieve 
this information.*/

USE sakila;
SELECT * FROM customer;

USE sakila;
SELECT * FROM customer_list;

USE sakila;
SELECT cl.name, c.customer_id, c.email, cl.country
FROM customer c INNER JOIN customer_list cl
ON c.customer_id = cl.ID
WHERE country = 'Canada';

-- 7d --
/* Sales have been lagging among young families, and you wish to target all 
family movies for a promotion. Identify all movies categorized as family films. */

USE sakila;
SELECT film.title FROM film
WHERE film_id IN (SELECT film_id FROM film_category WHERE category_id = 
    (SELECT category_id FROM category WHERE name = 'Family')
    );


-- 7e --
/* Display the most frequently rented movies in descending order. */

USE sakila;
SELECT title, COUNT(f.film_id) AS 'rental_count'
FROM film f
JOIN inventory i ON (f.film_id= i.film_id)
JOIN rental r ON (i.inventory_id=r.inventory_id)
GROUP BY title
ORDER BY rental_count DESC;

-- 7f --
/* Write a query to display how much business, in dollars, each store brought in. */

USE sakila;
SELECT s.store_id, SUM(p.amount) AS 'total_amount'
FROM payment p INNER JOIN staff s
ON p.staff_id = s.staff_id
GROUP BY store_id; 

-- 7g --
/* Write a query to display for each store its store ID, city, and country. */

USE sakila;
SELECT store_id, city, country FROM store s
JOIN address a ON (s.address_id=a.address_id)
JOIN city c ON (a.city_id=c.city_id)
JOIN country ctry ON (c.country_id=ctry.country_id);

-- 7h --
/* List the top five genres in gross revenue in descending order. (Hint: you may 
need to use the following tables: category, film_category, inventory, payment, and 
rental.) */

USE sakila;
SELECT c.name AS "category_name", SUM(p.amount) AS "Gross" 
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name 
ORDER BY Gross DESC LIMIT 5;

-- 8a --
/* In your new role as an executive, you would like to have an easy way of viewing 
the Top five genres by gross revenue. Use the solution from the problem above to 
create a view. If you haven't solved 7h, you can substitute another query to create 
a view. */

USE sakila;
CREATE VIEW Top_Five_View AS
SELECT c.name AS "category_name", SUM(p.amount) AS "Gross" 
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN inventory i ON fc.film_id = i.film_id
JOIN rental r ON i.inventory_id = r.inventory_id
JOIN payment p ON r.rental_id = p.rental_id
GROUP BY c.name 
ORDER BY Gross DESC LIMIT 5;

-- 8b --
/* How would you display the view that you created in 8a? */

USE sakila;
SELECT * FROM Top_Five_View;

-- 8c --
/* You find that you no longer need the view top_five_genres. Write a query to delete 
it. */

USE sakila;
DROP VIEW Top_Five_View;
