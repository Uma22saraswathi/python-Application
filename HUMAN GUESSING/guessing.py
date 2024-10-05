import random
low=1
high=1000
computer=random.randint(1,1000)
#print(computer)
while True:
    guess=int(input("enter number"))
     
    if guess > 1000:
        print("invalid")
        
    elif computer < guess:
        print("high")
    elif computer > guess:
        print ("low")
        
    else:
        computer==guess
        print("Correct guessing") 
        break    
    


