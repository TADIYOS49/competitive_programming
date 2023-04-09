# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        x = Solution.calc(root,val)
        return (x)
    def calc(root,val)-> Optional[TreeNode]:
        if not root:
            return None
        if (root.val == val):
            return root
        return Solution.calc(root.left,val) or Solution.calc(root.right,val)