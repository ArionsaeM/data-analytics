USE northwind;

/*
 1. Write a query to list the product id, product name, and unit price of every product. This 
time, display them in ascending order by price.
*/

SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY (UnitPrice) ASC; 

/* 
2. What are the products that we carry where we have at least 100 units on hand? Order 
them in descending order by price.
*/

SELECT ProductName, UnitsInStock  
FROM products
WHERE UnitsInStock >= 100
ORDER BY (UnitsInStock) DESC;

/*
3. What are the products that we carry where we have at least 100 units on hand? Order 
them in descending order by price. If two or more have the same price, list those in 
ascending order by product name. 
*/

SELECT ProductName, UnitsInStock  
FROM products
WHERE UnitsInStock >= 100 
ORDER BY (UnitsInStock) DESC, (ProductName) ASC;

/*
4. Write a query against the orders table that displays the total number of distinct 
customers who have placed orders, based on customer ID. Use an alias to label the 
count calculation as CustomerCount.
*/

SELECT COUNT(DISTINCT CustomerID) AS CustomerCount -- using DISTINCT here accounts for each customer one time not including duplicates. 
FROM Orders; -- returns one row in "customerCount" column because the answer is one number not each customers orders

/*
5. Write a query against the orders table that displays the total number of distinct 
customers who have placed orders, by customer ID, for each country where orders 
have been shipped. Again, use an alias to label the count as CustomerCount. Order 
the list by the CustomerCount, largest to smallest.
*/

SELECT ShipCountry,  COUNT(DISTINCT CustomerID) as CustomerCount
FROM orders
Group BY ShipCountry
ORDER BY (CustomerCount) DESC;

/*
6. What are the products that we carry where we have less than 25 units on hand, but 1 
or more units of them are on order? Write a query that orders them by quantity on 
order (high to low), then by product name.
*/

SELECT ProductName, UnitsOnOrder, UnitsInStock
FROM products

WHERE UnitsInStock <25 AND UnitsOnOrder >=1
ORDER BY (UnitsOnOrder)DESC;

/*
7. Write a query to list each of the job titles in employees, along with a count of how 
many employees hold each job title.
*/

SELECT title, COUNT(employeeID)
FROM employees
GROUP BY title;

/*
8. What employees have a monthly salary that is between $2000 and $2500? Write a 
query that orders them by job title. 
*/

SELECT FirstName, LastName, Salary, title
FROM employees
WHERE Salary BETWEEN 2000 AND 2500 -- use between query NOT greater than less than symbols 
ORDER BY title;