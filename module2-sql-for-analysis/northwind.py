import sqlite3

# Connect to Database
connection1 = sqlite3.connect("northwind_small.sqlite3")

# Need a cursor to execute queries
pg_curs1 = connection1.cursor()

connection1.commit()
connection1.close()

#- What are the ten most expensive items (per unit price) in the database?
# SELECT ProductName, UnitPrice, UnitsInStock
# FROM Product
# WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM ProductName)
# ;

# - What is the average age of an employee at the time of their hiring? (Hint: a
#   lot of arithmetic works with dates.)

# Join
# - What are the ten most expensive items (per unit price) in the database *and*
#   their suppliers?

# - What is the largest category (by number of unique products in it)?


#Part 4
# - In the Northwind database, what is the type of relationship between the
#   `Employee` and `Territory` tables?
# - What is a situation where a document store (like MongoDB) is appropriate, and
#   what is a situation where it is not appropriate?
# - What is "NewSQL", and what is it trying to achieve?
