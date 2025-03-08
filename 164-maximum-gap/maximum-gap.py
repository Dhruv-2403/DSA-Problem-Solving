class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        nums.sort(reverse=True)
        if len(nums)<2:
            return 0
        else:
            x=nums[0]
            y=0
            for i in range(1,len(nums)):
                x=x-nums[i]
                y=max(y,x)
                x=nums[i]
            return y

                


            



        