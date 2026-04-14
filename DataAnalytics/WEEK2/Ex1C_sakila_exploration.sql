/*
a) The actor table includes each actor's ID, first name, last name, and the last time the record was updated.
b) The film table includes information about each movie, such as the film ID, title, description, release year, rental details, length, rating, and last update.
c) The film_actor table contains both actor_id and film_id.
d) The rental table includes information about each rental transaction, such as the rental ID, rental date, inventory ID, customer ID, return date, and staff ID. It is somewhat hard to read because much of the information is stored as numeric IDs instead of descriptive names.
e) The inventory table includes each inventory item's ID, the film ID for the movie copy, the store ID, and the last update.
f) To find the names of all films rented on a specific date, I would need to use the rental, inventory, and film tables. The rental table shows the rental date and inventory ID, the inventory table connects each inventory item to a film ID, and the film table provides the film title. These tables are related through inventory_id and film_id.
*/

SELECT rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;