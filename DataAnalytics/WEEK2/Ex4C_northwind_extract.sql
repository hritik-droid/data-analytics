USE northwind;

/*
a) The table that holds the items Northwind sells is called 'products'.

b) The table that holds the types/categories of items is called 'categories'.
*/

-- Question 5
SELECT * FROM employees;

-- Answer:
-- The employee whose name looks like a bird is "Margaret Peacock"

-- Question 6
SELECT * FROM products;

-- Answer:
-- This query returns 77 records.
-- To retrieve only 10 rows, use the LIMIT keyword:
SELECT * FROM products LIMIT 10;

-- Question 7
SELECT * FROM categories;

-- Answer:
-- The category_id of seafood is 8

-- Question 8
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;
