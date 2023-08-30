class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        sources = [1] * n
        ans = []
        for edge in edges:
            sources[edge[1]] = 0
        for i in range(len(sources)):
            if sources[i] == 1:
                ans.append(i)
        return ans