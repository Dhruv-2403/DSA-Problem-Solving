class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] =1
    
        d2={}

            

        for i in d.values():
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        # return d2

        for i in nums:
            if d2[d[i]]==1:
                return i
        return -1
        
        
        