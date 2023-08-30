class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.count = 0
        def inbound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        def DFS(visited,node):
            visited.add((node[0],node[1]))
            for di,dj in [[0,1],[0,-1],[1,0],[-1,0]]:
                nebrI = node[0] + di
                nebrJ = node[1] + dj
                #print(nebrI,nebrJ,self.count)
                if not inbound(nebrI,nebrJ) or grid[nebrI][nebrJ]== 0:
                    self.count += 1
                elif (nebrI,nebrJ) not in visited:
                    DFS(visited,[nebrI,nebrJ]) 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    DFS(set(),[i,j])
                    return self.count
                    
        
            