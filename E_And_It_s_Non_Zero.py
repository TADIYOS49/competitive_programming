t = int(input())
for _ in range(t):
    l, r = map(int, input().split())
    if r // 2 >= l:
        print(r % (r // 2 + 1))
    else:
        print(r - l)