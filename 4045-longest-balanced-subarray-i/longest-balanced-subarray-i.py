class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s=0

        for i in range(len(nums)):
            e=set()
            o=set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    e.add(nums[j])
                else:
                    o.add(nums[j])
                if len(o)==len(e):
                    s=max(s,j-i+1)
        return s
        