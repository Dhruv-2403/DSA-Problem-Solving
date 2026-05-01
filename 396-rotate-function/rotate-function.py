class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        nn=len(nums)
        x=sum(nums)
        ans=0
       
        for i,j in enumerate(nums):
            ans+=(i*j)
        f=ans


        
        for k in range(1,nn):
            ans+=(x-nn*(nums[nn-k]))
            f=max(
                ans,f
            )

        return f