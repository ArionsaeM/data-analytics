USE northwind;
/*
1. Write a query to find the price of the cheapest item that Northwind sells. Then write a 
second query to find the name of the product that has that price.
*/

SELECT MIN(UnitPrice) FROM products;

SELECT ProductName FROM Products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM Products); 


 /*
2. Write a query to find the average price of all items that Northwind sells. 
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help 
using the ROUND function to round the average price to the nearest cent.) 
*/
SELECT ROUND(AVG(UnitPrice),2) FROM products; -- without round (SELECT AVG(UnitPrice) FROM products;) 

/*
3. Write a query to find the price of the most expensive item that Northwind sells. Then 
write a second query to find the name of the product with that price, plus the name of 
the supplier for that product. 
*/
SELECT MAX(UnitPrice) FROM products;

SELECT UnitPrice, CompanyName, ProductName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID 

WHERE products.UnitPrice = (
	SELECT MAX(UnitPrice)
    FROM Products
)
ORDER BY ProductName;

/*
4. Write a query to find total monthly payroll (the sum of all the employees’ monthly 
salaries). 
*/
SELECT SUM(SALARY) 
FROM employees; -- $20362.93

/*
5. Write a query to identify the highest salary and the lowest salary amounts which any 
employee makes. (Just the amounts, not the specific employees!)
*/
SELECT MIN(Salary), MAX(Salary) -- comma represents "AND " here 
FROM employees;

/* 
6. Write a query to find the name and supplier ID of each supplier and the number of 
items they supply. Hint: Join is your friend here. 
*/

SELECT CompanyName, suppliers.SupplierID, COUNT(ProductID)
FROM suppliers
 JOIN Products
 ON products.SupplierID = suppliers.SupplierID 
GROUP BY  CompanyName, products.SupplierID;

/*
7. Write a query to find the list of all category names and the average price for items in 
each category. 
*/

SELECT CategoryName, AVG(UnitPrice)
FROM categories
JOIN products
ON products.CategoryID = categories.CategoryID
GROUP BY products.CategoryID;

 
/*
8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what 
is the name of each supplier and the number of items they supply.
*/

SELECT CompanyName, COUNT(DISTINCT(ProductID)) FROM suppliers
JOIN products
ON products.SupplierID = suppliers.SupplierID
GROUP BY CompanyName
HAVING COUNT(DISTINCT(ProductID)) >= 5;


/*
9. Write a query to list products currently in inventory by the product id, product name, 
and inventory value (calculated by multiplying unit price by the number of units on 
hand). 
Sort the results in descending order by value.
 If two or more have the same 
value, order by product name. 
If a product is not in stock, leave it off the list. 
*/

SELECT ProductID, ProductName, (UnitPrice*UnitsInStock) AS `Inventory Value`
FROM products
WHERE UnitsInStock <= 1 -- used where here instead of having 
ORDER BY `Inventory Value` DESC, ProductName ASC;