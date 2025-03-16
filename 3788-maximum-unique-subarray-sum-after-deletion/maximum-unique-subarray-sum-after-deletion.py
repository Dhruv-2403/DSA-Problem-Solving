class Solution:
    def maxSum(self, nums: List[int]) -> int:
        z=0
        y=float("-inf")
        x=set()
        for i in range(len(nums)):
            if nums[i]>0:
                x.add(nums[i])
            else:
                y=max(nums[i],y)
        for i in x:
            z+=i
        if z>0:
            return z
        return y
            
            


        