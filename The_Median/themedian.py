arr = [1,8,9,8,3,56,24,2,478,7]
arr.sort()
print(arr)
size = round(len(arr) / 2)
if (arr[size - 1] == arr[size]):
    print("The median is: " , arr[size])
elif (arr[size - 1] < arr[size]):
    print("The median is: " , ((arr[size-1] + arr[size])/2))
else:
    print("The median is: " , ((arr[size - 1] + arr[size])/2))
    
