class Solution(object):
    def smallestBalancedIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=list(range(len(nums)))
       
        l=sum(nums)
        # sum1=0
        prod1=1
        for i in reversed(x):
            # print(i)
            l-=nums[i]
            # print(l)


            if l==prod1:
                return i
            

            prod1*=nums[i]
        return -1
        