class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i,j in richer:
            graph[i].append(j)
            indegree[j] +=1
            
        ans = [i for i in range(len(quiet))]
        que = deque()
        
        for item in range(len(quiet)):
            if item not in indegree:
                que.append(item)
                ans[item] = item
                
        while que:
            node = que.popleft()
            for nebr in graph[node]:
                #ans[nebr] = min(quiet[ans[node]],quiet[ans[nebr]])
                if quiet[ans[node]] < quiet[ans[nebr]]:
                    ans[nebr] = ans[node]
                if indegree[nebr] == 1:
                    que.append(nebr)
                indegree[nebr] -= 1
        return ans
                
            