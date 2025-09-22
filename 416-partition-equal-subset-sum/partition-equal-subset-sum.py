class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if sum(nums)%2!=0:
            return False
        
        
        x=sum(nums)//2
        dp=[False]*(x+1)
        dp[0]=True
        for i in nums:
            for j in range(x,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        return dp[x]
            
            

       



