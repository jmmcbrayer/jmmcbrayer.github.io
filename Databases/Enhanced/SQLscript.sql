---- This SQL script will recreat the whole projects 1 and 2 from SNHU DAD-220 class ----
---- This script also contains additional advance SQL queries that were not previously developed ----
---- For running individual queries uncomment what is needed or copy and create a new query for specific needs ----

---- Create a database --
 CREATE DATABASE QuantigrationUpdates;

---- Show a list of all databases ----
SHOW DATABASES;

---- Connect to a database ----
USE QuantigrationUpdates;

---- Create a table specifying the correct data type. ----
---- This buids a Customers table and sets the CustomerID to the primary key. ----
CREATE TABLE Customers (
    CustomerID INT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    StreetAddress VARCHAR(100),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    Telephone VARCHAR(15),
    PRIMARY KEY (CustomerID));

---- Build an Orders table and set the prmary key to OrderID and the Foreign key to CustomerID and it references the Cusomters table CustomerID ----
CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    SKU VARCHAR(50),
    Description VARCHAR(100),
    OrderAmount VARCHAR(20),
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID));


---- Build an RMA table and set the primary key to the RMAID and the Foreign key as OrderID and it references the Orders table OrderID ----
CREATE TABLE RMA (
    RMAID INT,
    OrderID INT,
    Step VARCHAR(50),
    Status VARCHAR(15),
    Reason VARCHAR(15),
    PRIMARY KEY (RMAID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID));


---- Import data from a csv file into the tables ----
---- Command to load data into the Customers table: ----
LOAD DATA INFILE '/home/codio/workspace/customers.csv' 
INTO TABLE Customers 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n';

---- Command to load data into the Order table: ----
LOAD DATA INFILE '/home/codio/workspace/orders.csv' 
INTO TABLE Orders
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n';

---- Command to load data into the RMA table: ----
LOAD DATA INFILE '/home/codio/workspace/rma.csv' 
INTO TABLE RMA
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n';


---- Query to return the count of orders for customers located only in Framingham, Massachusetts using an inner join to link the orders table to customer table ----
SELECT COUNT(*)
FROM Customers
INNER JOIN Orders ON Customers.CustomerID = Orders.CustomerID
WHERE City = 'Framingham' AND State = 'Massachusetts';


---- Query to return all customers located in Massachusetts ----
SELECT *
FROM Customers
WHERE State = 'Massachusetts';


---- Query to insert four new records into the customers table ----
INSERT INTO Customers 
VALUES 
    (100004, 'Luke', 'Skywalker', '15 Maiden Lane', 'New York', 'New York', 10222, '212-555-1234'),
    (100005, 'Winston', 'Smith', '123 Sycamore Street', 'Greensboro', 'North Carolina', 27401, '919-555-6623'),
    (100006, 'MaryAnne', 'Jenkins', '1 Coconut Way', 'Jupiter', 'Florida', 33458, '321-555-8907'),
    (100007, 'Janet', 'Williams', '55 Redondo Beach Blvd', 'Torrence', 'California', 90501, '310-555-5678');


---- Query to insert four new records into the orders table ----
INSERT INTO Orders 
VALUES 
    (1204305, 100004, 'ADV-24-10C', 'Advanced Switch 10GigE Copper 24 port'),
    (1204306, 100005, 'ADV-48-10F', 'Advanced Switch 10 GigE Copper/Fiber 44 port copper 4 port fiber'),
    (1204307, 100006, 'ENT-24-10F', 'Enterprise Switch 10GigE SFP+ 24 Port'),
    (1204308, 100007, 'ENT-48-10F', 'Enterprise Switch 10GigE SFP+ 48 port');


---- Query to count all records where the cist is Woonsocket and the state is Rhode Island. ----
SELECT COUNT(*) AS CustCount 
FROM Customers 
WHERE City = 'Woonsocket' AND State = 'Rhode Island';


---- Query to get the Status and Step information from the RMA database where the OrderID is 5175 ----
SELECT Status, Step 
FROM RMA
WHERE OrderID = 5175;


---- Query to update the Status and Step information for OrderID 5175 to Status Complete and Step Credit Customer Account ----
UPDATE RMA
SET Status = 'Complete', Step = 'Credit Customer Account'
WHERE OrderID = 5175;


---- Query to delete ALL records from the RMA database where reason is set to Rejected ----
DELETE 
FROM RMA 
WHERE reason = 'Rejected';


---- Rename Customers table to Collaborators: ----
RENAME TABLE Customers TO Collaborators;

---- Rename CusteromID field to CollaboratorID in the Collaborators table ----
ALTER TABLE Collaborators CHANGE CustomerID CollaboratorID INT;

---- Rename CusteromID field to CollaboratorID in the Orders table ----
ALTER TABLE Orders CHANGE CustomerID CollaboratorID INT;


---- Query to output all the information from the Orders table to a csv file ----
SELECT * 
FROM Orders 
INTO OUTFILE '/home/codio/workspace/Orders-Project1.csv' 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\r\n';


---- Query to pull the number of reutnrs by state grouping by the state and in descending order ----
SELECT State, COUNT(*) AS Count
FROM RMA
INNER JOIN Orders ON RMA.OrderID = Orders.OrderID
INNER JOIN Collaborators ON Orders.CollaboratorID = Collaborators.CollaboratorID
GROUP BY Collaborators.State
ORDER BY Count DESC;


---- Query to get the percentage of returns by product type ----
---- Left join is used in this query to pull back all orders total needed to calculate the percentage.
---- COUNT(RMA.RMAID) gets the total returns
---- COUNT(DISTINCT Orders.OrderID) gets the total orders
---- ReturnPercentage calculates the percentage of returns based off the total orders
SELECT 
    Orders.SKU, 
    Orders.Description,
    COUNT(RMA.RMAID) AS Returns, 
    COUNT(DISTINCT Orders.OrderID) AS Orders,  
    ROUND((COUNT(RMA.RMAID) * 100.0) / COUNT(DISTINCT Orders.OrderID), 2) AS ReturnPercentage
FROM Orders 
LEFT JOIN RMA ON Orders.OrderID = RMA.OrderID
GROUP BY Orders.SKU, Orders.Description
ORDER BY ReturnPercentage DESC;


SELECT
    CollaboratorID,
    FirstName,
    LastName,
    COALESCE(SUM(Orders.OrderAmount), 0) AS TotalOrderAmount
    RANK() OVER (ORDER BY SUM(Orders.OrderAmount) DESC) AS ranking
FROM Collaborators
LEFT JOIN Orders
    ON Collaborators.CollaboratorID = Orders.CollaboratorID
GROUP BY
    Collaborators.CollaboratorID,
    Collaborators.FirstName,
    Collaborators.LastName
ORDER BY
    ranking;