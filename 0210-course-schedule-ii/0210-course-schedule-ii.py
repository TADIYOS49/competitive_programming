class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x,y in prerequisites:
            graph[y].append(x)
            indegree[x] += 1
        res = []
        stack = [i for i in range(numCourses) if i not in indegree]
        
        while stack:
            ans = stack.pop()
            res.append(ans)
            for nebour in graph[ans]:
                if indegree[nebour] == 1:
                    stack.append(nebour)
                indegree[nebour] -= 1
        if len(res) != numCourses:
            return []
        return res
                
                
        