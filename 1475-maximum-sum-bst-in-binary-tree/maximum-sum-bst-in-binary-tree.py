# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        max_s=[0]
        def order(node):
            if node is None:
                return True,0,float("inf"),float("-inf")
            
            is_left_bst,left_sum,left_min,left_max=order(node.left)
            is_right_bst,right_sum,right_min,right_max=order(node.right)

            if is_left_bst and is_right_bst and left_max<node.val<right_min:
                curr=node.val+left_sum+right_sum
                max_s[0]=max(max_s[0],curr)
                return True,curr,min(left_min,node.val),max(right_max,node.val)
            else:
                return False,0,0,0
        order(root)
        return max_s[0]

        


        