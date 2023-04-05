# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def solve(n,temp):
            temp.append(n.val)
            if n.left == None and n.right == None:
                x = "->".join(str(t) for t in temp)
                ans.append(x)
            if n.left != None:
                solve(n.left,temp)
            if n.right != None:
                solve(n.right,temp)
            temp.pop()
        solve(root,[])
        return ans
        