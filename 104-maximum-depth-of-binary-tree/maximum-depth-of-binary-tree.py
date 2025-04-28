# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def hello(root,far):
            if root is None:
                return far
            return max(hello(root.left,far+1),hello(root.right,far+1))
        return hello(root,0)
            

        


        
        
        