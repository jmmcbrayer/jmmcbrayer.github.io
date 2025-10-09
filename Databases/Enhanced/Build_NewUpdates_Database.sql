---- This SQL script will recreat the whole projects 1 and 2 from SNHU DAD-220 class ----
---- This script also contains additional advance SQL queries that were not previously developed ----
---- For running individual queries uncomment what is needed or copy and create a new query for specific needs ----

---- Create a database --
 CREATE DATABASE NewUpdate;

---- Connect to a database ----
USE QuantigrationUpdates;

DROP TABLE IF EXISTS Customers;

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
    PRIMARY KEY (CustomerID)
);

DROP TABLE IF EXISTS Orders;

---- Build an Orders table and set the prmary key to OrderID and the Foreign key to CustomerID and it references the Cusomters table CustomerID ----
CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    SKU VARCHAR(50),
    Description VARCHAR(100),
    OrderAmount DECIMAL(10,2),
    PRIMARY KEY (OrderID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    CHECK (OrderAmount >= 0) -- added to validate the amount is not negative
);

DROP TABLE IF EXISTS RMA;

---- Build an RMA table and set the primary key to the RMAID and the Foreign key as OrderID and it references the Orders table OrderID ----
CREATE TABLE RMA (
    RMAID INT,
    OrderID INT,
    Step VARCHAR(50),
    Status VARCHAR(15),
    Reason VARCHAR(15),
    PRIMARY KEY (RMAID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
    CHECK (Status IN ('Complete', 'Initiated', 'Pending'))  -- added to validate correct type of status was entered
);


---- Import data from a csv file into the tables ----
---- Command to load data into the Customers table: ----
LOAD DATA INFILE '/home/codio/workspace/customers.csv' 
INTO TABLE Customers 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n';

---- Command to load data into the Order table: ----
LOAD DATA INFILE '/home/codio/workspace/ordersWithDollars.csv' 
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

