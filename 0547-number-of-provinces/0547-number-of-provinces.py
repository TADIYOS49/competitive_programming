class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        for node in range(len(isConnected)):
            for value in range(len(isConnected[node])):
                if isConnected[node][value] == 1:
                    graph[node+1].append(value+1)
        def dfs(nod):
            visited.add(nod)
            for item in graph[nod]:
                if item not in visited:
                    dfs(item)
            return 1
        count = 0
        for nod in range(len(isConnected)):
            if nod+1 not in visited:
                count += dfs(nod+1)       
        return count
            