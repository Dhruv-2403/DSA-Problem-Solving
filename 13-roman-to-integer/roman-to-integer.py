class Solution(object):
    def romanToInt(self, s):
        x={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sum1=0
        for i in range(len(s)):
            if i<len(s)-1 and x[s[i]]<x[s[i+1]]:
                sum1-=x[s[i]]
            else:
                sum1+=x[s[i]]
        return sum1
        
        