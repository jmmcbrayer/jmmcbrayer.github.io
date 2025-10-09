#============================================================================
# Name        : Python_List_Sorting_Functions.py
# Author      : Michael McBrayer
# Version     : 1.0
# Copyright   : Copyright © 2017 SNHU COCE
# Description : CS-449 Capstone Project to port LinkedList.cpp to Python
#               This file provides supporting functions to implement different
#               sorting algorithms.  These were ported in part from VecroSorting.cpp.
#               Merge sort also included.
#============================================================================

import time
from Python_List_Classes import Bid, PythonList
from Python_List_Functions import printTimeElapsed
from copy import deepcopy

def partition(bidsList, begin, end):
    #set low and high equal to begin and end
    low = begin
    high = end

    # pick the middle element as pivot point
    pivot = begin + (end - begin) // 2

    pivotTitle = bidsList[pivot].title
    while True:
        # keep incrementing low index while bidsList[low] < bidsList[pivot]
        while bidsList[low].title < pivotTitle: # bidsList[pivot].title:
            low += 1

        # keep decrementing high inces while bidsList[pivot] < bidsList[high]
        while pivotTitle < bidsList[high].title:
            high -= 1
        
        if low >= high:
            break
        else:
            bidsList[low], bidsList[high] = bidsList[high], bidsList[low]
            low += 1
            high -= 1
    
    return high


def quickSort(bidsList, begin, end):
    # set mid equal to 0
    mid = 0

    # Base case: If there are 1 or zero bids to sort,
    # partition is already sorted otherwise if begin is greater
    # than or equal to end then return
    if begin >= end:
        return

    # Partition bids into low and high such that
    # midpoint is location of last element in low
    mid = partition(bidsList, begin, end)

    # recursively sort low partition (begin to mid)
    quickSort(bidsList, begin, mid)

    # recursively sort high partition (mid+1 to end)
    quickSort(bidsList, mid + 1, end)

    return bidsList    


def selectionSort(bidsList, size):
    # define min as int (index of the current minimum bid)
    minimumBid = 0

    # pos is the position within bids that divides sorted/unsorted
    # for size_t pos = 0 and less than size -1 
    for pos in range(size - 1):
        # set min = pos
        minimumBid = pos

        # loop over remaining elements to the right of position
        for pos2 in range(pos + 1, size):
            # if this element's title is less than minimum title
            if bidsList[pos2].title < bidsList[minimumBid].title:
                # this element becomes the minimum
                minimumBid = pos2
            
        # swap the current minimum with smaller one found
        # busing built in swap vectorr method
        bidsList[pos], bidsList[minimumBid] = bidsList[minimumBid], bidsList[pos]

    return bidsList


