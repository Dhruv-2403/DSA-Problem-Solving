class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        sum1=0
        n=len(nums)
        for i in range(n):
            start=max(0,i-nums[i])
            sum1+=sum(nums[start:i+1])
        return sum1


        