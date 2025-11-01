# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # return head
        nums=set(nums)
        while head and head.val in nums:
            head=head.next
        cur=head
        while cur and cur.next:
            while cur.next and cur.next.val in nums:
                cur.next=cur.next.next
            cur=cur.next
        return head
       

        