# Basic Python function's to sort a list using the merge sort algorithm
# functions merge and merge_sort
# credit: https://www.geeksforgeeks.org/dsa/merge-sort/
# code has been modified for this application, fully reviewed, and tested for proper functionality
def merge(bidsList, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = bidsList[left + i]
    for j in range(n2):
        R[j] = bidsList[mid + 1 + j]
        
    i = 0  
    j = 0  
    k = left  

    # Merge the temp arrays back
    # into bidsList[left..right]
    while i < n1 and j < n2:
        if L[i].title <= R[j].title:
            bidsList[k] = L[i]
            i += 1
        else:
            bidsList[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        bidsList[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        bidsList[k] = R[j]
        j += 1
        k += 1


def mergeSort(bidsList, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(bidsList, left, mid)
        mergeSort(bidsList, mid + 1, right)
        merge(bidsList, left, mid, right)


def pythonSort(bidsList, sortBy, descending):
    return sorted(bidsList, key=lambda bid: getattr(bid, sortBy), reverse=descending)


def sortList(bidsList): #, sortItem="bidId", reversed=False):
    choice = 0
    while True:
        print()
        print("Sorting Menu:")
        print("  1. Sort by Bid ID (ascending order)")
        print("  2. Sort by Bid Title (ascending order)")
        print("  3. Sort by Bid ID (descending order)")
        print("  4. Sort by Bid Title (descending order)")
        
        try:
            choice = int(input("Enter choice: "))
        except:
            print("\nInvalid input.  Please choose from the options listed. (1-4)\n")
            continue

        match choice:
            case 1:
                sortBy = "bidId"
                descending = False
                startTime = time.time()
                pythonSortedList = pythonSort(deepcopy(bidsList), sortBy, descending)
                endTime = time.time()
                print(f"List sorted in {printTimeElapsed(startTime, endTime)}")
                break

            case 2:
                sortBy = "title"
                descending = False
                startTime = time.time()
                pythonSortedList = pythonSort(deepcopy(bidsList), sortBy, descending)
                endTime = time.time()
                print(f"List sorted in {printTimeElapsed(startTime, endTime)}")
                break

            case 3:
                sortBy = "bidId"
                descending = True
                startTime = time.time()
                pythonSortedList = pythonSort(deepcopy(bidsList), sortBy, descending)
                endTime = time.time()
                print(f"List sorted in {printTimeElapsed(startTime, endTime)}")
                break

            case 4:
                sortBy = "title"
                descending = True
                startTime = time.time()
                pythonSortedList = pythonSort(deepcopy(bidsList), sortBy, descending)
                endTime = time.time()
                print(f"List sorted in {printTimeElapsed(startTime, endTime)}")
                break

    #print()
    #startTime = time.time()
    #print("Sorting list using Python's sort algorithm (Timsort: a hybrid of merge & insertion sort)")
    #pythonSortedList = pythonSort(deepcopy(bidsList), sortItem)
    #endTime = time.time()
    #pythonSortTime = endTime - startTime
    #print("Time for sorting data: ")
    #printTimeElapsed(startTime, endTime)

    #sortTimes = {"Quick Sort": quickSortTime,
    #             "Selection Sort": selectionSortTime,
    #             "Merge Sort": mergeSortTime,
    #             "Python Sort": pythonSortTime}
    
    #name, smallest = min(sortTimes.items(), key=lambda item: item[1])
    #print(f"\nThe most efficient sorting algorithm is {name} with a time of {smallest}\n")

    return pythonSortedList


def evalSort(bidsList, sortItem="bidId", reversed=False):
    # check size of bidsList
    size = len(bidsList)

    # if the list size is 0 or 1 its already sorted
    if size <= 1:
        return bidsList
    
    startTime = time.time()
    print("Quick sort algorithm")
    quickSortedList = quickSort(deepcopy(bidsList), 0, size - 1)
    endTime = time.time()
    quickSortTime = round((endTime - startTime), 2)
    printTimeElapsed(startTime, endTime)
    print()
    
    startTime = time.time()
    print("Selection sort algorithm")
    selectionSortedList = selectionSort(deepcopy(bidsList), size)
    endTime = time.time()
    selectionSortTime = round((endTime - startTime), 2)
    printTimeElapsed(startTime, endTime)
    print()

    startTime = time.time()
    print("Merge sort algorithm")
    mergeCopy = deepcopy(bidsList)
    mergeSort(mergeCopy, 0, size - 1)
    mergeSortedList = mergeCopy
    endTime = time.time()
    mergeSortTime = round((endTime - startTime), 2)
    printTimeElapsed(startTime, endTime)
    print()

    startTime = time.time()
    print("Python's sort algorithm (Timsort: a hybrid of merge & insertion sort)")
    pythonSortedList = pythonSort(deepcopy(bidsList))
    endTime = time.time()
    pythonSortTime = round((endTime - startTime), 2)
    printTimeElapsed(startTime, endTime)
    print()

    sortTimes = {"Quick Sort": quickSortTime,
                 "Selection Sort": selectionSortTime,
                 "Merge Sort": mergeSortTime,
                 "Python Sort": pythonSortTime}
    
    name, smallest = min(sortTimes.items(), key=lambda item: item[1])
    print(f"\nThe most efficient sorting algorithm is {name} with a time of {smallest}\n")

    return pythonSortedList