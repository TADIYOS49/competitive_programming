from collections import defaultdict
verti = int(input())
k = int(input())
graph = defaultdict(list)
def addedge(u,v):
    graph[u].append(v)
    graph[v].append(u)
def vertex(u):
    print(*graph[u])
for i in range(k):
    n = list(map(int,input().split()))
    if n[0] == 1:
        addedge(n[1],n[2])
    else:
        vertex(n[1])
