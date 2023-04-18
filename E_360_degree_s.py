def solve(a,n,sumi,i):
    if i == n:
        if sumi == 0 or sumi%360 == 0:
            return True
        else:
            return False
    left = solve(a,n,sumi+a[i],i+1)
    right = solve(a,n,sumi-a[i],i+1)
    return left or right
n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
if solve(a,n,0,0):
    print("YES")
else:
    print("NO")
