class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        x=[0]*(len(nums))
        y=[0]*(len(nums))
        x[0]=nums[0]
        for i in range(1,len(nums)):

            x[i]=max(x[i-1],nums[i])
        # return x
        y[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            y[i]=min(y[i+1],nums[i])
        # return y
        for i in range(len(nums)):
            if x[i]-y[i]<=k:
                return i
        return -1



        