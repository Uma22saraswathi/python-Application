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

# mycursor.execute("""
# CREATE TABLE  User_accounts(
#     ID INT AUTO_INCREMENT PRIMARY KEY,
#     user_ID INT,
#     Account_number INT,
#     Balance INT,
#     CONSTRAINT FK_user_id FOREIGN KEY (user_ID) REFERENCES User_details(ID)
# )
# """)
# sql = "DROP TABLE User_accounts"

# mycursor.execute(sql)
mydb.commit() 




class Bank:
    def __init__(self):
         self.accounts = {}

    def create_account(self, name, password, initial_balance=0.0):
        if name in self.accounts:
            print(f"Account with name {name} already exists.")
            return
        self.accounts[name] = {"password": password, "balance": initial_balance}
        print(f"Account created for {name}")

    def sign_in(self, name, password):
        if name in self.accounts and self.accounts[name]["password"] == password:
            return True
        return False

    def deposit(self, name, amount):
        if name in self.accounts:
            self.accounts[name]["balance"] += amount
            return self.accounts[name]["balance"]
        return None

    def withdraw(self, name, amount):
        if name in self.accounts:
            if amount > self.accounts[name]["balance"]:
                print("Insufficient balance")
                return None
            self.accounts[name]["balance"] -= amount
            return self.accounts[name]["balance"]
        return None
def generate_account_number():
        return random.randint(1000,9999)    

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
            mycursor = mydb.cursor()

            sql = "INSERT INTO user_details (name,password,Balance) VALUES (%s, %s, %s)"
            val = (name, password,initial_balance)
            mycursor.execute(sql, val)
            mydb.commit()

        elif choice == '2':
            name = input("Enter your name: ")
            password = input("Enter password: ")
            if bank.sign_in(name,password):
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

                        account_number=generate_account_number()
                        mycursor = mydb.cursor()
                        sql = "INSERT INTO user_accounts (account_number,Balance) VALUES (%s, %s)"
                        val = (account_number, amount)
                        mycursor.execute(sql, val)

                        mydb.commit()


                        if action == 'd':
                            result = bank.deposit(name, amount)
                            print(f"Balance after deposit: {result}")
                        else:
                            result = bank.withdraw(name, amount)
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