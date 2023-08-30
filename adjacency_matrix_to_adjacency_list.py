from collections import defaultdict
leng = int(input())
graph = defaultdict(list)
for i in range(leng):
    row = list(map(int,input().split()))
    for item in range(len(row)):
        if row[item] == 1:
            graph[i+1].append(item+1)
for i in range(1,leng+1):
    print(len(graph[i]),*graph[i])
