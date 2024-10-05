n=str(int(input("enter the number")))
sum=0
for i in n:
    sum=sum+int(i)**len(n)
if int(n)==sum:
    print(n,"it's an armstrong number")    
else:
    print(n,"not an armstrong number")
