class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """



        count_0=0
        x=0
        l=0
        for i in range(len(nums)):

            if nums[i]==0:
                count_0+=1
            if count_0>1:
                if nums[l]==0:
                    count_0-=1
                
                    
                l+=1
            x=max(x,i-l)
        return x


            
        