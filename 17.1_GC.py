"""
Name: Gio Cisneros
HW12-1
Date:5/15/2022
This program demonstrates how to build a table given a cursor execution 
The program uses sqlite,pandas, and other methods in to call this data
"""
from multiprocessing import connection
from queue import PriorityQueue
import sqlite3
import pandas as pd
fileName = input('Please specify the file name of your books database: ')
#C:\\Users\\Giovanni Cisneros\\OneDrive\\Documents\\School\\Advanced Python\\HW12\\books.db
connection = sqlite3.connect(fileName)

pd.options.display.max_columns = 10
cursor = connection.cursor()


#A
q1 = pd.read_sql('SELECT last FROM authors ORDER BY last DESC', connection) 
print("**A**",'\n',q1)

#B
q2 = pd.read_sql('SELECT title FROM titles ORDER BY title ASC', connection)
print("**B**",'\n',q2)



#E
q3= pd.read_sql("""SELECT first, last, title, isbn, copyright FROM titles INNER JOIN authors WHERE first ='Paul' ORDER BY title ASC""", connection)
print("**C**",'\n',q3)



#D
cursor.execute("""INSERT INTO authors (first, last) VALUES ('Gio','Cisneros')""")
c1= pd.read_sql('SELECT id, first, last FROM authors',connection, index_col=['id'])
print("**D**",'\n',c1)



#E
isbn = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES ('1', '0133464652')""")
isbn2 = cursor.execute("""INSERT INTO author_ISBN (id, isbn) VALUES ('2', '0133464652')""")
title= cursor.execute("""INSERT INTO titles (isbn, title,edition,copyright) VALUES ('0133464652','C How to Program 7th Edition',7,2015)""")

query1 = pd.read_sql('SELECT id, isbn FROM author_isbn',connection).tail()
query2 = pd.read_sql('SELECT isbn, title FROM titles',connection).tail()

print("**E**",'\n')
print(query1)
print(query2)
