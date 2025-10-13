class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len1=0
        x=-1
        for i in nums:
            if i>=x:
                x=i
                len1+=1
        return len1
        