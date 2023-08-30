class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        
        def union(c1, c2):
            pc1 = find(c1)
            pc2 = find(c2)
            if pc1 == pc2:
                return 0
            parent[pc2] = pc1
            return 1
            
        def find(c):
            if not parent.get(c):
                parent[c] = c
                return c
            if parent[c] == c:
                return c
            boss = find(parent[c])
            parent[c] = boss
            return boss
        
        rows = {}
        cols = {}
        removed = 0
        
        for i, (row,col) in enumerate(stones):
            if row in rows:
                removed += union(i,rows[row])
            else:
                rows[row] = i
            if col in cols:
                removed += union(i,cols[col])
            else:
                cols[col] = i
                
        return removed
        
        