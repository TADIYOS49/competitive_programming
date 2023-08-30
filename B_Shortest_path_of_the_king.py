source= input()
dest = input()
source = str(ord(source[0]) - 96) + source[1]
dest = str(ord(dest[0]) - 96) + dest[1]
ans = []
visited = set()
def inbound(row,col):
    return (1<= row <= 8) and (1<= ord(col)<= 8)
def dfs(nod,combo):
    if nod == dest:
        ans.append(combo)
        return
    visited.add((nod[0],[1]))
    for di,dj in [-1,0],[1,0],[0,1],[0,-1],[-1,1],[-1,-1],[1,1],[1,-1]:
        newrow = int(nod[0]) + di
        newcol = int(nod[1]) + dj
        if inbound(newrow,newcol) and (str(newrow),str(newcol)) not in visited:
            combo.append([di,dj])
            dfs([newrow,newcol],)
dfs(source,[])
res = []
for i in ans:
    
