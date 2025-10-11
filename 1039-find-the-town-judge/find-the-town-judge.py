class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if n>1 and len(trust)==0:
            return -1
        elif len(trust)==0 or n==1:
            return 1
        
        count=[0]*(n+1)
        for i in trust:
            count[i[0]]-=1
            count[i[1]]+=1
        for i in range(len(count)):
            if count[i]==n-1:
                return i
        return -1











        
        