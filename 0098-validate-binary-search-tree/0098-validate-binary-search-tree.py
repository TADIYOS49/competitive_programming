# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(left,root,right):
            if not root:
                return True
            return left < root.val < right and solve(left,root.left,root.val) and solve(root.val,root.right,right)
        return solve(float("-inf"),root,float("+inf"))