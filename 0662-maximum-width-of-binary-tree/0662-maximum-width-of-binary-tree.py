# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        leveldict = defaultdict(lambda: [float("inf"),float("-inf")])
        maxi = 0
        def solve(root,l,index):
            nonlocal maxi
            if root == None:
                return 
            leftchild = 2*index
            rightchild = (2*index) + 1
            minind= leveldict[l][0]
            maxind = leveldict[l][1]
            leveldict[l] = [min(minind,index),max(maxind,index)]
            maxi = max(maxi,(leveldict[l][1]-leveldict[l][0])+1)
            return solve(root.left,l+1,leftchild) or solve(root.right,l+1,rightchild)
        solve(root,0,0)
        return maxi
        
    """
    2:0,1
    3:0,3
    """
        