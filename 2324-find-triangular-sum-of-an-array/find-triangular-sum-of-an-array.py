class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
  



   
        while len(nums)>1:
            l=[]
            for i in range(len(nums)-1):

               x=(nums[i]+nums[i+1])%10
               l.append(x)

     
            nums=l[:]
        return nums[0]
        