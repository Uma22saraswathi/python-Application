class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self,name,password,initial_Balance=0.0) :
        self.accounts[name]={"password":password,"balance":initial_Balance}
        print(f"account created {name}")
        print(self.accounts)

    def sign_in(self, name, password):
        if name in self.accounts or self.accounts[name]["password"] == password:
            return True
        return False

    def deposite(self,name,amount):
        if name in self.accounts:
            self.accounts[name]["balance"] += amount
            return self.accounts[name]["balance"]
        return None


    def withdraw(self,name,amount):
        if name in self.accounts:
         if amount>self.accounts[name]["balance"]:
            print("Balance is less")
            return None
        else:
            self.accounts[name]["balance"]-=amount
            return self.accounts[name]["balance"]
        return None
def main():
  bank = Bank() 

  while True:
    print("\n1. Create Account")
    print("2. Sign In")
    print("3. Exit")
   

    Choice=input("enter your choice : ")

    if Choice=='1':
       name=(input("enter the name : "))
       password=int(input("enter password : "))
       initial_balance=int(input("enter initial amount : "))
       bank.create_account(name,password,initial_balance)

    elif Choice =='2':
        name=input("enter your name : ")
        password=(input("enter password : "))
        if bank.sign_in(name,password):
            print(f"welcome{name}")

            while True:
              print('''
             press d = deposit
             press w = withdraw
             press e = exit      
             ''')
              choice=input("enter d w or e : ")
            
              if (choice=='e'):
               exit()
             
              elif choice in ['d', 'w']:
                 amount = float(input("Enter amount: "))
                 if choice == 'd':
                  result = bank.deposite(name, amount)
                  print(f"Balance after deposit: {result}")
                 else:
                  result = bank.withdraw(name, amount)
                  if result is not None:
                   print(f"Balance after withdrawal: {result}")
              else:
                print("Invalid choice. Please enter 'd', 'w', or 'e'.")
        else:
         print("Invalid credentials. Please try again.")
    elif Choice == '3':
        print("Thank you for using our banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()

 
                


