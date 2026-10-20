/*
a) In the coumns section in the actor table the following data fields are listed: actor_id , first_name, last_name, last_update. 
*/

/*
b)  In the coumns section in the film table the following data fields are listed: film_id, title, description, release_year
language_id, original_language_id, rental_duration, rental_date, length
replacement_cost, rating, special_features, last_upadte
*/

/* 
c) No other feilds in sakila have both actor_id and film_id other than film_actor. 
*/

/* 
d) The rental table includes dates, times, inventory id, customer id, and staff id. 
It is a bit hard to read because it's so bunched up together.
*/

/*
e) The inventory table lists the inventory_id, film_id, store_id and last updated time. 
*/

/*
f)I would need to look in the film and rental tables to get the namees of movies and specfic rental dates. 
The tables are all related to each other because they all include information about the same movies production. 
*/

SELECT title FROM film;
SELECT rental_date FROM rental;






