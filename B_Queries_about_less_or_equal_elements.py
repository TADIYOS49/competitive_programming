def solve(arr,x):
    if arr[0] > x:
        return 0
    if arr[-1] < x:
        return len(arr)
    l, r = 0, len(arr)-1
    f = 0
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] > x:
            r = mid -1
        elif arr[mid] <= x:
            f = mid
            l = mid + 1
    return f + 1
l1, l2 = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
res = []
for i in arr2:
    temp = solve(arr1,i)
    res.append(str(temp))
print(" ".join(res))