"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.ans = 0
        visited = set()
        if root == None:
            return 0
        def dfs(self,nod,count):
            #print(node.children)
            if nod.children == []:
                if self.ans < count:
                    self.ans = count
                return
            for i in nod.children:
                dfs(self,i,count+1)  
        dfs(self,root,1)
        return self.ans
        