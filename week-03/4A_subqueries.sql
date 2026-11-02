USE northwind;

/*
1. What is the product name(s) of the most expensive products?  
∗ HINT: Find the max price in a subquery and then use that value to find products 
whose price equals that value. (Some of your answers from Exercise 3.A may offer a 
useful starting point.) 
*/

SELECT ProductName,(
	SELECT MAX(UnitPrice)
    FROM products) AS MaxItemPrice
    FROM products
    WHERE UnitPrice = (
	SELECT MAX(UnitPrice)
    FROM products);

/*
2. What is the product name(s) and categories of the least expensive products?  
∗ HINT: Find the min price in a subquery and then use that in your more complex 
query that joins products with categories. 
*/

SELECT ProductName, CategoryName, (
	SELECT MIN(UnitPrice)
    FROM products) AS MinPrice
    FROM products
    JOIN categories
    ON products.CategoryID = categories.CategoryID
WHERE UnitPrice = (SELECT MIN(UnitPrice)
FROM products);
    
    


/*
3. What is the order id, shipping name and shipping address of all orders shipped via 
"Federal Shipping"?  
∗ HINT: Find the shipper id of "Federal Shipping" in a subquery and then use that 
value to find the orders that used that shipper. 
∗ You do not need "Federal Shipping" to display in the results. 
*/

SELECT orderID, ShipName, ShipAddress
    FROM orders
    WHERE ShipVia = (
		SELECT ShipperID
		FROM shippers 
		WHERE CompanyName = 'Federal Shipping'
        ); -- 255 rows returned 


/*
4. What are the order ids of the orders that included "Sasquatch Ale"?  
∗ HINT: Find the product id of "Sasquatch Ale" in a subquery and then use that value 
to find the matching orders from the `order details` table.  
∗ Your final results only need to display OrderID, but you may find it helpful to include 
additional columns as you work on creating the query to better understand how the 
query is working.  
*/

SELECT OrderID
FROM `order details` 
WHERE ProductID =  ( 
	SELECT ProductID 
    FROM products
    WHERE ProductName = "Sasquatch Ale"
    ); -- 19 rows returned
/*
5. What is the name of the employee that sold order 10266? 

Key rule: When one table has the information you want, but another table identifies which record you need, use a subquery in WHERE.

Memory trick: The inner query finds WHO or WHAT to look for. The outer query displays the answer.
*/

SELECT LastName, FirstName
FROM employees 

WHERE Employees.EmployeeID = (
	SELECT EmployeeID
    FROM orders
    WHERE OrderID = "10266");


/*
6. What is the name of the customer that bought order 10266?
*/
SELECT ContactName
FROM customers 

WHERE CustomerID = (
	SELECT CustomerID
    FROM orders
    WHERE OrderID = "10266");