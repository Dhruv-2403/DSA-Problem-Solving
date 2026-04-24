class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        # score=0
        l=[]
        n=len(nums)
        for i in range(len(nums)):
            if (max(nums[:i+1])-min(nums[i:n]))<=k:
                l.append(i)
        if l==[]:
            return -1
        else:
            return l[0]