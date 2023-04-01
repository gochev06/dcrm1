# Install MySQL on the computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector


database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
)

# Prepare a cursor object
cursor_object = database.cursor()

# Create the database
cursor_object.execute("CREATE DATABASE dcrmdb")

print('Database created!')