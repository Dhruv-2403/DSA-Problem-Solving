# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def preorderTraversal(self, root):
        l=[]
        def preorder(x,l):
        
        

    


    

            if x is None:
                return
            l.append(x.val)

            preorder(x.left,l)

            preorder(x.right,l)
        preorder(root,l)
        return l

    