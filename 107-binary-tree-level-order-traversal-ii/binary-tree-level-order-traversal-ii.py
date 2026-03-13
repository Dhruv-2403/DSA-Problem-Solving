# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root):
        l=deque([root])

        if not root:
            return []
        l3=[]
        while l:
            l2=[]
            for _ in range(len(l)):
                node=l.popleft()

                l2.append(node.val)

                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            l3.append(l2)
        return l3[::-1]

                
        