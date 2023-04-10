def solve(n):
    if len(n) == 1:
        return 1
    maxi = 0
    temp = 1
    l, r = 0, 1
    while r <= len(n)-1:
        if n[r] >= n[r-1]:
            temp += 1
        if n[r] < n[r-1]:
            maxi = max(maxi,temp)
            temp = 1
            l = r
        r += 1
    maxi = max(maxi,temp)
    return maxi
leng = input()
arr = list(map(int,input().split()))
ans = solve(arr)
print(ans)