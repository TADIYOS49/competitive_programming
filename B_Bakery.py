n, m, k = map(int, input().split())
edges = []
for _ in range(m):
    u, v, l = map(int, input().split())
    edges.append((u, v, l))
storage = set()
if k > 0:
    storage = set(map(int, input().split()))
ans = float('inf')
for edge in edges:
    if (edge[0] in storage) != (edge[1] in storage):
        ans = min(ans, edge[2])
print(ans if ans != float('inf') else -1)
