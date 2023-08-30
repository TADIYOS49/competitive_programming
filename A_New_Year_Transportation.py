leng,t = map(int,input().split())
a = list(map(int,input().split()))
i = 0
ans = False
while i <= t-1:
    if i == t-1:
        ans = True
    i = a[i] + i
if ans:
    print("YES")
else:
    print("NO")