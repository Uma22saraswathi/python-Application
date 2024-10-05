arr=[1,10,11,5,2]

for i in range (0,len(arr)-1):
    for j in range(0,len(arr)-1):
        print(arr[i] , arr[j])
        if arr[j]<arr[j+1]:
            continue
        elif arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)  
