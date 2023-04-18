n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
row = []
for i in arr:
    row.append(sum(i))
col = []
for j in range(len(arr[0])):
    sumi = 0
    for i in range(len(arr)):
        sumi += arr[i][j]
    col.append(sumi)
row.sort()
totalcount = 0
for i in col:
    l,r = 0,len(row)-1
    f = -1
    while l <= r:
        mid = l + (r-l)//2
        if i > row[mid]:
            f = mid
            l = mid + 1
        else:
            r = mid - 1
    totalcount += f + 1
print(totalcount)