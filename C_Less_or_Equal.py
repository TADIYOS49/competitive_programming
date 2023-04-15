leng, k = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
i = arr[k-1]
ans = -1
if k == leng:
    print(arr[k-1])
elif k == 0 and arr[0] > 1:
    print(1)
elif k == 0 and arr[0] == 1:
    print(-1)
else:
    while i < arr[k]:
        if i >= arr[k-1]:
            ans = i
            break
        i += 1
    print(ans)