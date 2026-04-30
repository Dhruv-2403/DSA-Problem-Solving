class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        x=0
        for i in range(1,len(nums)):
            if nums[i]>nums[x]:
                x=i
        if sum(nums[:x+1])==sum(nums[x:]):
            return -1
        elif sum(nums[:x+1])>sum(nums[x:]):
            return 0
        return 1


        