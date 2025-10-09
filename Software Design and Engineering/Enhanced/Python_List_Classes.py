#============================================================================
# Name        : Python_List_Classes.py
# Author      : Michael McBrayer
# Version     : 1.0
# Copyright   : Copyright © 2017 SNHU CODE
# Description : CS-449 Capstone Project to port LinkedList.cpp to Python
#               Provides Bid, and PythonList class information
#============================================================================


# Class to build each bid object
class Bid:
    def __init__(self, bidId, title, fund, amount) -> None:
        self.bidId = bidId # ID of the bid
        self.title = title # title of the bid
        self.fund = fund # the bid will be part of

        if isinstance(amount, str):  # the user input will be a string and this confirms
            amount = amount.replace(",", "").replace("$", "")  # input is a monetary value so may contain $ or ,.  This will remove these so the string can be converted to a float.
            amount = float(amount)  # convert the string to float value
        
        self.amount = amount  # bid amount entered as a float

    # function to print bid information to the screen.
    def printBid(self):
        print(f"{self.bidId}: {self.title} | {self.amount} | {self.fund}")


# Class to handle and build the list of data
class PythonList:
    bidList = []

    @classmethod
    def appendList(cls, bid):  # appends bid to the list
        cls.bidList.append(bid)

    @classmethod
    def prependList(cls, bid):  # prepend bid to the list (no build in prepend function so insert is used to place the bid at the beginning)
        cls.bidList.insert(0, bid)

    @classmethod
    def searchList(cls, bidId):  # uses a forloop to search the list by the bidId
        for bid in cls.bidList:
            if bid.bidId == bidId:
                return bid
            
        return None
    
    @classmethod
    def removeFromList(cls, bidId):  # uses a for loop to search the list by the bidId and then removes when found
        for bid in cls.bidList:
            if bid.bidId == bidId:
                cls.bidList.remove(bid)

    @classmethod
    def printList(cls):  # uses the Bid printBid function to print each bid in the list
        for bid in cls.bidList:
            bid.printBid()

    @classmethod
    def size(cls):  # returns the size of the list
        return len(cls.bidList)