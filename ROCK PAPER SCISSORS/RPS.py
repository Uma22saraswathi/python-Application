import random
options = ['rock','paper','scissors']
computer = random.choice(options)
player = input('enter your move : ').lower()

if player == computer:
    print("tie")
elif player == 'rock':
    if computer == 'scissors':
        print("the computer played scissors, you  win the game")
    else:
        print("the computer played paper you  lose the game")    
elif player == 'paper':
    if computer == 'scissors':
        print("The computer played Scissors, you  lose the game")
    else:
        print("The computer played rock , you  win the game") 
elif player =='scissors':
    if computer == 'paper':
        print("The computer played paper you  win the game")
    else:
        print("The computer played rock you  lose the game")  



    

