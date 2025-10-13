class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        y=0
        jump=0
        for i in range(len(nums)-1):
            x=max(x,i+nums[i])
            if i==y:
                jump+=1
                y=x
        return jump






        




        