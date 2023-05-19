class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = []
        self.sumi = 1
        def inbound(row,col):
            return (0 <= row < len(grid[0])) and (0 <= col < len(grid))
        def dfs(self,nod):
            visited.add((nod[0],nod[1]))
            for di,dj in [0,1],[1,0],[0,-1],[-1,0]:
                newrow = di + nod[0]
                newcol = dj + nod[1]
                if inbound(newcol,newrow) and (newrow,newcol) not in visited and grid[newrow][newcol] == 1:
                    self.sumi += 1
                    dfs(self,[newrow,newcol])
            
        for vleng in range(len(grid)):
            for hleng in range(len(grid[0])):
                if grid[vleng][hleng] == 1 and (vleng,hleng) not in visited:
                    dfs(self,[vleng,hleng])
                    ans.append(self.sumi)
                    self.sumi = 1
                elif grid[vleng][hleng] == 0:
                    ans.append(0)

        return max(ans)
                
        