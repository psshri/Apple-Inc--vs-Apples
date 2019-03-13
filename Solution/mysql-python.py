## need to execute this file just once

host_name = raw_input("Enter Host Name : ")
user_name = raw_input("Enter User Name : ")
password = raw_input("Enter Password : ")


import mysql.connector ## python needs a mysql driver to access the mysql database
## we will use the driver mysql connector

## create a connection to the database
mydb = mysql.connector.connect(
  host= host_name, ## enter the name of the local host
  user= user_name, ## enter the user name
  passwd= password ## enter the password used for the user in mysql
)

mycursor = mydb.cursor()

## creates a database
mycursor.execute("CREATE DATABASE intern")


## connect directly to a database after creating that databse
mydb2 = mysql.connector.connect(
  host= host_name,
  user= user_name,
  passwd= password,
  database="intern"
)

mycursor2 = mydb2.cursor()

## create a table apple to store the data
mycursor2.execute("CREATE TABLE apple ( ID int NOT NULL AUTO_INCREMENT PRIMARY KEY, TEXT LONGTEXT , CLASS LONGTEXT)")
