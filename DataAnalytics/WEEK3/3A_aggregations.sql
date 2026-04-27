USE northwind;

-- 1. Find the price of the cheapest item that Northwind sells.
SELECT MIN(UnitPrice) AS CheapestPrice
FROM products;

-- 1. Find the name of the product that has the cheapest price.
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (
    SELECT MIN(UnitPrice)
    FROM products
);

-- 2. Find the average price of all items that Northwind sells.
SELECT AVG(UnitPrice) AS AveragePrice
FROM products;

-- Bonus: rounded to nearest cent
SELECT ROUND(AVG(UnitPrice), 2) AS AveragePriceRounded
FROM products;

-- 3. Find the price of the most expensive item that Northwind sells.
SELECT MAX(UnitPrice) AS MostExpensivePrice
FROM products;

-- 3. Find the name of the product with that price, plus the supplier name.
SELECT p.ProductName, p.UnitPrice, s.CompanyName AS SupplierName
FROM products p
JOIN suppliers s
ON p.SupplierID = s.SupplierID
WHERE p.UnitPrice = (
    SELECT MAX(UnitPrice)
    FROM products
);

-- 4. Find total monthly payroll.
SELECT SUM(Salary) AS TotalMonthlyPayroll
FROM employees;

-- 5. Find the highest and lowest salary amounts.
SELECT MAX(Salary) AS HighestSalary, MIN(Salary) AS LowestSalary
FROM employees;

-- 6. Find supplier name, supplier ID, and number of items they supply.
SELECT s.CompanyName, s.SupplierID, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName, s.SupplierID;

-- 7. Find all category names and the average price for items in each category.
SELECT c.CategoryName, AVG(p.UnitPrice) AS AveragePrice
FROM categories c
JOIN products p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName;

-- 8. Find suppliers that provide at least 5 items, with supplier name and item count.
SELECT s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
JOIN products p
ON s.SupplierID = p.SupplierID
GROUP BY s.CompanyName
HAVING COUNT(p.ProductID) >= 5;

-- 9. List products in inventory with inventory value, sorted by value descending.
SELECT ProductID,
       ProductName,
       UnitPrice * UnitsInStock AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName ASC;