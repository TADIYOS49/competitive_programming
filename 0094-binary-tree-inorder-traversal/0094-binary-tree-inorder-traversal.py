# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if root == None:
            return result
        
        def fun(rt):
            if rt.left != None:
                fun(rt.left)
            
            result.append(rt.val)
            if rt.right == None:
                return
            else:
                fun(rt.right)
        fun(root)
        return result
        