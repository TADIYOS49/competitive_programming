n = int(input())
p = list(map(int, input().split()))
ans = 0
for i in range(n):
    if p[p[i] - 1] == i + 1:
        ans += 1
print(ans // 2)
