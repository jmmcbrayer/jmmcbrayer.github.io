#============================================================================
# Name        : Python_List_Functions.py
# Author      : Michael McBrayer
# Version     : 1.0
# Copyright   : Copyright © 2017 SNHU CODE
# Description : CS-449 Capstone Project to port LinkedList.cpp to Python
#               This file provides supporting functions to the application
#============================================================================


import csv
from Python_List_Classes import Bid, PythonList


# Gather bid information from the user and build a new Bid object
# Returns the new bid to the calling function
def createBid():
    bidId = input("Enter Id: ")
    title = input("Enter title: ")
    fund = input("Enter fund: ")
    amount = input("Enter amount: ")
    
    newBid = Bid(bidId, title, fund, amount)

    return newBid


# Load bids from a csv file. Default file name is provided if the user does not enter anything.
def loadBids():
    defaultPath = "eBid_Monthly_Sales_Dec_2016.csv"
    fileName = input("Please enter the file name (if blank default is eBid_Monthly_Sales_Dec_2016.csv): ")
    if fileName == "" or fileName == None:  # if the user does not enter any file information it will use the default name
        fileName = defaultPath

    print(f"Loading CSV file {fileName}")

    try:
        with open(fileName, 'r') as file:  # open the file as variable file
            fileData = csv.reader(file)  # read the csv content from the file into fileData
            has_header = csv.Sniffer().has_header(file.read(2048))  # reads the first 2048 lines of the csv file to try to determine if the first row contains headers.
            
            if has_header:  # if the sniffer finds a header skip the first line of data
                next(fileData)
            
            for row in fileData:  # for each row in the data from the csv file build a new bid.
                newBid = Bid(row[1], row[0], row[8], row[4])  # relevant bid information is found in column 2, then 1, then 9 and then 5
                PythonList.appendList(newBid)  # append each newBid to the list
            
    except Exception as e:
        print(e)
        print("Please try again.")


# Support utility to get a bid ID from the user.
# If no bid ID is entered it will use the default bid ID.
# Returns the bid ID either user input or default
def getBidId():
    defaultBid = "98109"
    bidId = input("Please enter the Bid ID (if blank default is 98109): ")
    if bidId == "" or bidId == None:
        bidId = defaultBid

    return bidId


# Function to calculate and print the time elapsed both in milliseconds and seconds.
def printTimeElapsed(startTime, endTime):
    print(f"time: {round(((endTime - startTime) * 1000), 2)} milliseconds")
    print(f"time: {round((endTime - startTime), 2)} seconds")