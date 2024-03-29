class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        ans = 0
        for u,v in roads:
            graph[u].add(v)
            graph[v].add(u)
        for node in graph:
            for snode in graph:
                if snode in graph[node] and snode != node:
                    temp = len(graph[node])- 1 + len(graph[snode])
                    ans = max(temp,ans)
                elif snode != node:
                    temp = len(graph[node]) + len(graph[snode])
                    ans = max(temp,ans)        
        return ans
                                                                                                                