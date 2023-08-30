n = int(input())
s1 = input()
s2 = input()
parent = [i for i in range(26)]
size = [0] * 26
sol = []
def union(n1,n2,size,parent):
    p1 = find(n1)
    p2 = find(n2)
    if p1 != p2:
       if size[p1] >= size[p2]:
          parent[p2] = p1
          size[p1] += size[p2]
       else:
          parent[p1] = p2
          size[p2] += size[p1]
       x = chr(p1+ord('a'))
       y = chr(p2+ord('a'))
       sol.append([x,y])
def find(n):
   if parent[n] != n:
      parent[n] = find(parent[n])
   return parent[n]
for i,j in zip(s1,s2):
   i = ord(i) - ord('a')
   j = ord(j) - ord('a')
   union(i,j,size,parent)

print(len(sol))
for i in range(len(sol)):
   print(*sol[i])
   
   

