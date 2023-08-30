def solve(c,arr,res):
    if len(arr) == 1:
        t = arr.index(arr[0])
        #print(t)
        res[t] = c
        return 
    temp = max(arr)
    inx = arr.index(temp)
    #print(inx)
    res[inx] = c
    if inx > 0:
        solve(c+1,arr[0:inx],n)
    if inx < len(arr)-1:
        solve(c+1,arr[inx+1:],n)
    # print(left)
    # print(right)
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    res = [0] * len(arr)
    #print(res)
    ans =solve(0,arr,[0]*len(arr))
    print(ans)
