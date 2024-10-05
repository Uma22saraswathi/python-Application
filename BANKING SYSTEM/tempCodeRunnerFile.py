import random
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="uma1234",
  database="IOP_Bank"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE IOP_Bank")
# mycursor.execute("CREATE TABLE User_details(ID INT AUTO_INCREMENT PRIMARY KEY,Name VARCHAR(255), Password VARCHAR(255),Balance int)")
# mycursor.execute("CREATE TABLE User_accounts(ID INT AUTO_INCREMENT PRIMARY KEY,Account_number int,Balance int)")

# mycursor.execute("""
# CREATE TABLE  User_details(
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     Name VARCHAR(255),
#     Password VARCHAR(255),
#     Balance INT,
             
# )
#  """)

mycursor.execute("""
CREATE TABLE  User_accounts(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    user_ID INT,
    Account_number INT,
    Balance INT,
    CONSTRAINT FK_user_id FOREIGN KEY (user_ID) REFERENCES User_details(ID)
)
""")