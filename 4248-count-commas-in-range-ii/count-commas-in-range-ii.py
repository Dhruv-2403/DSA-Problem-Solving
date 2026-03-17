class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0

        for i in range(1,6):
        
            count+=max(0,((n-(1000**i))+1))
        return count
        