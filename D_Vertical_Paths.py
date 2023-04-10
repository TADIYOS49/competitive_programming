def solve(n,p)-> (int,list):
    if len(p) == 1:
        return (1,[[1]])
    paths = []
    parentnodes = set(p)
    leafnodes = []
    for x in range(len(p)):
        if (x+1) not in parentnodes:
            leafnodes.append(x+1)
    picked = []
    for i in leafnodes:
        path = [i]
        j = i - 1
        while p[j] != (j+1):
            if p[j] not in picked:
                picked.append(p[j])
                path.append(p[j])
                j = p[j]- 1
            else:
                break
        paths.append(path[::-1])
    return (len(leafnodes),paths)

    

tests = int(input())
for _ in range(tests):
    n = input()
    p = list(map(int,input().split()))
    l, paths = solve(n,p)
    print(l)
    for i in range(l):
        print(len(paths[i]))
        print(*paths[i])
    print('')

# def solve(n, nodes):
#     if len(nodes) == 1:
#         return [[1]]
#     nodes = [0] + nodes
#     leafNodes = [0] * (n+1)
#     for i in range(n+1):
#         leafNodes[nodes[i]] += 1
#     paths = []
#     visited = set()
#     for i in range(1, n+1):
#         if leafNodes[i] != 0:
#             continue
#         else:
#             cur = i
#             path = [cur]
#             visited.add(cur)
#             while nodes[cur] not in visited:
#                 path.append(nodes[cur])
#                 visited.add(nodes[cur])
#                 cur = nodes[cur]
#             paths.append(path[::-1])
#     return paths
            
                

# tests = int(input())
# for _ in range(tests):
#     n = int(input())
#     nodes = list(map(int, input().split()))
#     paths = solve(n, nodes)
#     print(len(paths))
#     for i in range(len(paths)):
#         print(len(paths[i]))
#         print(*paths[i])
#     print(" ")