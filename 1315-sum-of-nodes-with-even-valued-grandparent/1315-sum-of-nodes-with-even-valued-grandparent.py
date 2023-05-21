# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        def check(gp):
            nonlocal total
            if gp == None:
                return
            if gp.val % 2 == 0:
                if gp.left and gp.left.left:
                    total += gp.left.left.val
                if gp.left and gp.left.right:
                    total += gp.left.right.val
                if gp.right and gp.right.left:
                    total += gp.right.left.val
                if gp.right and gp.right.right:
                    total += gp.right.right.val
            check(gp.left)
            check(gp.right)
        check(root)
        return total