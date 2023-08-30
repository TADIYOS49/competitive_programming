class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for x in range(len(recipes)):
            for ind in ingredients[x]:
                graph[ind].append(recipes[x])
                indegree[recipes[x]] += 1
                
        res = []
        stack = supplies
        recipes = set(recipes)
        while stack:
            ans = stack.pop()
            if ans in recipes:
                res.append(ans)
            for nebour in graph[ans]:
                if indegree[nebour] == 1:
                    stack.append(nebour)
                indegree[nebour] -= 1
                
        return res
        
        
            
            