l1, D = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
l,r = 0,len(arr)-1
sumi = arr[-1]
count = 0
while l <= r:
    if sumi > D:
        count += 1
        sumi = 0
        r -= 1
        sumi += arr[r]
    elif sumi <= D:
        sumi += arr[r]
        l += 1
print(count)

