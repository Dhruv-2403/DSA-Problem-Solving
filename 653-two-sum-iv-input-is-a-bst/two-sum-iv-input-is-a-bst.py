# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: bool
        """
        s=set()
        def help(node):

            if node is None:
                return False
            if k-node.val in s:
                return True

            s.add(node.val)
            return help(node.left) or help(node.right)

        return help(root)

        