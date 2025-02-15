class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            x=True
            if i-k>=0:
                if nums[i]<=nums[i-k]:
                    x=False
            if i+k<len(nums):
                if nums[i]<=nums[i+k]:
                    x=False



            if x:
                count+=nums[i]

        return count
