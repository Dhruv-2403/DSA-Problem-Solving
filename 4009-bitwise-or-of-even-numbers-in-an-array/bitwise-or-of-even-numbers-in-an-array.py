class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                count|=nums[i]
        return count

        