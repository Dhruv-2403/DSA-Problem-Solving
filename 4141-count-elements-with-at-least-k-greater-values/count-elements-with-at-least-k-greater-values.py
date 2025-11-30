class Solution(object):
    def countElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
"""
        count=0
        if k==0:
            return len(nums)
        n=len(nums)
        nums.sort()
        for i in nums:
            if i<nums[n-k]:
                count+=1
        return count









        