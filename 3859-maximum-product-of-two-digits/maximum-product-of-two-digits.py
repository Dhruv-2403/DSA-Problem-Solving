class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in str(n):
            l.append(int(i))
        l.sort()
        return l[-1]*l[-2]




        

        