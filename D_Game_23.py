def solve(n,m):
    if m == n:
        return 0
    if m%n != 0:
        return -1
    s = m//n
    count = 0
    while s > 1:
        if s%2 == 0:
            s = s//2
            count += 1
        elif s%3 == 0:
            s = s//3
            count += 1
    return count  
n,m = map(int,input().split())
print(solve(n,m))