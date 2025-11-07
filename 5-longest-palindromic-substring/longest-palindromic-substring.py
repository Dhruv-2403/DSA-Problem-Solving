class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def exp(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return l+1,r-1
        x,y=0,0
        for i in range(len(s)):
            l1,r1=exp(i,i)
            l2,r2=exp(i,i+1)








            if r1-l1>y-x:
                x,y=l1,r1
            if r2-l2>y-x:
                x,y=l2,r2
        return s[x:y+1]












        