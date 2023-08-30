inp = int(input())
maze = []
visited = set()
ans = False
def inbound(len,row,col):
    return (0<= row < 2) and (0<= col < len)
def dfs(node,n):
    global ans
    if node[0] == 1 and node[1] == n-1:
        ans = True
    visited.add((node[0],node[1]))
    for di,dj in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]:
        newrow = di + node[0]
        newcol = dj + node[1]
        if inbound(n,newrow,newcol) and (newrow,newcol) not in visited and maze[newrow][newcol] == '0':
            dfs([newrow,newcol],n)
      
for _ in range(inp):
    colnum = int(input())
    maze.append(list(input()))
    maze.append(list(input()))
    dfs([0,0],colnum)
    if ans:
        print("YES")
    else:
        print("NO")
    visited = set()
    maze = []
    ans = False
