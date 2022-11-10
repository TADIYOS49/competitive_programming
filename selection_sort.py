arr = [10,9,8,7,6,5,4,3,2,1]
n = 10
print(arr)
print("begins")
for i in range(n):
    min = i
    for j in range(i+1,n):
        if (arr[min] > arr[j]):
            min = j
    temp = arr[min]
    arr[min] = arr[i]
    arr[i] = temp         
print(arr)
