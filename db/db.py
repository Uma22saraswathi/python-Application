import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="uma1234",
  database = "uma"
)

mycursors = mydb.cursor()

# mycursor.execute("SHOW DATABASES ")
# mycursors.execute("CREATE TABLE customers (name varchar(255),address varchar(255)")
mycursors.execute("INSERT INTO customers values('uma','abcd street')")
mycursors.execute("select * from customers")
myresult=mycursors.fetchall()
print(myresult)
mydb.commit()

# for x in mycursor:
#   print(x)