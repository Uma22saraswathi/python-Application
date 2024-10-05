import random
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="uma1234",
  database="IOP_Bank"
)

mycursor = mydb.cursor()

# Ensure tables are created with proper structure
mycursor.execute("""
CREATE TABLE IF NOT EXISTS User_details (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255),
    Password VARCHAR(255),
    Balance INT
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS User_accounts (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    user_ID INT,
    Account_number INT,
    Balance INT,
    FOREIGN KEY (user_ID) REFERENCES User_details(ID)
)
""")

mydb.commit()

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, password, initial_balance=0.0):
        mycursor = mydb.cursor()

        # Insert user details and get the user ID
        sql = "INSERT INTO User_details (Name, Password, Balance) VALUES (%s, %s, %s)"
        val = (name, password, initial_balance)
        mycursor.execute(sql, val)
        mydb.commit()
        user_id = mycursor.lastrowid

        # Create a new account for the user
        account_number = self.generate_account_number()
        sql = "INSERT INTO User_accounts (user_ID, Account_number, Balance) VALUES (%s, %s, %s)"
        val = (user_id, account_number, initial_balance)
        mycursor.execute(sql, val)
        mydb.commit()

        print(f"Account created for {name} with account number {account_number}")
        print(f"user id {user_id} name {name}")

    def sign_in(self, name, password):
        mycursor = mydb.cursor()
        sql = "SELECT ID FROM User_details WHERE Name = %s AND Password = %s"
        val = (name, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        return result[0] if result else None
    

    def deposit(self, user_id, amount):
        mycursor = mydb.cursor()
        sql = "UPDATE User_accounts SET Balance = Balance + %s WHERE user_ID = %s"
        val = (amount, user_id)
        mycursor.execute(sql, val)
        mydb.commit()

        sql = "SELECT Balance FROM User_accounts WHERE user_ID = %s"
        val = (user_id,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        return result[0] if result else None

    def withdraw(self, user_id, amount):
        mycursor = mydb.cursor()
        sql = "SELECT Balance FROM User_accounts WHERE user_ID = %s"
        val = (user_id,)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        
        if result and result[0] >= amount:
            sql = "UPDATE User_accounts SET Balance = Balance - %s WHERE user_ID = %s"
            val = (amount, user_id)
            mycursor.execute(sql, val)
            mydb.commit()
            return result[0] - amount
        else:
            print("Insufficient balance")
            return None

    @staticmethod
    def generate_account_number():
        return random.randint(1000, 9999)

def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Sign In")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            password = input("Enter password: ")
            initial_balance = float(input("Enter initial amount: "))
            bank.create_account(name, password, initial_balance)

        elif choice == '2':
            name = input("Enter your name: ")
            password = input("Enter password: ")
            user_id = bank.sign_in(name, password)
            if user_id:
                print(f"Welcome, {name}!")
                while True:
                    print("\nOptions:")
                    print("d - Deposit")
                    print("w - Withdraw")
                    print("e - Exit to main menu")
                    
                    action = input("Enter your choice (d/w/e): ").lower()
                    
                    if action == 'e':
                        break
                    elif action in ['d', 'w']:
                        amount = float(input("Enter amount: "))
                        if action == 'd':
                            result = bank.deposit(user_id, amount)
                            print(f"Balance after deposit: {result}")
                        else:
                            result = bank.withdraw(user_id, amount)
                            if result is not None:
                                print(f"Balance after withdrawal: {result}")
                    else:
                        print("Invalid choice. Please enter 'd', 'w', or 'e'.")
            else:
                print("Invalid credentials. Please try again.")

        elif choice == '3':
            print("Thank you for using our banking system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()