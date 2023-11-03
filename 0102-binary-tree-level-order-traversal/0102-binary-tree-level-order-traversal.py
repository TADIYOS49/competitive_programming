# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        result = [[root.val]]
        
        count = 1
        
        que = deque([root])
        
        
        temp_res = []
        
        while que:
            
            
            if count == 0:
                count = len(que)
                result.append(temp_res.copy())
                temp_res = []
                
            pop = que.popleft()
            count -= 1
            
            if pop.left:
                print(pop.left.val)
                temp_res.append(pop.left.val)
                left = pop.left
                que.append(left)
                
            if pop.right:
                temp_res.append(pop.right.val)
                right = pop.right
                que.append(right)
                
        return result
            
                
            
        
        
        
        