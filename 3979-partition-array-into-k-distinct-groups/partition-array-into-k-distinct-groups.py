class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        # return d

            


        for i in d.values():
            if i>(len(nums)//k):
                return False
        if len(nums)%k==0:
            return True
        return False
        