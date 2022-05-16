#Program Documentation
"""
Name: Gio Cisneros
HW12-2
Date:5/15/2022
This program demonstrates how to build a table given a cursor execution 
The program uses sqlite,pandas, and other methods in to call this data
"""
from multiprocessing import connection
from queue import PriorityQueue
import sqlite3
import pandas as pd

#C:\\Users\\Giovanni Cisneros\\OneDrive\\Documents\\School\\Advanced Python\\HW12\\books.db
#fileinput
fileName = input('Please specify the file name of your books database: ')
#connect to file name
connection = sqlite3.connect(fileName)

#set cursor connection
cursor = connection.cursor()
#exec all titles
cursor.execute("""SELECT * FROM titles""")

result = cursor.fetchall()
col = cursor.description
df = pd.DataFrame(result, columns=['ISBN', 'Title', 'Edition','Copyright'])
print(df)
