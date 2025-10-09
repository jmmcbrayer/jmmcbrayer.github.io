---
layout: default
title: ePortfolio
---

# Professional Self-Assessment

TODO: Update professional Self-Assessment content

<br>

# Code Review

A video walkthrough of the original applications prior to enhancement.

<iframe width="600" height="355"
  src="https://www.youtube.com/embed/K1w2KWmQNFo?si=MGUWxVfmIZuQEB9N" 
  title="YouTube video player" 
  frameborder="0" 
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
  referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
</iframe>

<br>

# Course Outcomes

- **Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science**
  - TODO: Update with how this was met

- **Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts**
  - TODO: Update with how this was met

- **Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices**
  - TODO: Update with how this was met

- **Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals**
  - TODO: Update with how this was met

- **Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources**  
  - TODO: Update with how this was met

<br>

# Enhancments

## Software Design and Engineering
[**Original Code**](https://github.com/jmmcbrayer/jmmcbrayer.github.io/tree/main/Software%20Design%20and%20Engineering/Original/LinkedList)  
[**Enhanced Code**](https://github.com/jmmcbrayer/jmmcbrayer.github.io/tree/main/Software%20Design%20and%20Engineering/Enhanced)

The artifact used for this enhancement was an application written during my CS-300 Data Structures and Algorithms classwork called LinkedLists.  This was an application written in C++ that would provide the user with several options to input and work with bid data that was for a fictitious local government project.  The menu would ask the user for input to enter in a single bid information, import a list of bids into the application from a csv file, print the list, search the list, and remove a single bid as well.

I chose this artifact to include in my ePortforlio because my plan to satisfy this category was to port an application over from one language to another.  In this case I ported the C++ based application over to Python and was able to perfectly replicate the functionality of the original application and also provide several missing functions as well.  The specific components of the artifact that showcase my skills and abilities is to demonstrate my ability to develop a fully functional application, with proper code isolation using multiple files, and utilizing components of object-oriented programing that was partially absence from the original application.  I was also able to add in completely new features as well that include the ability to prompt the user for input for searching, removal, and filenames.

I was able to meet the course outcomes I planned to meet with this enhancement by fulfilling the requirements of the Software Design and Engineering sections but also demonstrating my ability to develop secure and reliable coding.  Each function is broken down into simple sections for easy support and error handling can gracefully deal with invalid input and provide useful information to the user instead of crashing the application.  At this point I do not believe there is any update needed for my outcome-coverage plans as the other sections will address the remaining items.

During the process of enhancing the artifact I was able to reflect and review the variations between these two programming languages and see where there are shortcomings and advantages to each.  One example is that in C++ it required another support application to handle the csv files that added more complications and overhead to the application.  In Python there is a csv library that simplifies this process and speeds up the implementation of that particular component.  As far as challenges as the original C++ application is not using objects to store data, but rather vectors I had to remember and/or figure out how to properly implement these using Python.  It took a little bit of reading online, but I was quickly able to wrap my mind around what was needed and implemented the classes to handle both the bid objects and to build and handle the list.


## Algorithms and Data Structures	
[**Original Code**](https://github.com/jmmcbrayer/jmmcbrayer.github.io/tree/main/Algorithms%20and%20Data%20Structures/Original)  
[**Enhanced Code**](https://github.com/jmmcbrayer/jmmcbrayer.github.io/tree/main/Algorithms%20and%20Data%20Structures/Enhanced)

The artifact used for this enhancement was also an application written during my CS-300 Data Structures and Algorithms classwork using a combination of the ported LinkeLists application with an additional enhancement from the VectorSorting application.  The application retains it original functionality to input data into a list but has been enhanced to include the ability to sort the data in multiple ways.  Not only were the algorithms from VectorSorting included, but also some additional ones demonstrating the difference in efficiency depending on what was used.  Ultimately the build in Python sorting algorithm was the most efficient, but for demonstration purposes several can be evaluated for comparison.	

I chose this artifact to include in my ePortfoloio because it allows me to demonstrate not only further building on an existing application, but also different ways that data can be manipulated and sorted to make it more useful to the user.  The data is already being structured in a list, and this enhancement introduces algorithms to sort the data by either the ID or the title of every bid that is loaded in.  The application will evaluate multiple sorting algorithms and let the user know the most efficient one.  This provides an example of a real-world situation where data is being collected but may not be in a very useful order.  While there are options to search for information, when reviewing the list, it may be difficult to find particular pieces of information. Being able to quickly and easily organize it is a common need when working with a data set.

I was able to meet the course outcomes I planned to meet with this enhancement by fulfilling the requirements of the Algorithms and Data Structures sections but also further demonstrating my ability to develop secure and reliable coding.  As with the first enhancement each function is broken down into simple sections for easy support and error handling can gracefully deal with invalid input and provide useful information to the user instead of crashing the application.  At this point I do not believe there is any update needed for my outcome-coverage plans as the other sections will address the remaining items.

During the process of enhancing the artifact I was able to reflect and review the variations between the different ways and algorithms used to manipulate and sort a data set.  Python does have its own sorting algorithms built in and is used as well, but as the assignment was to develop sorting algorithms, I incorporated those as well.  I was able to port over the algorithms from the C++ VectorSorting application in a similar manner to the LinkedList application, but during my research I found several other sorting algorithms that were more efficient than some of the others used.  It took a little bit of reading online, but I was able to get them working in my application.  In the end I discovered that the built in sorting Python provides is the most efficient and decided to use that as my primary sorting option, but the others are there for demonstration.


## Databases
[**Original Code**](https://github.com/jmmcbrayer/jmmcbrayer.github.io/tree/main/Databases/Original)  
[**Enhanced Code**](https://github.com/jmmcbrayer/jmmcbrayer.github.io/tree/main/Databases/Enhanced)
The artifact used for this enhancement was a database designed, deployed and updated in my DAD-220 Database classwork.  This was originally part of the final project to build a basic database and run a few queries using different SQL statements.  Build a SQL script that would build a new database and populate it with a modified set of data that could be used with some other queries to demonstrate more advanced functionality.  So, for this the original database and table structure were reproduced with a script and then the queries allow us to pull data in different ways that would be useful in a business.

I chose this artifact to include in my ePortfoloio because it allows me to demonstrate my ability to build and manipulate data in mySQL from starting from nothing and having a fully functional and usable database.  The script was developed to show the original queries that were included in the original project.  Another script demonstrates how to build the database, create the tables, populate from csv files (but could also add in data directly from the script).  The final New_Scripts.sql is a combination of all the new queries that pull and present data in a variety of ways.   was able to meet the course outcomes I planned to meet with this enhancement by fulfilling the requirements of the Database sections showing creation and manipulation of a database.  All scripts were tested to validate proper functionality, and screenshots were captured to demonstrate each.

During the process of enhancing the artifact I was able to reflect and review on how SQL queries are structured and different techniques that can be implemented.  I was able to learn how to build a SQL script and how it is run in a database to automate tasks.  I also had to do a bit of research on SQL queries to learn how they should be structured when you do more advanced things including sub queries.  When working with more basic queries you don’t really have to use aliases to identify fields, but I found that with subqueries it becomes necessary as SQL was returning a lot of ambiguous error messages.  At first, I thought it was easier to follow the logic of a query with full names, but at the end of this enhancement I found that aliases are even easier and faster to work with when designing queries.  By the end of this enhancement I was not only able to demonstrate complex queries, but also more efficient design.

<br>

# Contact

You can reach me on [GitHub](https://github.com/jmmcbrayer) or email me at *jmmcbrayer@gmail.com*.