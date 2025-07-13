class Solution(object):
    def longestConsecutive(self, nums):
        count=1
        r=1

        nums.sort()

        if nums==[]:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                count=1
            r=max(r,count)
        return r
        