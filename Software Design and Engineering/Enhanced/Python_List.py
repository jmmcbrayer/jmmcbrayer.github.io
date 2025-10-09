#============================================================================
# Name        : Python_List.py
# Author      : Michael McBrayer
# Version     : 1.0
# Copyright   : Copyright © 2017 SNHU COCE
# Description : CS-449 Capstone Project to port LinkedList.cpp to Pythoon
#============================================================================

import time
from Python_List_Classes import Bid, PythonList
from Python_List_Functions import createBid, loadBids, getBidId, printTimeElapsed

# main function to display the menu
if __name__ == "__main__":
    choice = 0

    while True:
        print("Menu:")

        print("  1. Enter a Bid (append)")
        print("  2. Enter a Bid (prepend)")
        print("  3. Load Bids")
        print("  4. Display All Bids")
        print("  5. Find Bid")
        print("  6. Remove Bid")
        print("  9. Exit")

        # to handle invalid input (ie. letters or symbosls that would cause the application to crash.)  Input accepts integers only.
        try:
            choice = int(input("Enter choice: "))
        except:
            print("\nInvalid input.  Please choose from the options listed. (1-9)\n")
            continue

        # Match case to choose what functions to call.  All supporting functions are located in Python_List_Functions.py
        match choice:
            case 1:  # Create a new bid and append to the end of the list
                print()
                bid = createBid()
                PythonList.appendList(bid)
                print("\nNew bid appended to list: ")
                bid.printBid()
                print()

            case 2:  # Create a new bid and prespend to the beginning of the list.
                print()
                bid = createBid()
                PythonList.prependList(bid)
                print("\nNew bid prepended to list: ")
                bid.printBid()
                print()

            case 3:  # Loads bid information from a csv file into the list
                print()
                startTime = time.time()
                loadBids()
                print(f"{PythonList.size()} bids read")
                endTime = time.time()
                printTimeElapsed(startTime, endTime)
                print()

            case 4:  # Prints all items in the list to the screen in the current arrangement
                print()
                PythonList.printList()
                print(f"\n{PythonList.size()} items in list.")
                print()

            case 5:  # Search the list by bid Id
                print()
                startTime = time.time()
                bidId = getBidId()

                results = PythonList.searchList(bidId)
                
                if results is not None:
                    Bid.printBid(results)
                else:
                    print(f"Bid Id {bidId} not found.")

                endTime = time.time()
                
                printTimeElapsed(startTime, endTime)
                print()

            case 6:  # Removes a bid from the list by the bid ID
                print()
                startTime = time.time()
                bidId = getBidId()

                results = PythonList.searchList(bidId)
                
                if results is not None:
                    PythonList.removeFromList(bidId)
                    print("Has been removed.")
                else:
                    print(f"Bid Id {bidId} not found.")

                endTime = time.time()

                printTimeElapsed(startTime, endTime)
                print()

            case 9:  # Exit application
                print("Good bye.\n\n")
                break
            
            case _:  # Dafault case if invalid number is entered
                print("\nInvalid option.  Please try again.\n")