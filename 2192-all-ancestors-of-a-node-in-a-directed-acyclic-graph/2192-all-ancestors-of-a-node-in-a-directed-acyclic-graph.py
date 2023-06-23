class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x,y in edges:
            graph[x].append(y)
            indegree[y] += 1
        ancestor = [set() for i in range(n)] 
        stack = [i for i in range(n) if i not in indegree]
        while stack:
            ans = stack.pop()
            curr = set([ans])
            curr.update(ancestor[ans])
            for nebour in graph[ans]:
                ancestor[nebour].update(curr)
                indegree[nebour] -= 1
                if indegree[nebour] == 0:
                    stack.append(nebour)
        for i in range(n):
            ancestor[i] = sorted(ancestor[i])
        return ancestor