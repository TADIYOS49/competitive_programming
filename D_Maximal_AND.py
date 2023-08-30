t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = [0] * 31
    for i in range(n):
        for j in range(31):
            if a[i] & (1 << j):
                cnt[j] += 1
    ans = 0
    for i in range(30, -1, -1):
        if cnt[i] == n:
            ans |= (1 << i)
        elif k > 0:
            ans |= (1 << i)
            k -= 1
    print(ans)