#============================================================================
# Name        : Python_List_Sorting.py
# Author      : Michael McBrayer
# Version     : 1.0
# Copyright   : Copyright © 2017 SNHU CODE
# Description : CS-449 Capstone Project to port LinkedList.cpp to Python
#============================================================================

import time
from Python_List_Classes import Bid, PythonList
from Python_List_Functions import createBid, loadBids, getBidId, printTimeElapsed
from Python_List_Sorting_Functions import sortList, evalSort


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
        print("  7. Evaluate Sorting Times")
        print("  8. Sort List")
        print("  9. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("\nInvalid input.  Please choose from the options listed. (1-9)\n")
            continue

        match choice:
            case 1:
                print()
                bid = createBid()
                PythonList.appendList(bid)
                print("\nNew bid appended to list: ")
                Bid.printBid(bid)
                print()

            case 2:
                print()
                bid = createBid()
                PythonList.prependList(bid)
                print("\nNew bid prepended to list: ")
                Bid.printBid(bid)
                print()

            case 3:
                print()
                startTime = time.time()
                loadBids()
                print(f"{PythonList.size()} bids read")
                endTime = time.time()
                printTimeElapsed(startTime, endTime)
                print()

            case 4:
                print()
                PythonList.printList()
                print(f"\n{PythonList.size()} items in list.")
                print()

            case 5:
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

            case 6:
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

            case 7:
                print()
                evalSort(PythonList.bidList)

            case 8:
                print()
                PythonList.bidList = sortList(PythonList.bidList)
            
            case 9:
                print("Good bye.\n\n")
                break
            
            case _:
                print("\nInvalid option.  Please try again.\n")