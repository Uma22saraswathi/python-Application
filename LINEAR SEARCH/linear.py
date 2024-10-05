my_list=[1,4,5,6,2,7]
print("list has the items :",my_list)
search_item=int(input("enter a number to search for "))
flag=0
for i in range(len(my_list)):
    if my_list[i] == search_item:
        flag=1
        print(search_item,"is found in the given position",i)
        break
if flag ==0:
    print(search_item,"is not found in the list")
