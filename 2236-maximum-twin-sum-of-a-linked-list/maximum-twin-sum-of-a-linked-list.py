from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        cont = deque()

        iterNode = head

        while iterNode is not None:
            cont.append(iterNode.val)
            iterNode = iterNode.next

        res = 0

        while cont:
            f=cont.popleft()
            f2=cont.pop()
            res=max(res,f+f2)

        return res