class Solution(object):
    def maxProfit(self, prices):
        
        x=prices[0]
        maxProfit=0
        for i in range(1,len(prices)):
            if prices[i]<x:
                x=prices[i]
            if prices[i]-x>maxProfit:
                maxProfit=prices[i]-x
        return maxProfit
        