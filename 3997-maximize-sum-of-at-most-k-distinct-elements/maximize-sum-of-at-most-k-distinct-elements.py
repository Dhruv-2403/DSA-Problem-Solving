class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums=list(set(nums))
        nums.sort(reverse=True)
        return nums[:k]

        