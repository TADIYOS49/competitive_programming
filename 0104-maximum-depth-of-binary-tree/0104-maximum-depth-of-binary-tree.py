# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        x = Solution.calc(root,count)
        return (x)
    def calc(root,count) -> int:
        if (root==None):
            return count
        return max(Solution.calc(root.left,count+1), Solution.calc(root.right,count+1))

        