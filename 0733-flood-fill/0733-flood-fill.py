class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        checkval = image[sr][sc]
        visited = set()
        def inbound(row,col):
            return (0<= row < len(image)) and (0<= col < len(image[0]))
        def dfs(node):
            visited.add((node[0],node[1]))
            for di,dj in [0,1],[0,-1],[1,0],[-1,0]:
                newrow = di + node[0]
                newcol = dj + node[1]
                if inbound(newrow,newcol) and image[newrow][newcol] == checkval and (newrow,newcol) not in visited:
                    image[newrow][newcol] = color
                    dfs([newrow,newcol])
        dfs([sr,sc])
        image[sr][sc] = color
        return image
        