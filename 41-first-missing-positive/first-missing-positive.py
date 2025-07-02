class Solution(object):
    def firstMissingPositive(self, arr):
        l=[]
        for i in arr:
            if i>0:
                l.append(i)
        l.sort()
        
        x=1
        for i in l:
            if i>x:
                return x
            elif i==x:
                x+=1
        return x