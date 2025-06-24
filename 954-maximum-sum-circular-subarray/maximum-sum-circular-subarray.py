class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        x=nums[0]
        x1=nums[0]
        y=nums[0]
        y1=nums[0]

        sum1=nums[0]
        for i in range(1,len(nums)):
            x=max(x+nums[i],nums[i])
            x1=max(x1,x)
            y=min(y+nums[i],nums[i])
            y1=min(y1,y)
        
            sum1+=nums[i]

        if x1<=0:
            return x1

        cir_sum=sum1-y1
        # if cir_sum==0:
        #     return x1

        return max(x1,cir_sum)


        


        