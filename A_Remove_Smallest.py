def solve(n):
    n.sort()
    i = 1
    while i <= len(n)-1:
        if n[i] - n[i-1]>1:
            return "NO"
        i += 1
    return "YES"
tests = int(input())
for _ in range(tests):
    length = input()
    arr = list(map(int,input().split()))
    ans = solve(arr)
    print(ans)
