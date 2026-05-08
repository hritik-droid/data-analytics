USE northwind;
-- SHOW TABLES;
USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells.
SELECT ProductID, ProductName, UnitPrice
FROM products;

-- 2. Write a query to indentify to identify the products where the unit price is $7.50 or less
SELECT ProductID, ProductNAme, UnitPrice
FROM products
WHERE UnitPrice <= 7.50;

-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder?
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0
  AND UnitsOnOrder > 0;

-- 4. Examine the products table. How does it identify the type (category) of each item sold?
-- Where can you find a list of all categories?
-- Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry.

-- Products table uses CategoryID to identify the category
SELECT ProductID, ProductName, CategoryID
FROM products;

-- Categories table contains the list of all categories
SELECT CategoryID, CategoryName
FROM categories;

-- List of all seafood items
SELECT ProductID, ProductName, CategoryID
FROM products
WHERE CategoryID = (
    SELECT CategoryID
    FROM categories
    WHERE CategoryName = 'Seafood'
);

-- 5. Examine the products table again. How do you know what supplier each product comes from?
-- Where can you find info on suppliers?
-- Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.

-- Products table uses SupplierID to identify the supplier
SELECT ProductID, ProductName, SupplierID
FROM products;

-- Suppliers table contains supplier information
SELECT SupplierID, CompanyName
FROM suppliers;

-- Find the identifier for Tokyo Traders
SELECT SupplierID, CompanyName
FROM suppliers
WHERE CompanyName = 'Tokyo Traders';

-- Find all products from Tokyo Traders
SELECT ProductID, ProductName, SupplierID
FROM products
WHERE SupplierID = (
    SELECT SupplierID
    FROM suppliers
    WHERE CompanyName = 'Tokyo Traders'
);

-- 6. How many employees work at northwind?
SELECT COUNT(*) AS EmployeeCount
FROM employees;

-- What employees have "manager" somewhere in their job title?
SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE Title LIKE '%manager%';