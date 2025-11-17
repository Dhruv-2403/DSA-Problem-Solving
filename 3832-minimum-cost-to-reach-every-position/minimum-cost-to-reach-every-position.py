class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        a=[float("inf")]*(len(cost))
        for i in range(len(cost)):
            a[i]=min(cost[i],a[i-1])
        return a
