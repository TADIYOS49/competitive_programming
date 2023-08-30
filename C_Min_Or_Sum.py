t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(30):
        cnt = 0
        for j in range(n):
            if a[j] & (1 << i):
                cnt += 1
        if cnt == 1:
            for j in range(n):
                if a[j] & (1 << i):
                    b[j] |= (1 << i)
    ans = sum(b)
    print(ans)