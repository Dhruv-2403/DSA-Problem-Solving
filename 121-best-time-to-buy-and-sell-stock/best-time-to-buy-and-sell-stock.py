class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        x=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            if prices[i]<x:
                x=prices[i]
            if prices[i]-x>maxProfit:
                maxProfit=prices[i]-x
        return maxProfit
        