import math
def add (x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "error"
def sin(x): 
    return math.sin(math.radians(x)) 
def cos(x):
    return math.cos(math.radians(x))
def tan(x):
    return math.tan(math.radians(x))
def ln(x):
    return math.log(x)
def main():
    print("Scientific calculator")
    print("Available operations")
    print("1.Add")
    print("2.Subtract")
    print("3.multiply")
    print("4.Divide")
    print("5.sin")
    print("6.cos")
    print("7.tan")
    print("8.natural logarithm(ln)")

    choice=input("enter the number 1-8 : ")

    if choice in ('1','2','3','4'):
        num1 = float(input("enter first number"))
        num2 = float(input("enter second number"))
        if choice == '1':
            print("result : ",add(num1,num2))
        elif choice == '2':
            print("result : ",subtract(num1,num2))
        elif choice == '3':
            print("result : ",multiply(num1,num2)) 
        elif choice == '4':
            print("result : ",divide(num1,num2))
    elif choice in ('5','6','7','8'):
        num = float(input("enter a number"))
        if choice =='5':
            print("result : ",sin(num))
        elif choice == '6':
            print("result : ",cos(num))  
        elif choice == '7':
            print("result : ",tan(num))
        elif choice == '8':
            print("result : ",ln(num))
    else:
        print("invalid number")  
main()                      





    