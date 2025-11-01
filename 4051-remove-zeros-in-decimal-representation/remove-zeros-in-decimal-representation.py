class Solution(object):
    def removeZeros(self, n):
        """
        :type n: int
        :rtype: int
        """

        s=str(n)
        l=[]
        for i in range(len(s)):
            l.append(int(s[i]))
        l2=[]
        for i in l:
            if i!=0:
                l2.append(i)
        return int("".join(map(str,l2)))










        