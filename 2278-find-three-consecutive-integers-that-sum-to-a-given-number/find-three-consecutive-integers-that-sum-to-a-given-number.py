class Solution(object):
    def sumOfThree(self, num):
        x=num//3
        if sum([x-1,x,x+1])==num:
            return ([x-1,x,x+1])
        else:
            return []
        
        