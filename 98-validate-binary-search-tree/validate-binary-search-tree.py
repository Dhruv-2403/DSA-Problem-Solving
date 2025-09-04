# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res=[]
        def inorder(node):
            if node is None:
                return 
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        for i in range(1, len(res)):
            if res[i] <= res[i-1]:
                return False
        return True

        
        