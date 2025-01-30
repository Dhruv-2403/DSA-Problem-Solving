class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        x=0
        for i in nums:
            if i==1:
                count+=1
                x=max(count,x)
            else:
                count=0
        return x