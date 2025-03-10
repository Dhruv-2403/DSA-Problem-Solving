class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        x=nums[0]
        y=nums[0]
        for i in range(1,n):
            x=max(nums[i],nums[i]+x)

            y=max(x,y)

        max1=float("inf")
        min1=max1
        min2=max1
        for i in range(n):
            if min1>0:
                min1=nums[i]
            else:
                min1+=nums[i]
            min2=min(min1,min2)
        if y>abs(min2):
            return y
        return abs(min2)
        