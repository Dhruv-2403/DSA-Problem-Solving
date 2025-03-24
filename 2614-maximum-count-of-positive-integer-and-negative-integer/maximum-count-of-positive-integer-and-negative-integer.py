class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count=0
        count1=0
        for i in nums:
            if i>0:
                count+=1
            if i<0:
                count1+=1
        return max(count,count1)
        