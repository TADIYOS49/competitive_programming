class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        count = 0
        Total_time = 0
        chain_que = deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    chain_que.append([i,j])
                    count += 1
                    
        def out_of_range(x,y):
            if (x >=0 and x < len(grid)) and (y>=0 and y < len(grid[0])):
                return True
            else:
                return False
            

        while len(chain_que) > 0:
            
            if count == 0:
                Total_time += 1
                count = len(chain_que)
            
            pop = chain_que.popleft()
            count -= 1
            
            for u,v in ([0,1],[1,0],[0,-1],[-1,0]):
                
                x = pop[0] + u
                y = pop[1] + v
                
                if out_of_range(x,y) and grid[x][y] == 1:
                    grid[x][y] = 2
                    chain_que.append([x,y])
     
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return (-1)
                            
        return Total_time
        
                    