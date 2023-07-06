class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [i for i in range(len(edges)+1)]
        def find(child):
            if graph[child] == child:
                return child
            return find(graph[child])
        def uni(child,parent):
            p1 = find(child)
            p2 = find(parent)
            graph[p1] = graph[p2]
            
        for i,j in edges:
            if find(i) == find(j):
                ans = [i,j]
            uni(i,j)
            
        return ans
        