USE northwind;

-- 1. List product id, product name, and unit price in ascending order by price
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;

-- 2. Products with at least 100 units in stock, ordered by price descending
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;

-- 3. Same as above, but if same price, order by product name ascending
SELECT ProductID, ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;

-- 4. Total number of distinct customers who placed orders
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders;

-- 5. Distinct customers per country, ordered by count descending
SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;

-- 6. Products with less than 25 in stock but at least 1 on order
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25
  AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- 7. Job titles and how many employees have each title
SELECT Title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title;