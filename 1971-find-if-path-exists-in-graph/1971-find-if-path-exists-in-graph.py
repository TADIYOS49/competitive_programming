class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        queue = deque([source])
        for node1,node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        print(graph)
        # def dfs(node):
        #     if node == destination:
        #         return True
        #     visited.add(node)
        #     for i in graph[node]:
        #         if i not in visited:
        #             found = dfs(i)
        #             if found:
        #                 return True
        #     return False
        def bfs():
            while queue:
                node = queue.popleft()
                for nebour in graph[node]:
                    if nebour not in visited:
                        visited.add(nebour)
                        queue.append(nebour)
                        if nebour == destination:
                            return True
            if source == destination:
                return True
            return False
                
        return bfs()
        
        
        