def solve(n,arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    counts = list(freq.values())
    res = []
    for i in counts:
        if i not in res:
            res.append(i)
        else:
            while i > 0:
                if i not in res:
                    res.append(i)
                    break
                else:
                    i -= 1
    return sum(res)

q = int(input())
for _ in range(q):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
