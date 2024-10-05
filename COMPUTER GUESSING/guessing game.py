import random
low = 1
high=100
player=(input("enter number"))
while True:
    computer=random.randint(low,high)
    
    if player == computer:
        low = computer+1
        print("low") 

    elif player == computer:
        high = computer+1
        print("High")

    elif player == computer:
        print("Correct Answer")
        break  

    else:
        print("invalid")    
