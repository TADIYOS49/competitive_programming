from collections import deque
x,y =map(int,input().split())
def bfs(n, m):
    if n >= m:
        return n - m
    q = deque([(m, 0)])
    while q:
        x, d = q.popleft()
        if x == n:
            return d
        if x < n:
            return d + n - x
        if x % 2 == 0:
            q.append((x // 2, d + 1))
        else:
            q.append((x + 1, d + 1))
print(bfs(x,y))
