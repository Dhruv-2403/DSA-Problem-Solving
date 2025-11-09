class Solution(object):
    def minimumDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=float("inf")
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                for k in range(j+1,len(nums)):
                    if nums[i]==nums[j]==nums[k]:
                        x=min(x,abs(i-j)+abs(j-k)+abs(k-i))
        if x!=float("inf"):
            return x
        return -1


        