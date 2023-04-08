# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def solve(ans,n):
            if len(n) == 0:
                return None
            mid = len(n)//2
            ans = TreeNode(n[mid])
            ans.left = solve(ans.left,n[0:mid])
            ans.right = solve(ans.right,n[mid+1:])
            return ans
        res = solve(TreeNode(),nums)
        return res
        
        