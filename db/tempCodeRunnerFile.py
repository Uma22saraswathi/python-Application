import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="uma1234",
  database = "uma"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name varchar(255),address varchar(255))")

mydb.commit()