---- List all customers and the total amount spent ----
---- LEFT JOIN ensure that customers without any purchases are included ----
---- JOIN could be used if you only wanted to return customers with orders ----
---- COALESCE returns the first non-null value, returns 0 instead of null if no orders have been placed ----
SELECT c.CustomerID, c.FirstName, c.LastName,
       COALESCE(SUM(o.OrderAmount), 0) AS TotalSpent
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalSpent DESC
LIMIT 10;


---- Find customers who have never placed an order ----
---- Returns information based on OrderID being NULL ----
SELECT c.CustomerID, c.FirstName, c.LastName
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL
LIMIT 10;


---- Find customers who have never placed an order ----
---- Returns information based on no order being found using WHERE NOT EXISTS ----
---- Ideal for larger datasets ----
SELECT c.CustomerID, c.FirstName, c.LastName
FROM Customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    WHERE o.CustomerID = c.CustomerID
)
LIMIT 10;


---- Find orders that have RMAs ----
---- Will only return order information that have an RMA ----
---- Using LEFT JOIN will return all order even without RMAs ----
SELECT o.OrderID, o.SKU, o.OrderAmount, r.RMAID, r.Status
FROM Orders o
JOIN RMA r ON o.OrderID = r.OrderID
LIMIT 10;


---- Return how many RMAs are associated with an order ----
SELECT o.OrderID, COUNT(r.RMAID) AS RMA_Count
FROM Orders o
LEFT JOIN RMA r ON o.OrderID = r.OrderID
GROUP BY o.OrderID
LIMIT 10;


---- Return only pending RMAs ----
SELECT o.OrderID, o.SKU, o.OrderAmount, r.RMAID, r.Status
FROM Orders o
JOIN RMA r ON o.OrderID = r.OrderID
WHERE r.Status = 'Pending'
LIMIT 10;


---- Count how many RMAs each customer has even if 0 ----
---- use JOIN instead of LEFT JOIN to count RMAs only if not 0 ----
SELECT c.CustomerID, c.FirstName, c.LastName,
       COUNT(r.RMAID) AS RMA_Count
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
LEFT JOIN RMA r ON o.OrderID = r.OrderID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY RMA_Count DESC
LIMIT 10;


---- Show RMA status breakdown ----
---- Ordered in descending order ----
---- Include percentage of each ----
SELECT 
    Status,
    COUNT(*) AS CountPerStatus,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM RMA), 2) AS PercentOfTotal
FROM RMA
GROUP BY Status
LIMIT 10;


---- Find the highest-value order for each customer ----
SELECT c.CustomerID, c.FirstName, c.LastName, o.OrderID, o.OrderAmount
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderAmount = (
    SELECT MAX(o.OrderAmount)
    FROM Orders o2
    WHERE o2.CustomerID = c.CustomerID
)
LIMIT 10;


---- same as above, but using window function (OVER) and adding ranking ----
SELECT c.CustomerID, c.FirstName, c.LastName, c.OrderID, c.OrderAmount
FROM (
    SELECT c.CustomerID, c.FirstName, c.LastName,
           o.OrderID, o.OrderAmount,
           RANK() OVER (
               PARTITION BY c.CustomerID
               ORDER BY o.OrderAmount DESC
           ) AS rnk
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
) ranked
WHERE rnk = 1
LIMIT 10;


---- Running total of orders per customer (window function) ----
---- Window function calculates across a set of rows without collapsing into a single ly GROUP BY ----
SELECT 
    c.CustomerID, 
    c.FirstName, 
    c.LastName, 
    o.OrderID, 
    o.OrderAmount,
    SUM(o.OrderAmount) OVER (PARTITION BY c.CustomerID ORDER BY o.OrderID) AS RunningTotal
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
LIMIT 10;


---- Find top 3 customers by total amount spent ----
---- ordered in descending order ----
SELECT c.CustomerID, c. FirstName, c.LastName,
       SUM(o.OrderAmount) AS TotalSpent
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalSpent DESC, c.LastName ASC
LIMIT 3;


---- Same as above, but including of total revenue ----
SELECT c.CustomerID, c.FirstName, c.LastName,
       SUM(o.OrderAmount) AS TotalSpent,
       ROUND(SUM(o.OrderAmount) * 100.0 / (SELECT SUM(OrderAmount) FROM Orders), 2) AS PercentOfTotal
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.FirstName, c.LastName
ORDER BY TotalSpent DESC
LIMIT 3;


---- Same as above but using a window function ----
---- If 3rd and 4th are tied both will be returned ----
SELECT CustomerID, FirstName, LastName, TotalSpent
FROM (
    SELECT c.CustomerID, c.FirstName, c.LastName,
           SUM(o.OrderAmount) AS TotalSpent,
           RANK() OVER (ORDER BY SUM(o.OrderAmount) DESC) AS rnk
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    GROUP BY c.CustomerID, c.FirstName, c.LastName
) ranked
WHERE rnk <= 3;