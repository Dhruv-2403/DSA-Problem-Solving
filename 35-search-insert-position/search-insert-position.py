class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i]==target:
                return nums.index(target)
                
            elif nums[i]>target:
                return nums.index(nums[i])
            
            elif target>nums[-1]:
                return nums.index(nums[-1])+1
              
        
            
        