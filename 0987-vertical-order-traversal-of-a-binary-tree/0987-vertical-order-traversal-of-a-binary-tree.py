# Definition for a binary tree node.
# class TreeNode:
#     def init(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic={}
        def solve(node,row,col):
            if not node:
                return 
            next_node_row_position=row+1
            next_node_col_position=col+1
            if col in dic:
                dic[col].append([node.val,row])
            else:
                dic[col]=[[node.val,row]]
            solve(node.right,next_node_row_position,next_node_col_position)
            next_node_row_position=row+1
            next_node_col_position=col-1
            solve(node.left,next_node_row_position,next_node_col_position)
        solve(root,0,0)        
        res=[]
        for i in dict(sorted(dic.items())):
            d=[x[0] for x in sorted(dic[i],key=lambda x:(x[1],x[0]))]
            res.append(d)

        return res