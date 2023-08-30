class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [i for i in range(n)]
        def find(child):
            if graph[child] == child:
                return child
            return find(graph[child])
        
        def uni(child, parent):
            rep = find(child)
            rep1 = find(parent)
            graph[rep] = graph[rep1]
        
        for i,j in edges:
            uni(i,j)
        if find(source) == find(destination):
            return True
        else:
            return False
        