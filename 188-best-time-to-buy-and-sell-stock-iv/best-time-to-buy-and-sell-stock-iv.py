class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """




        dp=[[float("inf"),0] for _ in range(k+1)]

        for i in prices:
            for j in range(1,k+1):
                dp[j][0]=min(dp[j][0],i-dp[j-1][1])
                dp[j][1]=max(dp[j][1],i-dp[j][0])
        return dp[k][1]









                          

        