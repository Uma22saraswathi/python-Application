l=list(input("enter the list of numbers"))
l.sort()
print(l)
s=(input("enter the element"))
start=0
end=len(l)-1
while(start<=end):
    mid=(start+end)//2
    if(s==l[mid]):
        print("element found at",mid)
        break
    elif(s<l[mid]):
        stop=mid-1
    else:
        start=mid+1
else:
    print("not found")
                                        