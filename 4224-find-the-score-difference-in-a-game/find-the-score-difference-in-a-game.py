class Solution(object):
    def scoreDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=0
        y=0
        flag=True
        for i in range(len(nums)):
            if nums[i]%2==1:
                flag=not flag
            if i%6==5:
                flag=not flag
            if flag:
                x+=nums[i]
            else:
                y+=nums[i]
        return x-y
                
        