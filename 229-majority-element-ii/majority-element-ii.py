class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
    

        l=[]
        for i,j in d.items():
            if j>n//3:
                l.append(i)
        return l
        