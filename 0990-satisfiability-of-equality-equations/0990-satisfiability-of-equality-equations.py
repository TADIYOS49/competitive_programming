class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def union(c1, c2):
            pc1 = find(c1)
            pc2 = find(c2)
            if pc1 == pc2:
                return
            parent[pc2] = pc1
        
        def find(c):
            if not parent.get(c):
                parent[c] = c
                return c
            if parent[c] == c:
                return c
            
            return find(parent[c])
        
        for eq in equations: 
            if eq[1] == '=':
                x, y = eq[0], eq[3]
                union(x, y)
        
        for eq in equations:
            if eq[1] == '!':
                if find(eq[0]) == find(eq[3]):
                    return False
        return True