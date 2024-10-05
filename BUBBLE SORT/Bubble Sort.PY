def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        swapped=False
        print("i value ",i)
        for j in range(0,n-i-1):
            print("j value ",j)
            if arr[j] > arr [j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped=True
            print(arr) 
        if not swapped:
            break
    return arr

unsorted_list=[6,7,8,2,1]   
sorted_list=bubble_sort(unsorted_list) 
print(sorted_list)    

   

        

             




