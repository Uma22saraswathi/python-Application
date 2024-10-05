print("Simple calculator")
print("print 1 : add")
print("print 2 : sub")
print("print 3 : multiply")
print("print 4 : div")
a=int(input("choose an option "))
if(a in [1,2,3,4]):
    num1 = int(input("enter the first number : "))
    num2 = int(input("enter the second number : "))

    if(a==1):
        result = num1 + num2
    elif(a==2):
        result = num1 - num2
    elif(a==3):
        result = num1 * num2
    elif(a==4):
        result = num1//num2        
       
else:
    print("invalid option")    
print(f"the result is {result}")    